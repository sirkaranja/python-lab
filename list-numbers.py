#Given a list of numbers, find the 
    #largest, 
    # smallest, and
    # second-largest

num =[2,54,67,32,90,100,100]
def list_numbers(num):
    #set removes duplicate values in the list
    num2 = list(set(num))
    #check the length of the new list
    length= len(num2)
    #arrange the values from smallest to largest
    num2.sort()
    print("the largest is", num2[length-1])
    print("the second largest is:", num2[length-2])
    print("the smallest is", num2[0])
    print("the second smallest",num2[1])

list_numbers(num)


