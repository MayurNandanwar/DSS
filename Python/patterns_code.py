

# ****
# ****
# ****
def pattern(n):
    lst = []
    for i in range(n):
        x = ''
        for j in range(n):
            x = x + '* '
        lst.append(x)
    res = '\n'.join(lst)
    return res

# *
# **
# ***

def tri_pattern(n):
    lst = []
    for i in range(n):
        x = ''
        for j in range(i):
            x += '* '
        if x !='':
            lst.append(x)
    res = '\n'.join(lst)
    return res

# 1
# 12
# 123
# 1234

def numb_pattern(n):
    lst = []
    for i in range(2,n+1):
        x = ''
        for j in range(1,i):
            print(j)
            x+=str(j)
        print(x)
        lst.append(x)
    res = '\n'.join(lst)
    return res

# 1
# 22
# 333
def same_num(n):
    lst = []
    for i in range(n):
        lst.append(i * str(i))
    res = '\n'.join(lst)  
    return res


# ****
# ***
# **
# *

def revers_star(n):
    lst =[]
    for i in range(n,0,-1):
        lst.append(i*'* ')
    return '\n'.join(lst)


# 12345
# 1234
# 123
# 12
# 1
def num_desc(n):
    lst =[]
    for i in range(n,0,-1):
        x = ''
        for i in range(1,i+1):
            x+=str(i)
        lst.append(x)
    return '\n'.join(lst)

# 54321
# 4321
# 321
# 21
# 1
def rev_num_desc(n):
    lst =[]
    for i in range(n,0,-1):
        x = ''
        for i in range(i,0,-1):
            x+=str(i)
        lst.append(x)
    return '\n'.join(lst)


#    *
#   ***
#  *****
# *******

def triangle(n):
    lst = []
    for i in range(0,n):
        lst.append((n-i)*' '+i*'*'+(i+1)*'*')
    return '\n'.join(lst)

        
# *******
#  *****
#   ***
#    *

def rev_triangle(n):
    lst = []
    for i in range(0,n):
        lst.append((i)*' '+(((2*(n-i))-1))*'*'+(i)*' ')
    return '\n'.join(lst)

# print(rev_triangle(5))


#   *
#  ***
# *****
# *****
#  ***
#   *
def asc_desc_tri(n):
    lst = []
    for i in range(0,n):
        lst.append((n-1-i)*' '+i*'*'+(i+1)*'*')

    for i in range(0,n):
            lst.append((i)*' '+(((2*(n-i))-1))*'*')
    return '\n'.join(lst)



# 12345
# 1234
# 123
# 12
# 1
# 1
# 12
# 123
# 1234
# 12345
def num_des_asc(n):
    lst = []
    for i in range(n,0,-1):
        x = ''
        for i in range(1,i+1):
            x+=str(i)
        lst.append(x)

    for i in range(1,n+1):
        x = ''
        for i in range(1,i+1):
            x+=str(i)
        lst.append(x)
    return '\n'.join(lst)


# 1
# 0 1 
# 1 0 1
# 0 1 0 1

def zero_one_alter(n):

    lst = []
    for i in range(1,n+1):# 3
        if i%2==0:
            x='0'
            for i in range(1,i): # 1 2 
                if i%2!=0:
                    x+='1'
                else:
                    x+='0'
            lst.append(x)
        else:
            x = '1'
            for i in range(1,i): # 1 2 3 
                if i%2!=0:
                    x+='0'
                else:
                    x+='1'
            lst.append(x)
    return '\n'.join(lst)

# 1     1
# 12   21
# 123 321
# 1234321
def v_shap_num(n):
    lst = []
    for i in range(1,n+1):
        x= ''
        for j in range(1,i):
            x+=str(j)

        x+=((2*n)-(2*(i)+1))*' '

        y = ''
        for k in range(1,i):
            y+=str(k)
        y = ''.join(list(reversed(y)))
        if i==(n):
            y = y[1:]

        x+=y

        lst.append(x)
    return '\n'.join(lst)
    
# print(v_shap_num(6))

    

    
    

        

