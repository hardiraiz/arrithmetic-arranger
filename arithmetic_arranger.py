from typing import List


def arithmetic_arranger(*args):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if len(args) > 1:
        problems = args[0]
        show_answers = args[1]
    else:
        problems = args[0]
        show_answers = False

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for idx, problem in enumerate(problems):
        split_problem = problem.split()
        len_num1 = len(split_problem[0])
        len_num2 = len(split_problem[2])

        if split_problem[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        
        if split_problem[0].isdecimal() is False or split_problem[2].isdecimal() is False:
            return "Error: Numbers must only contain digits."

        if len_num1 > 4 or len_num2 > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if len_num1 >= len_num2:
            distance1 = len_num1+2
            distance2 = len_num1
        else:
            distance1 = len_num2+2
            distance2 = len_num2
        
        if len(problems) > idx+1:
            line1 += '{}{}'.format(split_problem[0].rjust(distance1), ' '*4)
            line2 += '{} {}{}'.format(split_problem[1], split_problem[2].rjust(distance2), ' '*4)
            line3 += '{}{}'.format('-'*distance1, ' '*4)
            if show_answers is True:
                line4 += '{}{}'.format(str(eval(problem)).rjust(distance1), ' '*4)
        else:
            line1 += '{}'.format(split_problem[0].rjust(distance1))
            line2 += '{} {}'.format(split_problem[1], split_problem[2].rjust(distance2))
            line3 += '{}'.format('-'*distance1)
            if show_answers is True:
                line4 += '{}'.format(str(eval(problem)).rjust(distance1))
        
    temp_arr = list()
    temp_arr.append(line1)
    temp_arr.append(line2)
    temp_arr.append(line3)
    if show_answers is True:
        temp_arr.append(line4)
    
    arranged_problems = ""
    for idx, x in enumerate(temp_arr):
        if len(temp_arr) > idx+1:
            arranged_problems += '{}\n'.format(x)
        else:
            arranged_problems += '{}'.format(x)

    return arranged_problems
