# adding jump command with {jump_place}
temp = "+++{11}++++"
temp_places = {}
temp_stack = []
for index, inst in enumerate(temp):
    if inst == "{":
      temp_stack.append(index)
    if inst == "}":
      # getting the starting of the bracket
      starting = temp_stack.pop()
      # saving the place as end:start
      temp_places[index] = starting
      # saving the place as start:end
      temp_places[starting] = index

pointer = 0
cell_indx = 0
program_temp = [0]*20

while pointer < len(temp):
  inst = temp[pointer]
  if inst == "+":
    program_temp[cell_indx] += 1

  elif inst == "{":
    start = pointer
    end = temp_places[pointer]
    jump_place = int(temp[start+1:end])
    pointer = temp_places[start]
    cell_indx = jump_place
    print(f"start:{start}, end:{end}, jump:{jump_place}")
    continue

  elif inst == "}":
    pointer += 1

  pointer += 1

print(program_temp)