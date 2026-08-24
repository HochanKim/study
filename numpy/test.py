import numpy as np

a = np.array([82.0, 91.5, 78.2])
# (a - a.min()) / (a.max() - a.min())
print((a - a.min()) / (a.max() - a.min()))