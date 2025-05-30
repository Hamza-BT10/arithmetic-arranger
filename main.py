class Solution(object):
    @staticmethod
    def arithmetic_arranger(problems: list, show_answers=False):
        split_list =[]
        first_num_list = []
        second_num_list = []   
        result = []
        def chech_Nproblems(problems):
            return  len(problems)>5
        def Convert_list(problems):
            for arg in problems:
                split_list.append(arg.split())
            return split_list
        def check_NLenth(problems):
            for arg in problems:
                if len(arg[0]) <= 4 and len(arg[-1]) <= 4:
                    continue
                else:
                    print("Error: Numbers cannot be more than four digits.")
                    return False
            return True
        def Is_Degit(problems):
            for arg in problems:
                if arg[0].isdigit() and arg[-1].isdigit():
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
            for arg in problems:
                if arg[1] == "+":
                    result.append(str(int(arg[0]) + int(arg[-1])))
                elif arg[1] == "-":
                    result.append(str(int(arg[0]) - int(arg[-1])))           
            return result
        def Ajust_Lenth(problems,result: list,i = 0 ): 
            for arg in problems:
                first_num,second_num,operoator = arg[0],arg[-1],arg[1]
                if len(first_num) < len(second_num):
                    second_num = operoator+' '+ second_num
                    first_num = first_num.rjust(len(second_num))
                    result[i] = result[i].rjust(len(second_num))
                elif len(first_num) > len(second_num):
                    first_num = first_num.rjust(len(first_num)+2)
                    second_num = operoator+ second_num.rjust(len(first_num)-1)
                    result[i] = result[i].rjust(len(first_num))
                else:
                    first_num = first_num.rjust(len(first_num)+2)
                    second_num = operoator + second_num.rjust(len(second_num)+1)
                    result[i] = result[i].rjust(len(result[i])+2)   
                first_num_list.append(first_num)
                second_num_list.append(second_num)
                i+=1 
    
        def print_arithmetic_arranger(problems, show_answers=False):
            problems = Convert_list(problems)
            if not validation(problems):
                return
            result = Get_result(problems)
            Ajust_Lenth(problems,result)
            for i in range(len(first_num_list)):
                print(f"{first_num_list[i]}{' ':>4}",end='')  
            print()         
            for i in range(len(second_num_list)):
                print(f"{second_num_list[i]}{' ':>4}",end='')
            print()         
            for i in range(len(second_num_list)):
                print(f"{'-'*len(second_num_list[i])}{' ':>4}",end='')
            if show_answers:
                print()
                for i in range(len(result)):
                    print(f"{result[i]}{' ':>4}",end='')

        if show_answers:
            print()
            print_arithmetic_arranger(problems,show_answers=True)
        else:
            print()
            print_arithmetic_arranger(problems)

problems = ["32 - 698","3801 - 2", "45 + 43", "1239 + 499","225 - 9999"]
Solution.arithmetic_arranger(problems,show_answers=True)
Solution.arithmetic_arranger(problems)
