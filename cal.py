def do_operation(stack_int, stack_op):
    int_1, int_2 = stack_int.pop(), stack_int.pop()
    op_1 = stack_op.pop() 
    
    if op_1 == '+':
        stack_int.append(int_1 + int_2)
    elif op_1 == '-':
        stack_int.append(int_2 - int_1)
    elif op_1 == '*':
        stack_int.append(int_1 * int_2)
    elif op_1 == '/':
        stack_int.append(int_1 / int_2)    

# Проверка парвильности введных данных
def check_right(s):
    for i in s:
        if not(i in "1234567890+-/*()"):
            return 1

# Удаление пробелов и табов и создание списка
def create_list(s):
    my_list = []
    for i in s:
        if i != ' ' and i != "\t":
            my_list.append(i)

    return my_list

# Строковое представление чисел в просто числа
def str_to_int(tmp):
    
    if not(tmp in "1234567890"):
        return tmp    
    
    len_tmp = len(tmp) - 1
    res = 0
    
    for i in tmp:
        if i == '0':
            res += 0 * 10 ** len_tmp
            len_tmp -= 1
        if i == '1':
            res += 1 * 10 ** len_tmp
            len_tmp -= 1    
        if i == '2':
            res += 2 * 10 ** len_tmp
            len_tmp -= 1
        if i == '3':
            res += 3 * 10 ** len_tmp
            len_tmp -= 1      
        if i == '4':
            res += 4 * 10 ** len_tmp
            len_tmp -= 1
        if i == '5':
            res += 5 * 10 ** len_tmp
            len_tmp -= 1    
        if i == '6':
            res += 6 * 10 ** len_tmp
            len_tmp -= 1
        if i == '7':
            res += 7 * 10 ** len_tmp
            len_tmp -= 1 
        if i == '8':
            res += 8 * 10 ** len_tmp
            len_tmp -= 1
        if i == '9':
            res += 9 * 10 ** len_tmp
            len_tmp -= 1 
    return res

# Список к удобному формату
def list_to_new_format(s_list):
    new_list = []
    tmp = ""
    for i in range(0, len(s_list)):
        
        if i == (len(s_list) - 1):
            if s_list[i] == "(" or s_list[i] == ")":
                new_list.append(s_list[i])
            else:
                tmp += s_list[i]
                new_list.append(str_to_int(tmp))
        else:
            
            if ord(s_list[i]) < 48 or ord(s_list[i]) > 57:
                
                new_list.append(s_list[i])
                continue
            
            tmp += s_list[i]
            
            if ord(s_list[i+1]) < 48 or ord(s_list[i+1]) > 57:
                
                new_list.append(str_to_int(tmp))
                tmp = ""
            
    return new_list
            
# Непосредственно калькуляция            
def calculate(inputs):
    stack_int = []
    stack_op = []
    for a in inputs:
        if type(a) is int:
            stack_int.append(a)
        else:
            if len(stack_op) == 0:
                stack_op.append(a)
            else:
                
                if a == ")":
                    while stack_op[-1] != "(":
                        do_operation(stack_int, stack_op)
                            
                    stack_op.pop()
                    
                else:
                    while op[stack_op[-1]] >= op[a] and stack_op[-1] != ")" and stack_op[-1] != "(":
    
                        do_operation(stack_int, stack_op)
                        
                        if len(stack_op) == 0:
                            break

                    stack_op.append(a)    

    for i in range(len(stack_op)):
        
        do_operation(stack_int, stack_op)
            
    return stack_int.pop()



op = {
"+" : 1,
"-" : 1,
"*" : 2,
"/" : 2,
"(" : 3,
")" : 3
} 

while True:
    
    s = input()
    s_list = create_list(s)
    
    if (check_right(s_list)):
        print("Некрутые символы, введите другие!")
        continue
    
    my_list = list_to_new_format(s_list)
    
    try: 
        
        print(calculate(my_list))

    except:
        print("Некорректо введенные данные") 