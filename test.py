#!/user/bin/env python3

import numpy as np

# i = 0
# while i <5 :
#     test_uniform = np.random.uniform(0, 1)
#     print(test_uniform)
#     i += 1



state = np.zeros((3, 3))
print(state,'  --------  type:',type(state))
map = map(tuple, state)
print(map,'  --------  type:',type(map))
state_tuple = tuple(map)
print(state_tuple,'  --------  type:',type(state_tuple))

