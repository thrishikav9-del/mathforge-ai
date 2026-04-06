def generate_code(ir):

    if ir["ir_type"] == "algorithm":

        pattern = ir.get("algorithm_pattern")

        if pattern == "selection_sort":
            return """def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data"""

        if pattern == "bubble_sort":
            return """def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data"""

        if pattern == "binary_search":
            return """def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1"""

        if pattern == "merge_sort":
            return """def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)"""

        if pattern == "recursive":
            return """def recursive_function(n):
    if n <= 1:
        return 1
    return n * recursive_function(n-1)"""

    elif ir["ir_type"] == "numerical":
        return """def newton_raphson(f, df, x):
    return x - f(x)/df(x)"""

    return "# Code generation failed"