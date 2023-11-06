code = ""  # or make it in the program
# could make it as file input
# data = open("helloWorld.bf","r").read()
# code = data.replace("\n", "")
program = code

# the tape of the [] brackets
pos_br = {}
stack = []

# handling the brackets
for index, inst in enumerate(program):
    if inst == "[":
        stack.append(index)
    if inst == "]":
        # getting the starting of the bracket
        starting = stack.pop()
        # saving the place as end:start
        pos_br[index] = starting
        # saving the place as start:end
        pos_br[starting] = index


# print(pos_br)
PROGRAM_SIZE = 3000
program_list = [0]*PROGRAM_SIZE  # I want my program to be fix size

cell_index = 0  # place to make the operation
index_pointer = 0  # place to track the code

# using while
while index_pointer < len(program):

    instruction = program[index_pointer]

    if instruction == "+":
        program_list[cell_index] += 1
    elif instruction == "-":
        program_list[cell_index] -= 1
    elif instruction == ".":
        print(chr(abs(program_list[cell_index])), end="")
    elif instruction == ",":
        # take only one char even if input more
        program_list[cell_index] = ord(input().split()[0][0])
    elif instruction == ">":
        cell_index += 1
    elif instruction == "<":
        cell_index -= 1
    elif instruction == "[":
        if program_list[cell_index] == 0:
            # if the current cell is zero go to the end
            index_pointer = pos_br[index_pointer]
    elif instruction == "]":
        # if the current cell is not zero jump to the start again
        if program_list[cell_index] > 0:
            index_pointer = pos_br[index_pointer]

    index_pointer += 1
    # print(program_list[0:11], f"place:{cell_index} and op: {instruction}")
