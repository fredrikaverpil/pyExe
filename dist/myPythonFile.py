import sys

print 'Hello world'

# Retrieve any arguments
arguments = ''
if (len(sys.argv) > 1):
	for x in sys.argv:
		if( x != sys.argv[0] ):
			arguments += x + ' '
	print 'You passed on some arguments: ' + arguments