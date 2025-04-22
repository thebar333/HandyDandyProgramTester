import subprocess

# Run T1.py and capture the output
result = subprocess.run(["python", "T1.py"], capture_output=True, text=True)

# Retrieve the last printed output
last_output = result.stdout.strip()
print(f"Last printed output: {last_output}")


