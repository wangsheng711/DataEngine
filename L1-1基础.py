# 求2+4+6+8+...+100的求和，方法1
sum = 0
number = 2
while number < 101:
    sum = sum + number
    number = number + 2
print(sum)

# 求2+4+6+8+...+100的求和，方法2
import numpy as np
sum = 0
for x in np.arange(2,101,2):
	sum = sum + x
print(sum)
