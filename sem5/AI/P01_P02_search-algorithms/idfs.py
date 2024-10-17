from RMP import dict_gn

start = "Arad"
target = "Bucharest"
traversal = []

def recursive_DLS(city, level, limit):
    traversal.append(city)
    if city == target:
        return True
    if level == limit:
        return False
    for neighbor in dict_gn[city]:
        if neighbor not in traversal:
            if recursive_DLS(neighbor, level+1, limit):
                return True

for i in range(9):
    if recursive_DLS(start, 0, i):
        break
    traversal = []

print("IDDFS traversal from %s to %s :-" %(start, target))
print(' -> '.join(traversal))
