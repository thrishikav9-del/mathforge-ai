def compute_accuracy(correct, total):
    """
    Generic accuracy calculator
    """
    if total == 0:
        return 0.0
    return (correct / total) * 100


def evaluate_complexity(predicted, expected):
    """
    Returns 1 if correct else 0
    """
    return 1 if predicted == expected else 0


def evaluate_convergence(predicted, expected):
    """
    Compare convergence classification
    """
    return 1 if predicted == expected else 0


def calculate_pattern_accuracy(results):
    """
    Calculate accuracy per algorithm pattern
    """
    pattern_stats = {}
    for result in results:
        pattern = result.get("expected_pattern")
        if pattern:
            if pattern not in pattern_stats:
                pattern_stats[pattern] = {"correct": 0, "total": 0}
            pattern_stats[pattern]["total"] += 1
            if result.get("pattern_match", False):
                pattern_stats[pattern]["correct"] += 1
    
    return pattern_stats