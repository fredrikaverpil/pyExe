import sys, os

exeDir = sys.argv[0] [ 0:sys.argv[0].rfind('\\') ] # Get directory of pyExe.exe
pythonFile = 'myPythonFile.py' # Filename of python file
pythonFilePath = (exeDir + '/' + pythonFile).replace('\\','/') # The location of the python file

# Retrieve any arguments
arguments = ''
if (len(sys.argv) > 1):
	for x in sys.argv:
		if( x != sys.argv[0] ):
			arguments += x + ' '

command = 'python ' + pythonFilePath + ' ' + arguments # Create the command
os.system(command) # Run the command; run the Python file, wrapped with PyExe.exe
