from RMP import dict_gn

start = "Arad"
goal = "Bucharest"
result = ""

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    print("===== DLS(%s, %s, %s, %s)" % (city, visitedstack, startlimit, endlimit))
    found = False
    result = result + " " + city
    visitedstack.append(city)
    if city == goal:
        print("Found", goal, "in DLS")
        return True
    if startlimit == endlimit:
        print("\t %s: Reached upper bound" % (city))
        return False
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found = DLS(eachcity, visitedstack, startlimit+1, endlimit)
        else:
            print("\t %s: %s already visited" % (city, eachcity))
        if found:
            return found

def IDDFS(city, visitedstack, endlimit):
    global result
    for i in range(0, endlimit):
        print("\n\nSearching at limit:", i)
        found = DLS(city, visitedstack, 0, i)
        if found:
            print("Found!")
            break
        else:
            print("Not found!")
            print(result)
            result = ""
            visitedstack = []

visitedstack = []
IDDFS(start, visitedstack, 9)
print("\nIDDFS Traversal from", start, "to", goal, "is :-\n", result)
