import os
import subprocess

def execute_robot_tests():
    # Change directory to where the .robot test file is located
    os.chdir(r'C:\Users\HP\testai')
    # Directory containing chromedriver.exe
    chromedriver_dir = r"C:\Program Files\ChromeDriver"

    # Get current PATH variable
    current_path = os.environ.get('PATH')

    # Append chromedriver directory to PATH
    os.environ['PATH'] = f"{current_path};{chromedriver_dir}"

    # Run Robot Framework tests using subprocess
    result = subprocess.run(['robot', 'test_cases.robot'], capture_output=True, text=True)
    
    # Check if the test execution was successful
    if result.returncode == 0:
        print("Test cases executed successfully.")
    else:
        print("Failed to execute test cases:")
        print(result.stderr)


