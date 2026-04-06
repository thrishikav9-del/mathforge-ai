def generate_ir(semantic_data):

    method_type = semantic_data["method_type"]

    if method_type == "algorithm":
        return {
            "ir_type": "algorithm",
            "algorithm_pattern": semantic_data.get("algorithm_pattern"),
            "control_structure": {
                "loop": semantic_data.get("has_loop"),
                "recursion": semantic_data.get("has_recursion")
            },
            "data_structure": "array",
            "properties": {"deterministic": True}
        }

    elif method_type == "numerical":
        return {
            "ir_type": "numerical",
            "iteration": semantic_data.get("has_convergence"),
            "math_model": "iterative_update",
            "requires_derivative": True,
            "properties": {"convergence_required": True}
        }

    return {"ir_type": "unknown"}