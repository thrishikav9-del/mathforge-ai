def analyze_space_complexity(ir):

    if ir["ir_type"] == "algorithm":

        pattern = ir.get("algorithm_pattern")

        if pattern == "merge_sort":
            return "O(n)"

        return "O(1)"

    elif ir["ir_type"] == "numerical":
        return "O(1)"

    return "Unknown"