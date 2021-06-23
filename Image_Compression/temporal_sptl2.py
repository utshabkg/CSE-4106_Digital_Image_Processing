import numpy as np

def temporal_sptl2(D, c):
    const = 5
    [row, col] = np.shape(D)
    pred1 = np.zeros((row+1, col+1))
    pred11 = np.zeros((row+1, col+1))

    pred1[0, :] = const * np.ones((1, col+1))
    pred1[1: row+1, 0] = const
    pred1[1: row+1, 1:col+1] = D
    # pred1[0, :] = const
    # #print(pred1)

    # pred1[1:row, 0] = const
    # #print(pred1)

    # pred1[1:row, 1:col] = D
    # print(pred1)
    # print(pred11)

    if c==1:    #X=B
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i-1][j]
    if c==2:    #X=C
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i-1][j-1]
    if c==3:    #X=A
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i][j-1]
    if c==4:    #X=(A+B)/2
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = 0.5 * (pred1[i][j-1] + pred1[i-1][j])
    if c==5:    #X=A+B-C
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i][j-1] + pred1[i-1][j] - pred1[i-1][j-1]
    if c==6:
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i][j-1] + (0.5 * (pred1[i-1][j] - pred1[i-1][j-1]))
    if c==7:
        for i in range(1, row):
            for j in range(1, col):
                pred11[i][j] = pred1[i-1][j] + (0.5 * (pred1[i][j-1] - pred1[i-1][j-1]))
    
    pred11 = pred11[1:row+1, 1:col+1]
    # print(pred11)
    pred11 = D - np.fix(pred11)
    # print(pred11)
    # pred11 = pred11.astype('double')
    # print(pred11)

    return pred11