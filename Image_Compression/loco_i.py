import numpy as np
import pandas as pd

def loco_i(D):
    const = 50
    row = D
    col = D
    pred1 = np.zeros((D, D))
    pred11 = np.zeros((D, D))

    pred1[0, :] = const
    #print(pred1)

    pred1[1:row, 0] = const
    #print(pred1)

    pred1[1:row, 1:col] = D
    print(pred1)
    print(pred11)

    for i in range(1, row):
        for j in range(1, col):
            if pred1[i-1][j-1] >= max(pred1[i][j-1], pred1[i-1][j]):
                pred11[i][j] = min(pred1[i][j-1], pred1[i-1][j])
            elif pred1[i-1][j-1] <= min(pred1[i][j-1], pred1[i-1][j]):
                pred11[i][j] = max(pred1[i][j-1], pred1[i-1][j])      
            else:
                pred11[i][j] = pred1[i][j-1] + pred1[i-1][j] - pred1[i-1][j-1]            

    pred11 = pred11[1:row, 1:col]
    print(pred11)
    pred11 = pred11.astype('int64')
    print(pred11)
    pred11 = pred11.astype('double')
    print(pred11)