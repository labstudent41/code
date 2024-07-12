import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = "Arad"
goal = "Bucharest"
result = ""

def get_fn(citystr):
    cities = citystr.split(" -> ")
    hn = gn = 0
    for i in range(len(cities) - 1):
        gn += dict_gn[cities[i]][cities[i+1]]
    hn = dict_hn[cities[len(cities) - 1]]
    print("%-60s %6s %6s %6s" % (cities, gn, hn, gn+hn))
    return hn + gn

def expand(cityq):
    global result
    total, citystr, thiscity = cityq.get()
    print("\nChoosen Path:  %s   (cost=%s)" % (citystr, total))
    print(cityq)
    if thiscity == goal:
        result = citystr + " : " + str(total)
        return
    print()
    for neighbour in dict_gn[thiscity]:
        route = citystr + " -> " + neighbour
        cityq.put((get_fn(route), route, neighbour))
    expand(cityq)

if __name__ == "__main__":
    print("fn() = gn() + hn()\n")
    print("-" * 82)
    print("%-60s %6s %6s %6s" % ("City Route", "gn()", "hn()", "fn()"))
    print("-" * 82)
    cityq = Q.PriorityQueue()
    cityq.put((get_fn(start), start, start))
    expand(cityq)
    print("-" * 82)
    print("The A* path with the total is: ")
    print(result)

