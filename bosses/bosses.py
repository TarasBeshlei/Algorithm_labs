sorted_graph = dict()
time_graph = dict()
workers_salary = dict()
some_set = set()
time_dict = dict()
list_for_keys = []
salary_list = []

def data_from_file(name_of_file):
    file = open(name_of_file, 'r')
    data_of_file = file.read()
    file.close()
    return data_of_file

def list_of_vertex(in_data):
    vertex_list = []
    for i in range(len(in_data.split(' ')[0])):
        vertex_list.append(i)
    return vertex_list

def index_of_subordinates(in_data):
    subordinates_list = []
    for line in in_data.split(' '):
        meneger_subordinates = []
        for i in range(len(line)):
            if (line[i] == 'Y'):
                meneger_subordinates.append(i)
        if not subordinates_list:
            subordinates_list.append(meneger_subordinates)
        else:
            subordinates_list.append(meneger_subordinates)


    return subordinates_list


def graph(vertex_list, subordinates):
    graph = dict()
    for i in range(len(vertex_list)):
        graph[vertex_list[i]] = subordinates[i]

    return graph

def select_menegers(employees_list):
    for i in range(len(employees_list)):
        if not employees_list[i]:
            print(str(i) + " not a manager ")
        else:
            for subordinates_emloyeer in employees_list[i]:
                print(str(i) + " manager for " + str(subordinates_emloyeer))


def salary(graph):
    sorting_dict(graph)
    print(sorted_graph)
    print(sum((int(sorted_graph[j]) for j in range(0, int(len(sorted_graph))))))



def sorting_dict(graph):
    for i in graph.keys():
        time_graph[i] = len(graph[i])
        some_set.add(len(graph[i]))
    for j in some_set:
        for k in graph.keys():
            if (len(graph[k]) == j):
                sorted_graph[k] = graph[k]
    return sorted_graph

def salary(sorted_graph):
    for n in sorted_graph.keys():
        if (len(sorted_graph[n]) == 0):
            workers_salary[n] = 1
        for m in sorted_graph.keys():
            for b in sorted_graph[m]:
                if b == n:
                    time_dict[m] = workers_salary[n]
                    if m in workers_salary.keys():
                        workers_salary[m] = time_dict[m] + workers_salary[m]
                    else:
                        workers_salary.update(time_dict)
                    time_dict.clear()
                    
    for b in workers_salary.keys():
            salary_list.append(workers_salary[b])

    print(sum((int(salary_list[j]) for j in range(0, int(len(salary_list))))))
