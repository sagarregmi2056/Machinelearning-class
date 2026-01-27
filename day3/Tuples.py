import types


tuplesexample=(1,2,3,4,5,6)

print(tuplesexample)

convertedtolist= list(tuplesexample)

convertedtolist.append(9)

finalcreatedtuples= tuple(convertedtolist)


print(finalcreatedtuples)


print(tuplesexample[::-1])


# note the tuples can be modified only with the help by converting tuples into list by using =list(variableneedtobechanged)and again adding modifying then again converting back to tuples





checking_variable = [1]
checking_tuples=(1,)

print(type(checking_variable))
print(type(checking_tuples))




# very imp

# nested tuples
t=([1,2],[2,4],[3,5])





t[0].insert(1,100)

# output  ([1, 100, 2], [2, 4], [3, 5])
print(t)


# veryimp


# packing and unpacking approach

p=(1,2,3,4)

print(p)


# here the provided value must be same for destrucring 
f,g,h,i=p
print(f,g,h,i)
print(type(f))

