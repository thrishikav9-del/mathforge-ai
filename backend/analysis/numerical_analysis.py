def analyze_numerical_properties(ir):

    if ir["ir_type"] != "numerical":
        return None

    return {
        "convergence_order": "Quadratic",
        "order_formula": "e_{n+1} ≈ C * e_n^2",
        "local_convergence": True,
        "stability": "Conditionally stable",
        "requirements": [
            "Function must be differentiable",
            "Derivative should not be zero"
        ],
        "failure_cases": [
            "Poor initial guess",
            "Derivative near zero"
        ]
    }