class Solution(object):
    @staticmethod
    def arithmetic_arranger(problems: list, show_answers=False):
        split_list =[]
        first_num = []
        second_num = []   
        result = []
        def chech_Nproblems(problems):
            return  len(problems)>5
        def Convert_list(problems):
            for problem in problems:
                split_list.append(problem.split())
            return split_list
        def check_NLenth(problems):
            for problem in problems:
                if len(problem[0]) > 4 or len(problem[-1]) > 4:
                    print("Error: Numbers cannot be more than four digits.")
                    return False
                else:
                    continue
            return True
        def Is_Degit(problems):
            for problem in problems:
                if problem[0].isdigit() and problem[-1].isdigit():
                    continue
                else:
                    print('Error: Numbers must only contain digits.')
                    return False
            return True    
        def check_operators(problems):
            for operator in problems:
                if operator[1] not in ["+","-"]:
                    print("Error: Operator must be '+' or '-'.")
                    return False
            return True 
        def validation(problems):
            if chech_Nproblems(problems):
                print("Error: Too many problems.")
                return False
            elif not check_NLenth(problems):
                return False   
            elif not Is_Degit(problems):
                return False
            elif not check_operators(problems):
                return False
            return True   
        def Get_result(problems):
            for object in problems:
                if object[1] == "+":
                    result.append(str(int(object[0]) + int(object[-1])))
                elif object[1] == "-":
                    result.append(str(int(object[0]) - int(object[-1])))           
            return result
        def Ajust_Lenth(problems,result: list): 
            i = 0 
            for problem in problems:
                if len(problem[0]) < len(problem[-1]):
                    len_num =' '* (abs(len(problem[0]) - len(problem[-1]))+2)
                    problem[0] = len_num+problem[0]
                    problem[-1] =problem[1]+' '+ problem[-1]
                    result[i] = ' '*(len(problem[-1])-len(result[i]))+result[i]
                elif len(problem[0]) > len(problem[-1]):
                    len_num =' '* (abs(len(problem[0]) - len(problem[-1])))
                    problem[-1] =problem[1]+len_num + problem[-1]
                    problem[0] = ' ' +problem[0]
                    result[i] = ' '*(len(problem[-1])-len(result[i]))+result[i]
                else:
                    problem[0] = '  '+problem[0]
                    problem[-1] = problem[1] + ' '+ problem[-1]
                    result[i] = '  '+ result[i]
                i+=1   
                first_num.append(problem[0])
                second_num.append(problem[-1]) 
    
        def print_arithmetic_arranger(problems, show_answers=False):
            problems = Convert_list(problems)
            if not validation(problems):
                return
            result = Get_result(problems)
            Ajust_Lenth(problems,result)
            for i in range(len(first_num)):
                print(f"{first_num[i]}{' ':>4}",end='')  
            print()         
            for i in range(len(second_num)):
                print(f"{second_num[i]}{' ':>4}",end='')
            print()         
            for i in range(len(second_num)):
                print(f"{'-'*len(second_num[i])}{' ':>4}",end='')
            if show_answers:
                print()
                for i in range(len(result)):
                    print(f"{result[i]}{' ':>4}",end='')

        if show_answers:
            print_arithmetic_arranger(problems,show_answers=True)
        else:
            print("\n")
            print_arithmetic_arranger(problems)

problems = ["32 - 698","3801 - 2", "45 + 43", "1239 + 499","225 - 9999"]
Solution.arithmetic_arranger(problems,show_answers=True)
Solution.arithmetic_arranger(problems)
