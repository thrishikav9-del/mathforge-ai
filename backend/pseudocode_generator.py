def generate_pseudocode(ir):

    if ir["ir_type"] == "algorithm":

        pattern = ir.get("algorithm_pattern")

        if pattern == "selection_sort":
            return """FOR i ← 1 to n DO
    min_index ← i
    FOR j ← i+1 to n DO
        IF A[j] < A[min_index] THEN
            min_index ← j
        END IF
    END FOR
    SWAP A[i] and A[min_index]
END FOR"""

        if pattern == "bubble_sort":
            return """FOR i ← 1 to n DO
    FOR j ← 1 to n-i DO
        IF A[j] > A[j+1] THEN
            SWAP A[j] and A[j+1]
        END IF
    END FOR
END FOR"""

        if pattern == "binary_search":
            return """SET left ← 0, right ← n-1
WHILE left ≤ right DO
    mid ← (left + right) / 2
    IF A[mid] = target THEN
        RETURN mid
    ELSE IF A[mid] < target THEN
        left ← mid + 1
    ELSE
        right ← mid - 1
END WHILE
RETURN -1"""

        if pattern == "merge_sort":
            return """IF length(A) ≤ 1 THEN
    RETURN A
DIVIDE A into left and right halves
left ← MERGE_SORT(left)
right ← MERGE_SORT(right)
RETURN MERGE(left, right)"""

        if pattern == "recursive":
            return "Recursive function definition calling itself"

    elif ir["ir_type"] == "numerical":
        return """x_next ← x − f(x) / f′(x)
REPEAT until convergence"""

    return "Pseudocode cannot be generated"