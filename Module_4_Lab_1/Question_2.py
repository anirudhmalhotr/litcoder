import sys
def perform_operations(array_size, queries):
    # Initialize the array with zeros
    array = [0] * array_size

    # Perform each operation
    for query in queries:
        start_index, end_index, value = query
        for i in range(start_index - 1, end_index):
            array[i] += value

    max_value = max(array)
    return max_value


"""Main"""
array_size_1 = int(input())
query_count_1 = int(input())
queries_1 = []

for _ in range(query_count_1):
    query = list(map(int, input().split()))
    queries_1.append(query)

output_1 = perform_operations(array_size_1, queries_1)
print(output_1)
                                                                                                                            