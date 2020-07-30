user_info={"name":"swapnil",
"age":25,
"college":"imcost",
"favorate":["swapnil",25,"imcot"],
"movie":{"movie":"coco"}
}

# how to add data
user_info["song"]=["mauli mauli"]
print(user_info)

# delete data use in pop()method  or popitem() 
# pop method we have to assign atlest one input
# popitem we don't want to assign any input
# random delete last item in dictionaries

user_item=user_info.pop("favorate")#----------->pop()
print(type(user_item))
print(user_item)


print(user_info.popitem())#----------->popitem()
print(user_info)
