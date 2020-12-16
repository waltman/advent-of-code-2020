from constraint import *

problem = Problem()
problem.addVariable('class', [1,2]) # not 2-3
problem.addVariable('row', [0,1,2]) # not 6-7
problem.addVariable('seat', [2]) # not 14-15
problem.addConstraint(AllDifferentConstraint())
print(problem.getSolutions())
