from constraint import *

def all_diff_nonzero(*args):
    seen = set()
    for a in args:
        if a > 0:
            if a in seen:
                return False
            else:
                seen.add(a)
    return True

def sum_to(*args):
    print(f'{args=}')
    return sum(args) == 7

problem = Problem()
foods = {'mxmxvkd', 'kfcds', 'sqjhc', 'nhms', 'trh', 'fvjkl', 'sbzzf', 'mxmxvkd', 'sqjhc', 'fvjkl', 'sqjhc', 'mxmxvkd', 'sbzzf'}
for food in foods:
    problem.addVariable(food, [0,1,2,4])

#problem.addConstraint(lambda a,b,c,d: (a + b + c + d) & 3 == 3, ('mxmxvkd', 'kfcds', 'sqjhc', 'nhms'))
s = 'lambda a,b,c,d: (a + b + c + d) & 3 == 3'
problem.addConstraint(eval(s), ['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'])
problem.addConstraint(lambda a,b,c,d: (a + b + c + d) & 1 == 1, ('trh', 'fvjkl', 'sbzzf', 'mxmxvkd'))
problem.addConstraint(lambda a,b: (a + b) & 4 == 4, ('sqjhc', 'fvjkl'))
problem.addConstraint(lambda a,b,c: (a + b + c) & 2 == 2, ('sqjhc', 'mxmxvkd', 'sbzzf'))
#problem.addConstraint(lambda a,b,c,d,e,f,g: (a + b + c + d + e + f + g) == 7, list(foods))
problem.addConstraint(FunctionConstraint(all_diff_nonzero), list(foods))
problem.addConstraint(FunctionConstraint(sum_to), list(foods))
print(problem.getSolutions())

