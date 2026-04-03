import subprocess
import os

TESTS = ["test1"]

def run_test(test_name):
    input_file = os.path.join("test_inputs", f"{test_name}.txt")
    output_file = os.path.join("test_inputs", f"{test_name}_out.txt")

    print(f"\nRunning {test_name}...")

    result = subprocess.run(
        ["python", "code/main.py", input_file, output_file],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("FAIL")
        print(result.stderr)
        return

    print(f"PASS - wrote {output_file}")

def main():
    os.makedirs("test_inputs", exist_ok=True)
    for test in TESTS:
        run_test(test)

if __name__ == "__main__":
    main()