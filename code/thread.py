import subprocess

# Define a function to run the first program
def run_program1():
    subprocess.Popen(["python", "code/textbox_ingame.py"])  # Replace with the actual command to run program1

# Define a function to run the second program
def run_program2():
    subprocess.Popen(["python", "code/main.py"])  # Replace with the actual command to run program2

# Start the first program
run_program1()

# Start the second program
run_program2()
