# 求2+4+6+8+...+100的求和
import numpy as np
sum = 0
for x in np.arange(2,101,2):
	sum = sum + x
print(sum)

