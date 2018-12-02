couples = dict()
passed = []
list_of_tribes=[]
result=[]
number_of_possible_pairs=0

def addDictList(values):
    couples.setdefault(int(values[0]), [])
    if int(values[0]) in couples.keys():
        couples[int(values[0])].append(int(values[1]))
    else:
        couples[int(values[0])] = int(values[1])

with open ('Text') as Text :
    for line in Text:
        values = line.split(",")
        addDictList(values)

def orientedGraph():
    couples_copy=couples.copy()
    for i in couples.values():
        for j in i:
            couples_copy.setdefault(j,[])
    for i in couples_copy.keys():
        for j in couples.keys():
            if i in couples_copy[j]:
                couples_copy.setdefault(i,[])
                couples_copy[i].append(j)
    return couples_copy

copy_list = orientedGraph().copy()

def tribe():
    dfs(copy_list, min(copy_list.keys()))
    passed_copy=passed.copy()
    list_of_tribes.append(passed_copy)
    for d in passed :
        del copy_list[d]
    passed.clear()
    if len(copy_list.keys()) == 0 :
        return list_of_tribes
    else:
        tribe()

def dfs(graph,node):
    global passed
    if node not in passed:
        passed.append(node)
        for n in graph[node]:
            dfs(graph,n)

tribe()

list_of_tribes_copy = list_of_tribes.copy()
list_of_tribes_copy.pop(0)
list_of_tribes.pop(len(list_of_tribes) - 1)
for h in list_of_tribes:
    for p in list_of_tribes_copy:
        for i in h:
            for j in p:
                if (i+j)%2==1:
                    result.append(str(i)+"/"+str(j))
                    number_of_possible_pairs+=1

print(number_of_possible_pairs,result)
