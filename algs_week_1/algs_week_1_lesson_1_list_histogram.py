
import random

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

my_list = get_n_random_numbers(10,-8,8)
sorted(my_list)
my_f=my_frequency_with_dict(my_list)
print(my_list)
print(my_f)


def my_frequency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)
print(result_1,result_2)


