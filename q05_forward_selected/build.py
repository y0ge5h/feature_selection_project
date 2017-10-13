# Default imports
import pandas as pd
import statsmodels.formula.api as smf

data = pd.read_csv('data/house_prices_multivariate.csv')


# Your solution code here

def forward_selected(data, target):
    remaining = set(data.columns)
    remaining.remove(target)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(target,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(target,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model

