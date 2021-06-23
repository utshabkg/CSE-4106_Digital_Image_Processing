import numpy as np

def entropy(img):
    m = np.histogram(np.ravel(img), bins = 256)[0]/img.size
    m = list(filter(lambda p: p>0, np.ravel(m)))
    ent = -np.sum(np.multiply(m, np.log2(m)))
    return ent

