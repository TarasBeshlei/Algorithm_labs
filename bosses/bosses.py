

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

def salary(employees_list):
    salary_list = []
    for i in range(len(employees_list)):
        if not employees_list[i]:
            one = 1
            print("Salary" + "(" + str(i) + ") =" + str(one))
            salary_list.append(one)
        else:
            subordinate_salary_count = 0
            for subordinate_salary_count in range(len(employees_list[i])):
                subordinate_salary_count += 1

            print("Salary" + "(" + str(i) + ") =" + str(subordinate_salary_count))
            salary_list.append(subordinate_salary_count)
    print(sum((int(salary_list[j]) for j in range(0, int(len(salary_list))))))

