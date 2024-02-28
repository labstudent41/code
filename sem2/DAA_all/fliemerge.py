def file_merge(f):
    total=0
    for i in f:
        total+=i
    return total
def sorted_file_merge(f):
    total=0
    f.sort()
    for i in f:
        total=total+i
    return total
files=[80,30,15,90,50]
print("file merge greedy technique")
print("total cost of merging=",file_merge(files))
print("file merge greedy techniques")
print("total cost of mergind=",sorted_file_merge(files))
