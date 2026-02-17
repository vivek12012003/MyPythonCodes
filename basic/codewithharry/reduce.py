
from functools import reduce


l = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y , l)
print(sum)



#works
# l = [1,2,3,4,5]
# l = [3,3,4,5]
# l = [6,4,5]
# l = [10,5]
# l = [15]
