import subprocess

def run_program1():
    subprocess.Popen(["python", "code/textbox_ingame.py"]).wait()  # Wait for it to complete
    

def run_program2():
    subprocess.Popen(["python", "code/main.py"])
    

def run_program3():
    subprocess.Popen(["python", "code/textbox_guide_arrows.py"])
  

run_program2()  # bottom layer
run_program1()  
run_program3()  

