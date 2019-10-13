"""
Assignment 1-A
==============

Write fuction that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

>>> print(poem())
This is the house that Jack built.
---
This is the malt
That lay in the house that Jack built.
---
This is the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the farmer sowing his corn,
That kept the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
<BLANKLINE>
"""

def poem():    
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
	            print("This is the " + poem_lines[j][1], end = "")
	        else:
	            print("That " + poem_lines[j][0] + " the " + poem_lines[j][1], end ="")
	        if (j==0):
	        	print(". \n")
	        elif(j==1):
	        	print("")
	        else:
	        	print(",")
	print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    poem()
