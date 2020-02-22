#Mehmet Akif SELBİ

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_sub_sum_recursive(list_1):
    if len(list_1)==0:
        return 0
    if len(list_1)==1:
        return list_1[0]
    n=len(list_1)
    left_i = -1
    left_j = (n//2)-1
    right_i =n//2
    right_j = n

    left_sum = my_sub_sum_recursive(list_1[left_i:left_j])
    right_sum = my_sub_sum_recursive(list_1[right_i:right_j])
    
    t,temp_left_sum = 0,0
    for i in range(left_j,left_i,-1):
        t = t+list_1[i]
        if t>temp_left_sum:
                temp_left_sum = t

    t,temp_right_sum = 0,0
    for i in range(right_i,right_j):
        t = t+list_1[i]
        if t>temp_right_sum:
                temp_right_sum = t

    center_sum = temp_left_sum + temp_right_sum
    
    return  max_of_three(temp_left_sum,temp_right_sum,center_sum)

def my_bubble(list_1):
    for i in range(len(list_1)-1,-1,-1):
        for j in range(i):
            if list_1[j] > list_1[j+1]:
                t=list_1[j+1]
                list_1[j+1] = list_1[j]
                list_1[j] = t
    return list_1

liste = [4,-3,5,-2,-1,2,6,-2]
print(my_sub_sum_recursive(liste))
print(my_bubble(liste))

