from utils.simplePerceptron import find_net_i
from utils.simplePerceptron import find_error
from utils.simplePerceptron import re_calculate_weight
from utils.simplePerceptron import random_weight

vx = [[1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 1]]

vy = [0, 1, 1, 1]
vw = [1, 0, 0.5]
learn = 0.6

# print(random_weight(15, -0.2, 0.2))
print(random_weight(15, -0.2, 0.2))


# while True:
#     print("-" * 60)
#     count = 0
#     for i in range(len(vx)):
#         print("vw", vw)
#         net_i = find_net_i(vw, vx[i])
#         error = find_error(vy[i], net_i)
#
#         if error != 0:
#             count += 1
#             vw = re_calculate_weight(vw, learn, error, vx[i])
#     if count == 0:
#         break
