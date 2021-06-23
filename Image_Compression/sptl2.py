import numpy as np

def sptl2(D):
    const = 5
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

    #X = (A+B)/2
    for i in range(1, row):
        for j in range(1, col):
            pred11[i][j] = 0.5 * (pred1[i][j-1] + pred1[i-1][j])
    
    pred11 = pred11[1:row, 1:col]
    print(pred11)
    pred11 = D - np.fix(pred11)
    print(pred11)
    pred11 = pred11.astype('double')
    print(pred11)