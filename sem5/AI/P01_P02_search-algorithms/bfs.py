from RMP import dict_gn

start = "Arad"
target = "Bucharest"
queue = [start]
traversal = [start]

if start != target:
    while queue:
        city = queue.pop(0)
        for neighbor in dict_gn[city]:
            if neighbor not in queue and neighbor not in traversal:
                queue.append(neighbor)
                traversal.append(neighbor)
            if neighbor == target:
                queue = []

print("BFS Traversal from %s to %s:-" %(start, target))
print(' -> '.join(traversal))

