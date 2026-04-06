def validate_ir(ir):

    if "ir_type" not in ir:
        return False, "IR missing ir_type"

    if ir["ir_type"] == "unknown":
        return False, "Unknown method type"

    return True, "IR valid"