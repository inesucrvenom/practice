"""
Evaluate infix arithmetic expression

Assume: no whitespaces in given infix string
Assume: only binary operators (no negative numbers given)

Step 1: convert infix to postfix
using stack

idea from
http://stackoverflow.com/questions/11714582/good-infix-to-prefix-implementation-in-python-that-covers-more-operators-e-g

My version works for more than one char numbers, variables

Step 2: evaluate from postfix
using stack


Remember - pop() gets last one
so, first you get second value,
then pop() gets you first value

"""
# operator's precedece
ops_prec = {'+': 0, '-': 0, '*': 1, '/': 1}


def infix_to_postfix(string_input):
    """
    Convert given arithmetic expression from infix to postfix notation.
    All values are still strings!
    Sig: string -> listof string
    Assume: no whitespace in input string, only binary operators
    """
    stack_ops = []
    output = []
    value = ""

    for item in string_input:
        # item = operator
        if item in ops_prec.keys():
            value = value_to_output(value, output)

            # pop elements while they have lower precedence
            while (stack_ops
                   and stack_ops[-1] in ops_prec.keys()
                   and ops_prec[item] <= ops_prec[stack_ops[-1]]):
                output.append(stack_ops.pop())
            # else put item on stack
            stack_ops.append(item)

        # subexpression, delay precedence
        elif item == '(':
            value = value_to_output(value, output)

            stack_ops.append(item)
        elif item == ')':
            value = value_to_output(value, output)

            # flush output until ( is reached on stack
            while (stack_ops and stack_ops[-1] != '('):
                output.append(stack_ops.pop())
            # remove '('
            stack_ops.pop()

        # value = operand
        else:
            # concatenation of value for multidigit ones
            value += item
            # output.append(item) # this would be for one digit

    # flush stack to output
    value = value_to_output(value, output)

    while stack_ops:
        output.append(stack_ops.pop())

    return output


def value_to_output(value, output):
    """
    Push last created value to output
    Sig: string, listof number -> string
    """
    if value != "":
        output.append(value)
    return ""


def evaluate_postfix(list_input):
    """
    Evaluate given postfix expression
    Sig: listof string -> number
    """
    stack_values = []

    for item in list_input:
        # debug stuff
        # print "item", item
        try:
            item_value = float(item)
            has_value = True
        except ValueError:
            has_value = False

        # value, operand, put on stack
        if has_value:
            stack_values.append(item_value)
            has_value = False

        # operator, pull two operands from stack
        elif (has_value == False
              and len(stack_values) >= 2):
            second_value = stack_values.pop()
            first_value = stack_values.pop()
            result = evaluate_op(item,
                                 first_value,
                                 second_value)
            stack_values.append(result)
            # debug stuff
            # print "midstep", result

    return stack_values.pop()


def evaluate_op(op, first, second):
    """
    Return evaluation of op(first, second)
    Sig: string, number, number -> number
    """

    if op in ops_prec.keys():
        if op == '+':
            output = first + second
        elif op == '-':
            output = first - second
        elif op == '*':
            output = first * second
        elif op == '/' and second != 0:
            output = first / second
        else:
            print "there's some error, maybe div/0?"
            output = None
        return output


# primitive testing
print_list = []
print_list.append("2-3")  # -1
print_list.append("2-3*4+6")  # -4
print_list.append("2-3*(4+6)")  # -28
print_list.append("(2-3)*(4+6)")  # -10
print_list.append("(21-3)*(4+6)")  # -180

for to_print in print_list:
    a = infix_to_postfix(to_print)
    output_print = to_print + ' -> '
    output_print += " ".join(a) + ' = '
    output_print += str(evaluate_postfix(a)) + "\n"
    print output_print
