from graphviz import Graph
import time

def read_file(filename):
    adjacency_matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            adjacency_matrix.append(row)
    return adjacency_matrix

def visualize_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    dot = Graph()
    # Добавление вершин графа
    for i in range(num_vertices):
        dot.node(str(i))
    # Добавление ребер графа
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            weight = adjacency_matrix[i][j]
            if weight > 0:
                dot.edge(str(i), str(j), label=str(weight))
    # Вывод графа в формате PNG
    dot.render('vualya', view=True)

def find_edges(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    min_degree = min(sum(row) for row in adjacency_matrix)
    edges = []
    for i in range(num_vertices):
        if sum(adjacency_matrix[i]) == min_degree:
            for j in range(num_vertices):
                if adjacency_matrix[i][j] > 0:
                    edges.append((i, j))
    return edges

def connection(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    max_edges = (num_vertices - 1) * (num_vertices - 2) // 2
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2
    return num_edges >= max_edges

def main():
    filename = input("Введите имя файла с матрицей смежности: ")
    adjacency_matrix = read_file(filename)

    start_time = time.time()  # Запуск отсчета времени

    #visualize_graph(adjacency_matrix)

    #if connection(adjacency_matrix):
        #print("Граф связан")
    #else:
        #print("Граф не связан")

    edges = find_edges(adjacency_matrix)
    print("Ребра, смежные к вершинам с минимальной степенью:")
    for edge in edges:
        print(edge)

    end_time = time.time()  # Остановка отсчета времени
    elapsed_time = end_time - start_time
    print("Время работы программы: {:.8f} сек".format(elapsed_time))

if __name__ == '__main__':
    main()
