import numpy as np

def one(n):
  x = 3 * (np.random.rand(n, 2) - 0.5)
  r = x[:, 1]**2 + x[:, 2]**2
  y = (radius > 0.7 + 0.1 * np.random.randn(n, 1)) & (radius < 2.2 + 0.1 * np.random.randn(n, 1))
  y = 2 * y - 1

def four(n):
  x = 3 * (np.random.rand(n, 4) - 0.5)
  y = ( 2 * x[:, 1] - x[:, 2] + 0.5 + 0.5 * np.random.rand(n) ) > 0
  y = 2 * y - 1
  return x, y

def five(n):
  x = 3 * (np.random.rand(n, 4) - 0.5)
  w = np.array([[2, -1, 0.5], [-3, 2, 1], [1, 2, 3]])
  y = np.amax(np.matmul(np.concatenate([x[:, 1:3], np.ones((n, 1))], 1), w.T) + 0.5 * np.random.randn(n, 3), 1)
  return x, y