# Copyright <2017> <Florian Mueller>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, msole, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# math rule
def point_before_line(op, numbers_list):
    tmpsol = 0
    y = len(op)
    x = 0

    while x != y:
        if x == 0:
            if op[x] == "*":
                tmpsol = numbers_list[x] * numbers_list[x + 1]
                op.pop(x)
                numbers_list.pop(x)
                numbers_list[x] = tmpsol
                x = x - 1
                y = y - 1
            elif op[x] == "/":
                tmpsol = numbers_list[x] / numbers_list[x + 1]
                op.pop(x)
                numbers_list.pop(x)
                numbers_list[x] = tmpsol
                x = x - 1
                y = y - 1

        elif x > 0:
            if op[x] == "*":
                tmpsol = numbers_list[x] * numbers_list[x + 1]
                op.pop(x)
                numbers_list.pop(x)
                numbers_list[x] = tmpsol
                x = x - 1
                y = y - 1
            elif op[x] == "/":
                tmpsol = numbers_list[x] / numbers_list[x + 1]
                op.pop(x)
                numbers_list.pop(x)
                numbers_list[x] = tmpsol
                x = x - 1
                y = y - 1
        x = x + 1
    return op, numbers_list


# check new operators
def check(op, numbers_list, sol):
    # care about math rules
    op, numbers_list = point_before_line(op, numbers_list)

    tmpsol = 0
    for x in range(len(op)):
        if x == 0:
            if op[x] == "+":
                tmpsol = numbers_list[x] + numbers_list[x + 1]
            if op[x] == "-":
                tmpsol = numbers_list[x] - numbers_list[x + 1]
        if x > 0:
            if op[x] == "+":
                tmpsol = tmpsol + numbers_list[x + 1]
            if op[x] == "-":
                tmpsol = tmpsol - numbers_list[x + 1]
    # only multiplications
    if len(op) == 0:
        tmpsol = numbers_list[0]
    # compare result
    if tmpsol == sol:
        return True
    else:
        return False


# generate new set of operators
def generator(n, op, numbers_list, sol):
    y = 0
    diff = len(op) - n

    for x in range(len(op) - diff):
        while y < 4:
            # new lists for list modifications
            tmp_op = op[:]
            tmp_numbers_list = numbers_list[:]

            # check if result is found
            check_sol = check(tmp_op, tmp_numbers_list, sol)
            if check_sol:
                return op;

            if op[x + diff] == "+":
                op[x + diff] = "-"
                if n > 1:
                    generator(n - 1, op, numbers_list, sol)

            elif op[x + diff] == "-":
                op[x + diff] = "*"
                if n > 1:
                    generator(n - 1, op, numbers_list, sol)

            elif op[x + diff] == "*":
                op[x + diff] = "/"
                if n > 1:
                    generator(n - 1, op, numbers_list, sol)

            elif op[x + diff] == "/":
                op[x + diff] = "+"
                if n > 1:
                    generator(n - 1, op, numbers_list, sol)

            y = y + 1
    return op


# main()
def main():
    numbers = int(input("How many operands are shown? "))
    numbers_list = []
    op = []

    for x in range(numbers):
        number_x = int(input(str(x) + ". Operand = "))
        numbers_list.append(number_x)
        op.append("+")

    # decrement operations
    op.pop()
    sol = int(input("solution? "))

    numbers_string = "Your input was:"
    for x in numbers_list:
        numbers_string = numbers_string + " " + str(x) + " _"
    numbers_string = numbers_string[:-2]
    numbers_string = numbers_string + " = " + str(sol)
    print(numbers_string)

    n = len(op)
    result = generator(n, op, numbers_list, sol)
    tmp_result = result[:]
    if result != None and check(tmp_result, numbers_list, sol):
        print("Result: " + str(result))
    else:
        print("Sorry, no solution found! :(")

if __name__ == "__main__":
    main()