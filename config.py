import random
"""
resource_num = random.randint(2, 5)
custumer_num = random.randint(2, 6)
allocation = []
Max = []
for i in range(custumer_num):
    allocation.append(random.sample(range(1, 8), resource_num))
    Max.append(random.sample(range(8, 14), resource_num))

Bank_Avaliable = random.sample(range(2, 7), resource_num)
"""
resource_num = 3
custumer_num = 5
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
Max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
Bank_Avaliable = [3, 3, 2]
# print(resource_num)
# print(custumer_num)
# print(allocation)
# print(Max)
# print(Bank_Avaliable)
