#!/usr/bin/env python3

import operator
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def percentage(a,b):
	return (100*b/a)
	
operators = {
	'+':operator.add,
	'-':operator.sub,
	'*':operator.mul,
	'/':operator.truediv,

	#"Implement additional calculator key."
	'%':percentage,
	#'^':operator.pow,
	'.':operator.floordiv,

}

def calculate (arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		
		except ValueError:
			function = operators[token]
			
			if len(stack) == 1:
				arg1 = stack.pop()
				result = function(arg1)
				
			else:
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1, arg2)
			
			stack.append(result)		
			
		logger.debug(stack)
	
	if len(stack) != 1:
		raise TypeError	
		
	return stack.pop()
	
def main():
	while True:
		print( calculate( input("rpn calc>") ) )
	
if __name__ == "__main__":
	main()
