# unfinished

from queue import PriorityQueue
from RMP import dict_gn
from RMP import dict_hn

start = "Arad"
target = "Bucharest"
traversal = []

def get_fn(traversal):
    print("\nget_fn(%s)" %(traversal))
    gn = 0
    for i in range(len(traversal) - 1):
        gn += dict_gn[traversal[i]][traversal[i+1]]
    hn = dict_hn[traversal[-1]]
    print("g(n) = %s, h(n) = %s" %(gn, hn))
    return gn + hn

cityq = PriorityQueue()
cityq.put((get_fn(traversal + [start]), start, start))

while not cityq.empty():
    cityget = cityq.get()
    print("\n->", cityget)
    city = cityget[2]
    print("City Queue:", cityq.queue)
    traversal.append(city)
    if city == target:
        break
    for neighbor in dict_gn[city]:
        if neighbor not in cityq.queue and neighbor not in traversal:
            fn = get_fn(traversal + [neighbor])
            print(fn, city, neighbor)
            cityq.put((fn, city, neighbor))

print(traversal)
