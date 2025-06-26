import os
import re
from datetime import datetime

def find_latest_conversation_file(result_dir="Result"):
    conversation_dir = os.path.join(result_dir, "../logs/conversation")
    files = [f for f in os.listdir(conversation_dir) if f.startswith("conversation_") and f.endswith(".txt")]
    if not files:
        raise FileNotFoundError("No conversation log files found.")
    files.sort(key=lambda x: os.path.getmtime(os.path.join(conversation_dir, x)), reverse=True)
    return os.path.join(conversation_dir, files[0])

def extract_bdd_steps(conversation_file):
    with open(conversation_file, "r") as f:
        content = f.read()
    # Extract the user_request block (BDD steps)
    user_request_match = re.search(r"<user_request>\s*([\s\S]*?)</user_request>", content)
    bdd_steps = user_request_match.group(1).strip() if user_request_match else ""
    # Extract step evaluations
    step_pattern = re.compile(r"## Step (\d+)[\s\S]*?Step evaluation: ([^\n]+)", re.MULTILINE)
    step_results = step_pattern.findall(content)
    return bdd_steps, step_results

def write_bdd_result(bdd_steps, step_results, output_file):
    with open(output_file, "w") as f:
        f.write("Feature: Automated Test Result\n\n")
        f.write("  Scenario: Run through the to-do steps\n")
        # Write BDD steps
        for line in bdd_steps.splitlines():
            if line.strip():
                f.write(f"    {line.strip()}\n")
        f.write("\n    # Step Results\n")
        for step_num, evaluation in step_results:
            status = "PASSED" if "Success" in evaluation else "FAILED"
            f.write(f"    # Step {step_num}: {evaluation} [{status}]\n")

def main():
    try:
        conversation_file = find_latest_conversation_file()
        bdd_steps, step_results = extract_bdd_steps(conversation_file)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"Result/bdd_result_{timestamp}.feature"
        write_bdd_result(bdd_steps, step_results, output_file)
        print(f"BDD result written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 