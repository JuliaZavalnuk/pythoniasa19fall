"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem(): 
	result = ""
	poem_lines = [["lay in", "house that Jack built"],
				  ["ate","malt"],
				  ["killed", "rat"],
				  ["worried","cat"],
				  ["tossed", "dog"],
				  ["milked", "cow with the crumpled horn"],
				  ["kissed", "maiden all forlorn"],
				  ["married", "man all tattered and torn"],
				  ["waked", "priest all shaven and shorn"],
				  ["kept", "cock that crowed in the morn"],
				  ["is", "farmer sowing his corn"]]


	for i in range(len(poem_lines)):
	    for j in range(i, -1, -1):
	        if j == i:
	            result += ("This is the " + poem_lines[j][1])
	        else:
	            result += ("That " + poem_lines[j][0] + " the " + poem_lines[j][1])
	        if (j==0):
	        	result += (".\n\n")
	        elif(j==1):
	        	result += ("\n")
	        else:
	        	result += (",\n")
	return (result[:-2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(poem())
