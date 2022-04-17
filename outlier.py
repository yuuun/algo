# hello 
import numpy as np
from collections import Counter
def detect_outlier(data, n, columns):
    row_index = []
    for col in columns:
        q1 = np.percentile(data[col], 25)
        q3 = np.percentile(data[col], 75)
        iqr = (q3 - q1)
        outlier_step = iqr * 1.5

        tmp = data[(data[col] < q1 - outlier_step) | (data[col] > q3 + outlier_step)].index
        row_index += tmp
    cnt_row = Counter(row_index)
    return list(k for k, v in cnt_row.items() if v > 1)
