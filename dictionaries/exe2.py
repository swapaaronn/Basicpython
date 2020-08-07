# world count

def  world_count(l):
    count={}
    for i in l:
        count[i]=l.count(i)
        return count

print(world_count("swapnil"))