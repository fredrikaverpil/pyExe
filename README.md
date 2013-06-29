pyExe
======

Ever wanted to make a python script into a standalone .exe file?
Ever wanted to make this standalone .exe file actually just launch another python script (with arguments being passed on to the python script)?
Then maybe pyExe could be something for you.


Requirements
------------

In order to build pyExe.exe you will need:
* [Python](http://www.python.org/) (I've used Python 2.6 64-bit)
* [py2exe](http://www.py2exe.org/) (I've used py2exe 0.6.9 for Python 2.6 64-bit)


Building pyExe.exe
------------------

* Run "build_exe.bat". This will take pyExe.py and compile it into dist/pyExe.exe using py2exe.
* Some DLL files which will be required to run the pyExe.exe will be presented at the end of the compile. Copy all of them from their respective folder and into the "dist" directory, which is created on compile. These DLL files are required for pyExe.exe to run.
* Run "pyExe.exe" (compiled in the "dist" folder) and it should execute the "myPythonFile.py" file.

### Please note
Python (and any modules used in myPythonFile.py) needs to be installed on the machine to be able to execute myPythonFile.py. It's only the contents of pyExe.py which has been turned into a standalone .exe file, not requiring Python to be installed in order to run.

You can modify the contents of pyExe.py to make it into a standalone application which will not require Python or any other modules to be installed in order to run. If this is what you want, just replace the contents of pyExe.py with whatever Python code you want. When you then run "build_exe.bat" you may have to put some DLL files in the same folder as pyExe.py in order to compile pyExe.exe.