""" 

This is a program that calculates the Systematic Mean Absolute Percentage Error (SMAPE)

"""

a = [10, 15, 20]
p = [10, 15, 20]

def SMAPE(actual_values, predicted_values):

    val_sum = [(abs(i) + abs(j))/2 for i, j in zip(actual_values, predicted_values)]

    val_diff = [abs(i - j) for i, j in zip(predicted_values, actual_values)]

    val_comb = [i / j for i , j in zip(val_diff, val_sum)]

    smape = (100 / len(val_comb)) * sum(val_comb)

    return smape

print(SMAPE(a , p))
