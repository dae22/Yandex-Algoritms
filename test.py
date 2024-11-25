from collections import defaultdict


# Функция для выполнения поиска в глубину (DFS)
def dfs(node, graph, dp):
    # Если вершина уже посещалась и для неё подсчитаны сортировки, возвращаем результат
    if dp[node] != -1:
        return dp[node]

    # Если текущая вершина - лист, то у неё только одна возможная сортировка
    if not graph[node]:
        dp[node] = 1
        return 1

    # Иначе суммируем количество сортировок для всех потомков
    total_sorts = 1
    for child in graph[node]:
        total_sorts *= dfs(child, graph, dp)

    # Сохраняем результат для текущей вершины
    dp[node] = total_sorts
    return total_sorts


# Основная функция для расчёта количества топологических сортировок
def count_topological_sortings(n, edges):
    # Создаём граф в виде словаря смежностей
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])

    # Массив для хранения количества сортировок для каждой вершины
    dp = [-1] * n

    # Запускаем DFS с корневой вершины (предполагаем, что это вершина 0)
    root = 0
    return dfs(root, graph, dp)


# Тестируем на примере
if __name__ == "__main__":
    n = 4
    edges = [(2, 3), (3, 1), (2, 4)]  # Переименуем вершины так, чтобы индексация начиналась с нуля
    print(count_topological_sortings(n, edges))