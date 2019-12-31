"""
Alex Petrov
CPE 202
Project 2
"""
from stacks import StackArray

def infix_to_postfix(infix):
    """Converts a infix string into a postfix string
        Args:
            infix(string) - the infix expression
        Returns:
            new_eq(string) - a postfix expresion
    """
    if infix_valid(infix):
        operators = StackArray(30)
        ans_list = []
        looklist = infix.split()
        prec = {}
        prec["^"] = 4
        prec["~"] = 3
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1


        for item in looklist:
            if item not in "()+-*/~^":
                ans_list.append(item)
            elif item == "(":
                operators.push(item)
            elif item == ")":
                top = operators.peek()
                operators.pop()
                while top != "(":
                    ans_list.append(top)
                    top = operators.peek()
                    operators.pop()
            else:
                while not operators.is_empty() and ((prec[operators.peek()]) >= prec[item]):
                    ans_list.append(operators.peek())
                    operators.pop()
                operators.push(item)

        while not operators.is_empty():
            ans_list.append(operators.peek())
            operators.pop()
        new_eq = " ".join(ans_list)
        return new_eq

def postfix_eval(postfix):
    """evaluates a postfix expression
        Args:
            postfix(string) - the postfix expression to be evaluated
        Returns:
            This function returns an intger that is the solution to the equation
    """
    int_stack = StackArray(30)
    eq_list = postfix.split()
    if not postfix_valid(postfix):
        raise SyntaxError()
    else:
        for item in eq_list:
            if item not in "()+-*/~^":
                num = int(item)
                int_stack.push(num)
            elif item is "~":
                op1 = int_stack.peek()
                int_stack.pop()
                new_val = negate(op1)
                int_stack.push(new_val)
            else:
                op2 = int_stack.peek()
                int_stack.pop()
                op1 = int_stack.peek()
                int_stack.pop()
                new_val = math_help(item, op1, op2)
                int_stack.push(new_val)
        return int_stack.peek()

def negate(op):
    """negates a number
        Args:
            op(int) - the number
        Returns:
            This returns the negatove verion of the input
    """
    return op * -1

def math_help(op, op1, op2):
    """This function does the mathimatical operations needed to evaluate
        Args:
            op(string) - this argument is the mathematical operator 
                that shows the operation that needs to be done
            op1, op2 (int) - the integers that are used in the math
        Returns:
            the result of the mathematical operation
    """ 
    if op is "^":
        return op1 ** op2
    elif op is "*":
        return op1 * op2
    elif op is "/":
        if op2 == 0:
            raise ZeroDivisionError
        return op1 / op2
    elif op is "+":
        return op1 + op2
    elif op is "-":
        return op1 - op2

def size(list):
    """calculates the size of an expression
        Args:
            list(list) - the expression
        Returns:
            size(int) - the length of the list
    """
    size = 0
    for i in list:
        size += 1
    return size

def postfix_valid(postfix):
    """Checks the validity of a postfix expression
        Args:
            postfix(string) - the postfix expression
        Returns:
            Boolean - True if expression is valid, Flase if not
    """
    check_list = postfix.split()
    left = 0
    right = 0
    ops = 0
    ints = 0
    neg = 0
    list_size = size(check_list)
    if postfix == "":
        return False
    else:
        for i in range(0, list_size):
            if check_list[i] is "(":
                left += 1
            elif check_list[i] is ")":
                right += 1
            elif check_list[i] in "+-*/^":
                ops += 1
            elif check_list[i] not in "+-*/~^ ":
                ints += 1
            else:
                neg += 1
    if ints <= ops:
        return False
    elif ints != (ops + 1):
        return False
    elif postfix[0] in "+-*/~^ ":
        return False
    for i in range(len(postfix)):
        if postfix[i] not in "0123456789*^+-~/() ":
            return False
    return True

def infix_valid(infix):
    """Checks the validity of a infix expression
        Args:
            infix(string) - the infix expression
        Returns:
            Boolean - True if expression is valid, Flase if not
    """
    check_list = infix.split()
    length = len(infix) 
    left = 0
    right = 0
    ops = 0
    ints = 0
    neg = 0
    list_size = size(check_list)
    if infix == "":
        raise SyntaxError("The list is empty!")
    else:
        for i in range(0, list_size):
            if check_list[i] == "(":
                left += 1
            elif check_list[i] == ")":
                right += 1
            elif check_list[i] in "+-*/^":
                ops += 1
            elif check_list[i] not in "+-*/~^ ":
                ints += 1
            else:
                neg += 1
    if right != left:
        raise SyntaxError("Parenthases Mismatch")
    if ints <= ops:
        raise SyntaxError("Operator Mismatch - too many operators")
    elif ints != (ops + 1):
        raise SyntaxError("Operator Mismatch - too many ints")
    for i in range(length):
        if infix[i] not in "0123456789*^+-~/() ":
            raise SyntaxError()
        i += 1
    return True
