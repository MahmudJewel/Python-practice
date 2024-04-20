# def solve(s):
# 	return (' '.join(i.capitalize() for i in s.split(' ')))

# s='hello 3g world'
# print(solve(s))

# for i in range(5, 21, 3):
# 	print(i)


# d = {"a": 1, "b": 2, "c": 3}
# for i in d:
#     print(i)

# x=[1,2,3]
# y=x
# x.append(4)
# print(y)

# def detect_line_type(code):
#     if code.count('\n') > 0:
#         lst = list(code.split('\n'))
#         print('Multiple => ===========> ', lst)
#         return "Multiple lines"
#     else:
#         return "Single line"

# # Example usage
# code1 = "print('Hello, world!')"
# code2 = """
# for i in range(5):
#     print(i)
# """
# print(detect_line_type(code1))  # Output: Single line
# print(detect_line_type(code2)) 

import subprocess

def run_shell_command(command, directory):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=directory)
        
        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Command failed with error: {result.stderr}"
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {e.stderr}"

# Example usage:
command = """
a=104
echo $a
date
"""
directory = "/run/media/mahmud/Data/iawstest"
output = run_shell_command(command, directory)
print(output)
