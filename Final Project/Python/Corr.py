import pandas as pd
import numpy as np

data_path = "prosperLoanData.csv"
data = pd.read_csv(data_path)
headers = data.columns.tolist()
# print data.head()
# print headers

corr_df = pd.DataFrame()
corr_df = corr_df.append(data.corr())

# corr_df.to_csv('CorrelationData.csv')

col = list(corr_df.columns.values)
# print col
# print(corr_df.index.values)
# import matplotlib.pyplot as plt
#
# plt.matshow(data.corr())
# plt.show()


def highest_corr_below_one(num):
    h = 0
    if num < 1 and num > h:
        h = num
    return h

corr_dict = {}
new_corr_df = pd.DataFrame(columns=['var1', 'var2', 'num'])
i = 0

for head in col:
    # print corr_df[head]
    # print corr_df[head]
    highest = max(corr_df[head], key=highest_corr_below_one)
    metric = corr_df.index.values[corr_df.set_index(head).index.get_loc(highest)]
    # print highest
    # print metric
    corr_dict[i] = {'var1': head, 'var2': metric, 'num': highest}
    new_corr_df.loc[i] = [head, metric, highest]
    i += 1

# print corr_dict
# print new_corr_df

new_corr_df.to_csv('highest_corr.csv')


# need BorrowerState, BorrowerRate, LoanOriginalAmount, LoanOriginationDate, State
# need to add full state to data
data_path = "50_us_states_all_data.csv"
states = pd.read_csv(data_path)
# result = data.append(states, ignore_index=True)
result = pd.merge(data, states, on='BorrowerState')
result.to_csv('LoanAndState.csv')
