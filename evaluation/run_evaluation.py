import json
from backend.preprocess import preprocess_text
from backend.semantic_analyzer import analyze_semantics
from backend.ir_generator import generate_ir
from backend.analysis.time_complexity import analyze_time_complexity
from backend.analysis.space_complexity import analyze_space_complexity

def run_evaluation():
    try:
        with open("data/dataset.json") as f:
            dataset = json.load(f)
    except FileNotFoundError:
        # Try alternative path
        with open("../data/dataset.json") as f:
            dataset = json.load(f)

    total = len(dataset)
    print(f"\n🚀 Running evaluation on {total} test cases...\n")

    pattern_correct = 0
    time_correct = 0
    space_correct = 0
    type_correct = 0
    
    mismatches = []

    for i, item in enumerate(dataset, 1):
        text = item["input"]
        print(f"🔄 Testing {i}/{total}: {text[:50]}...")

        pre = preprocess_text(text)
        sem = analyze_semantics(pre, text)
        ir = generate_ir(sem)

        predicted_type = sem["method_type"]
        predicted_pattern = sem.get("algorithm_pattern")
        predicted_time = analyze_time_complexity(ir)
        predicted_space = analyze_space_complexity(ir)

        # Type check
        if predicted_type == item["expected_type"]:
            type_correct += 1
        else:
            mismatch = {
                "input": text,
                "type": {"expected": item["expected_type"], "predicted": predicted_type}
            }
            mismatches.append(mismatch)
            print(f"   ❌ Type mismatch: expected {item['expected_type']}, got {predicted_type}")

        # Pattern check (handle None values)
        expected_pattern = item.get("expected_pattern")
        if predicted_pattern == expected_pattern or (expected_pattern is None and predicted_pattern is None):
            pattern_correct += 1
        else:
            if "pattern" not in mismatches[-1] if mismatches else {}:
                mismatches[-1]["pattern"] = {"expected": expected_pattern, "predicted": predicted_pattern}
            print(f"   ❌ Pattern mismatch: expected {expected_pattern}, got {predicted_pattern}")

        # Time complexity check
        if predicted_time == item["expected_time"]:
            time_correct += 1
        else:
            if "time" not in mismatches[-1] if mismatches else {}:
                mismatches[-1]["time"] = {"expected": item["expected_time"], "predicted": predicted_time}
            print(f"   ❌ Time mismatch: expected {item['expected_time']}, got {predicted_time}")

        # Space complexity check
        if predicted_space == item["expected_space"]:
            space_correct += 1
        else:
            if "space" not in mismatches[-1] if mismatches else {}:
                mismatches[-1]["space"] = {"expected": item["expected_space"], "predicted": predicted_space}
            print(f"   ❌ Space mismatch: expected {item['expected_space']}, got {predicted_space}")
        
        if predicted_type == item["expected_type"] and \
           (predicted_pattern == item.get("expected_pattern") or (item.get("expected_pattern") is None and predicted_pattern is None)) and \
           predicted_time == item["expected_time"] and \
           predicted_space == item["expected_space"]:
            print("   ✅ All correct")

    print("\n" + "="*50)
    print("📊 MathForge Evaluation Results")
    print("="*50)
    print(f"✅ Type Accuracy: {(type_correct/total)*100:.2f}% ({type_correct}/{total})")
    print(f"✅ Pattern Accuracy: {(pattern_correct/total)*100:.2f}% ({pattern_correct}/{total})")
    print(f"✅ Time Complexity: {(time_correct/total)*100:.2f}% ({time_correct}/{total})")
    print(f"✅ Space Complexity: {(space_correct/total)*100:.2f}% ({space_correct}/{total})")
    print("="*50)
    
    overall = (type_correct + pattern_correct + time_correct + space_correct) / (total * 4) * 100
    print(f"🏆 Overall Accuracy: {overall:.2f}%")
    
    if mismatches:
        print(f"\n📝 Found {len(mismatches)} test cases with mismatches")
        
        # Save mismatches to file for analysis
        with open("evaluation_mismatches.json", "w") as f:
            json.dump(mismatches, f, indent=2)
        print("💾 Mismatch details saved to evaluation_mismatches.json")


if __name__ == "__main__":
    run_evaluation()