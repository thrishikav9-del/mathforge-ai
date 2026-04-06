def analyze_semantics(preprocessed_data, original_text=None):

    verbs = set(preprocessed_data.get("verbs", []))
    nouns = set(preprocessed_data.get("nouns", []))
    adverbs = set(preprocessed_data.get("adverbs", []))
    adjectives = set(preprocessed_data.get("adjectives", []))

    all_words = verbs.union(nouns).union(adverbs).union(adjectives)
    all_words = {word.lower() for word in all_words}

    # Raw text fallback
    if original_text:
        raw_words = set(original_text.lower().split())
    else:
        raw_words = set()

    combined_words = all_words.union(raw_words)

    method_type = "unknown"
    algorithm_pattern = None
    matched_keywords = []

    bubble_keywords = {"bubble", "adjacent"}
    selection_keywords = {"select", "minimum", "small"}
    selection_action_keywords = {"swap"}
    binary_keywords = {"search", "middle"}
    merge_keywords = {"divide", "merge", "half", "halves"}
    recursion_keywords = {"recursive", "recursion"}
    numerical_keywords = {"root", "derivative", "approximate", "converge", "iteration"}

    has_loop = False
    has_recursion = False
    has_convergence = False

    numerical_matches = combined_words.intersection(numerical_keywords)
    bubble_matches = combined_words.intersection(bubble_keywords)
    selection_matches = combined_words.intersection(selection_keywords)
    selection_action_matches = combined_words.intersection(selection_action_keywords)
    binary_matches = combined_words.intersection(binary_keywords)
    merge_matches = combined_words.intersection(merge_keywords)
    recursion_matches = combined_words.intersection(recursion_keywords)

    if numerical_matches and (
        bubble_matches or selection_matches or binary_matches or merge_matches or recursion_matches
    ):
        method_type = "ambiguous"
        matched_keywords = list(numerical_matches)

    elif numerical_matches:
        method_type = "numerical"
        has_convergence = True
        matched_keywords = list(numerical_matches)

    elif merge_matches:
        method_type = "algorithm"
        algorithm_pattern = "merge_sort"
        has_recursion = True
        matched_keywords = list(merge_matches)

    elif recursion_matches:
        method_type = "algorithm"
        algorithm_pattern = "recursive"
        has_recursion = True
        matched_keywords = list(recursion_matches)

    elif binary_matches:
        method_type = "algorithm"
        algorithm_pattern = "binary_search"
        has_loop = True
        matched_keywords = list(binary_matches)

    elif selection_matches or (selection_action_matches and selection_matches):
        method_type = "algorithm"
        algorithm_pattern = "selection_sort"
        has_loop = True
        matched_keywords = list(selection_matches.union(selection_action_matches))

    elif bubble_matches:
        method_type = "algorithm"
        algorithm_pattern = "bubble_sort"
        has_loop = True
        matched_keywords = list(bubble_matches)

    confidence_score = round(len(matched_keywords) / max(len(combined_words), 1), 2)

    explanation = (
        f"Detected {method_type}"
        + (f" ({algorithm_pattern})" if algorithm_pattern else "")
        + f" due to keywords: {matched_keywords}"
    )

    return {
        "method_type": method_type,
        "algorithm_pattern": algorithm_pattern,
        "has_loop": has_loop,
        "has_recursion": has_recursion,
        "has_convergence": has_convergence,
        "confidence_score": confidence_score,
        "explanation": explanation
    }