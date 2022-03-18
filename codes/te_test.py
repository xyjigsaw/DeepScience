# Name: te_test
# Author: Reacubeth
# Time: 2021/6/14 15:40
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from copent import transent
from pandas import read_csv
import json
import numpy as np
from file_walker import traverse

'''
# network_dl_pr.json
main_node_id = [52, 47, 91, 13, 19, 107, 110, 159, 275, 2]
main_node_name = ["Medicine", "Biology", "Chemistry", "Psychology", "Economics", "Sociology", "Geography", "Business", "Philosophy", "Computer Science"]
'''

# network_cov_pr.json
main_node_id = [0, 22, 54, 49, 20, 96, 14, 9, 58, 19]
main_node_name = ["Medicine", "Biology", "Chemistry", "Psychology", "Economics", "Sociology", "Geography", "Business", "Philosophy", "Computer Science"]

res_json = {}

pr_val = np.load('STGCNtest/pr_real_val_cov.npy')
x_name = 'Medicine'
base = 'DLcovid/tKG/new/COVID/main'
f_name = 'pr_te_cov2other.json'
csv_files = traverse(base, 'csv', False)
csv_files = [i.replace('.csv', '') for i in sorted(csv_files)]
print(pr_val.shape)     # 370 time steps * 311 nodes

for y_name in main_node_name:
    res_json[y_name] = {}

    data = pr_val[:, [main_node_id[main_node_name.index(y_name)],
                      main_node_id[main_node_name.index(x_name)]]]  # where X is cause of Y
    cause = []
    time_step = []
    for lag in range(pr_val.shape[0]):
        try:
            cause.append(transent(data[:, 0], data[:, 1], lag) - transent(data[:, 1], data[:, 0], lag))
            time_step.append(csv_files[lag])
            print("TE from %s to %s at %s days lag : %f" % (x_name, y_name, csv_files[lag], cause[-1]))
        except Exception as e:
            print(e)
            cause.append(0)
            time_step.append(csv_files[lag])
    res_json[y_name]['value'] = cause
    res_json[y_name]['time_step'] = time_step

with open(f_name, 'w') as f:
    json.dump(res_json, f)
