# Prolog
# Author:  Hardik Jhunjhunwala
# Email:  hjhunjhunwala1@student.gsu.edu
# Section: 22
'''
  Purpose: 
      convert feet to inches, using fact that there are 12 inches in 1 foot
  Pre-conditions (input): 
      number of feet (floating point)
  Post-conditions (output): 
      number of inches, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of feet to inches")
    print()

#  2.  Input amount of feet from user

    feet = float(input("How many feet? "))

#  3.  Calculate number of inches
    # 12 inches in one foot
    inches = feet * 12

#  4. Output resulting inches and given number of feet
    print()
    print(feet, "feet is {:.2f} inches".format(inches))

main()
# end of program file
# 

#1. There were 2 indentation errors in the code. The print statements were not indented properly.
#2. 1st indentation error:
#Traceback (most recent call last):
#  File "C:\Users\Hardik\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
#    return _run_code(code, main_globals, None,
#  File "C:\Users\Hardik\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 86, in _run_code
#    exec(code, run_globals)
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy\__main__.py", line 39, in <module>
#    cli.main()
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 430, in main    run()
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 284, in run_file
#    runpy.run_path(target, run_name="__main__")
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy    code, fname = _get_code_from_file(run_name, path_name)
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 294, in _get_code_from_file
#    code = compile(f.read(), fname, 'exec')
#  File "c:\Users\Hardik\Desktop\hello\feet.py", line 18
#    print("Conversion of feet to inches")
#    ^
#IndentationError: expected an indented block after function definition on line 14
#2nd indentation error:
#Traceback (most recent call last):
#  File "C:\Users\Hardik\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
#    return _run_code(code, main_globals, None,
#  File "C:\Users\Hardik\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 86, in _run_code
#    exec(code, run_globals)
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy\__main__.py", line 39, in <module>
#    cli.main()
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 430, in main    run()
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 284, in run_file
#    runpy.run_path(target, run_name="__main__")
#.py", line 320, in run_path
#    code, fname = _get_code_from_file(run_name, path_name)
#  File "c:\Users\Hardik\.vscode\extensions\ms-python.python-2022.12.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 294, in _get_code_from_file
#    code = compile(f.read(), fname, 'exec')
#  File "c:\Users\Hardik\Desktop\hello\feet.py", line 31
#    print(feet, "feet is {:.2f} inches".format(inches))
#IndentationError: unexpected indent
#3. Fixed error in line 14 by indenting the print statement properly. Fixed error in line 31 by indenting the pirnt statement properly.
#4. The semantic error in the program is the multiplication for conversion of feet to inches was wrong in line 27. The value being used to convert number of feet to inches was wrong since, to convert number of feet into inches the number of feet should be multiplied by 12 and not 9.
#5. The semantic error was in line 27.
#6. The semantic error was fixed by changing the number which was being multiplied by number of feet. The original value given was 9 it was changed to 12.