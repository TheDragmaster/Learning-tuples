import sys 
import timeit

my_list = [0, 1, 2, "hello", True] #List
my_tuple = (0, 1, 2, "hello", True) #Tuple
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) #List
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) #Tuple, also computes more efficiently 