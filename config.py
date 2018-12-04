import random
import time

random.seed(time)
resource_num = random.randint(2, 5)
custumer_num = random.randint(2, 6)
allocation = []
Max = []
name_data = ['Anna', 'Zoe', 'Tina', 'Joe', 'Peter', 'Mia', 'Bob', 'Andy', 'Nick', 'Dylan', 'Rachel', 'Sally', 'Bella', 'Lisa', 'Jenny', 'Wendy', 'Joseph', 'Robert', 'Tom', 'Amy', 'Justin', 'Jessica', 'Sunny', 'Raina', 'Daniel']

cus_name = random.sample(name_data, custumer_num)

for i in range(custumer_num):
    #allocation.append(random.sample(range(0, 4), resource_num))
    #Max.append(random.sample(range(5, 10), resource_num))
    allocation.append([])
    Max.append([])

    for j in range(resource_num):
        tmp = random.randint(0, 4)
        allocation[i].append(tmp)

        #if (tmp < 4):
        Max[i].append(random.randint(tmp, tmp+5))
        #else:
            #Max[i].append(random.randint(tmp, 9))


Bank_Avaliable = random.sample(range(1, 7), resource_num)
