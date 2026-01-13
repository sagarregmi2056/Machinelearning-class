listexample=[1,2,3,4,5]


# this shows list support multiple values
listname=["sagar","saugat","angat","kritish"]

# print("the first value of index of the list is",listexample[0])
# print("second is ",listexample[2])
# print("second is ",listexample[3])
# print("second is ",listexample[4])
# print("second is ",listexample[1])

# yaslya chai out of range wala error falxa kina ki list ma index 6 ma kai pani xaina soo
# print("second is ",listexample[6])

# check the length of the given array/list



# last element vanyako length(array )-1 ho why? kina ki len() function ley jailai pani array ko length kati ota xa count garxa empty vaya 0 1ta vaya 1 like that 5 ota xa soo 5
print(len(listexample)-1)

# yaslya chai last index ma kun element xa dinxa

print(listexample[len(listexample)-1])

print(listname[1])
print(listname[len(listname)-1])

# add element in the last of the list 
listname.append("puxxar")
print(listname)

# remove function ley chai k delete garni value dida hunxa like a b c d e f g h
listname.remove("sagar")
print(listname)



# yaslya chai error throw garxa yadi list ma xaina vanya directly not in the list wala error
# listname.remove("1")


listname.append("puxxar ko puxxar")
print(listname)


# list lai utalidinxa reverse gardinxa

listname.reverse()

print(listname)

# negative value means last bata start garxa -1 =last -2 = second last
print(listname[-1])


listname.sort()

print(listname)



# loop in list

for i in listname:
    print("the values of the list are",i ,"and index is",[i])