import sys
sys.path.append("./messages")

# from messages.testing_data_pb2 import TestingData
from messages.algorithm_pb2 import Algorithm

# x = TestingData()
x = Algorithm()
x.moving_average.lots.value = float(10)

print(x)
