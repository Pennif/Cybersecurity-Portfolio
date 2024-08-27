
# %%
# This code is to test the speed of a printing while loop. It is used to help understand buffer limits on websservers; it will
# help in the devolpment of fuzzers in the future

import time
import math
import matplotlib.pyplot as plt

final_message = []
max_a_count = []
count_takes = []
timeout_size = []
it_count = 0
it_list= []
while it_count <= 10:
    timeout = time.time() + 0.02* (1+ it_count)
    timeout_size.append(timeout)
    count = 0
    while True:
        if time.time() > timeout:
            max_a_count.append(len(print_message))
            count_takes.append(count)
            break
        count += 1
        print_message = "A" * count
        print(count, print_message)
    it_count += 1 
    print(it_count)
for i in range(it_count):
    new_tuple = (0.02*(i+1) ,max_a_count[i])
    it_list.append(0.02*i)
    final_message.append(new_tuple)

plt.plot(it_list,max_a_count)
plt.show()
print(final_message)



# %%
