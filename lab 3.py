from Image_Compression.sptl2 import *
from Image_Compression.temporal_sptl2 import *
from Image_Compression.entropy import *
import matplotlib.pyplot as plt

original = plt.imread('me2.jpg')
original = original[:, :, 0]
residual = sptl2(original)

for i in range(1, 8):
   vars()[f'temporal_residual{i}'] = temporal_sptl2(original, i)

# plt.imshow(residual)

entropy_original = entropy(original)
entropy_residual = entropy(residual)

for i in range(1, 8):
   vars()[f'entropy_temporal_residual_{i}'] = entropy(vars()[f'temporal_residual{i}'])

print('Original Entropy: ', entropy_original)


for i in range(1, 8):
    print(f'Case {i}:', vars()[f'entropy_temporal_residual_{i}'])
    plt.imshow(residual)