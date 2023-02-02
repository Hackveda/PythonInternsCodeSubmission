#Stack (LIFO- last in first out)

#making of list
#using push and pop operation
stack = [1,2,3]
stack.append(4)
stack.append(5)
stack

stack.pop()
stack.pop()
stack


#Checking Balance and Unbalance Parentheses
bal_string = "((()))"     #balance string
unbal_string = "(())())"    #unbalance string

def checkBal(str):
    stack = []     #create a empty stack
    is_balance = True   #initalize string as balance
    i = 0   #iterator to iterate over each paren in string

    while i < len(str) and is_balance:
        paren = str[i]   #Read parenthesis at index
        if paren == "(":
            stack.append(paren)
        elif paren == ")":
            if stack:
                stack.pop()
            else:
                is_balance = False    
        i += 1

    return is_balance and not stack

if __name__ == "__main__":
    print (checkBal(bal_string))
    print (checkBal(unbal_string))
