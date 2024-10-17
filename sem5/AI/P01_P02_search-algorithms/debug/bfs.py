from queue import Queue
from RMP import dict_gn

print("ln(dict_gn) = ", len(dict_gn))

start = "Arad"
goal = "Bucharest"
result = ""

def BFS(city, cityq, visited):
    print("\n===== BFS(%s, %s, %s)" % (city, list(cityq.queue), visited))
    global result
    if city == start:
        result = result + " " + city
    for eachcity in dict_gn[city].keys():
        if eachcity == goal:
            print("\t>>> Found", goal)
            result = result + " " + eachcity
            return
        if eachcity not in cityq.queue and eachcity not in visited:
            print("\t\"%s\" added to cityq" % (eachcity))
            cityq.put(eachcity)
            result = result + " " + eachcity
            visited.add(city)
        else:
            print("\t%s already visited" % (eachcity))
    BFS(cityq.get(), cityq, visited)

cityq = Queue()
visited = set()
BFS(start, cityq, visited)
print("\nBFS traversal from", start, "to", goal, "is :-\n", result)

