from bosses import data_from_file, index_of_subordinates, graph, select_menegers, salary, list_of_vertex

if __name__ == '__main__':
    data_of_matrix = data_from_file("in")
    list_of_vertex1 = list_of_vertex(data_of_matrix)
    index = index_of_subordinates(data_of_matrix)
    employeers = graph(list_of_vertex1, index)
    select_menegers(employeers)
    salary(employeers)