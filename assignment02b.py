"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""
import re   #  I don't know if regular expresions are part of this course, but it seems to be the most efficient solution for some problems
def poem():  
	result = ""
	poem_lines_rus = [["Вот дом, который построил Джек.", "В доме, который построил Джек."],
					  ["А это пшеница", "Которая в тёмном чулане хранится"],
					  ["А это весёлая птица-синица", "Которая часто ворует пшеницу,"],
					  ["Вот кот", "Который пугает и ловит синицу,"],
					  ["Вот пёс без хвоста", "Который за шиворот треплет кота,"],        
					  ["А это корова безрогая", "Лягнувшую старого пса без хвоста,"],        
					  ["А это старушка, седая и строгая", "Которая доит корову безрогую,"],
					  ["А это ленивый и толстый пастух", "Который бранится с коровницей строгою,"],
					  ["Вот два петуха", "Которые будят того пастуха,"]]


	for i in range(len(poem_lines_rus)):
		if i==0:
			result += poem_lines_rus[0][0]+ "\n\n"
		else:
			for j in range(i, -1, -1):
				if j == i:
					result += (poem_lines_rus[j][0] + ',\n'+ re.sub(r'^(Лягнувшую )', r'Лягнувшая ', poem_lines_rus[j][1]) + '\n' )
				elif (j == 0):
					result += (poem_lines_rus[j][1] + '\n\n')
				else:
					result += (poem_lines_rus[j][1] + '\n')
				
	return (result[:-2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(poem())
