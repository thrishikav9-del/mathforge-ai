def analyze_time_complexity(ir):

    if ir["ir_type"] == "algorithm":

        pattern = ir.get("algorithm_pattern")

        if pattern in ["selection_sort", "bubble_sort"]:
            return "O(n^2)"

        if pattern == "binary_search":
            return "O(log n)"

        if pattern == "merge_sort":
            return "O(n log n)"

        if pattern == "recursive":
            return "Depends on recurrence"

        return "Unknown"

    elif ir["ir_type"] == "numerical":
        return "O(k * C)"

    return "Unknown"