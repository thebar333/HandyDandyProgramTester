import subprocess
expv = input("Expected value:")
PyFi = input("Python file [Format: file.py]")
result = subprocess.run(["python", PyFi], capture_output=True, text=True)
lotpt = result.stdout.strip()
if lotpt == expv: 
    print("pass")
else:
    print("fail")               






