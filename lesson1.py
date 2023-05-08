
# List
names = ['Valeria', 'Elad', 'Maria', 'Moshe', 'David', 'Tamir']
# print(type(names))
# print(names)
# print(names[0])
# print(type(names[0]))
# print(names[2])
# print(names[-1])
# print(names[-3])
# print(names[1:4])
# print(names[-1:-4:-1])
# print(names[1:4:5])
# print(names[2:3:1])
# print(names[2])
# print(names[2:])
# print(names[:-1])
# print(names[::-1])
# print(names[-1::-1])

# grades = [87, 90, 56, 67]

# various = ['Moshe', 23874, True, 4.5, 345]
# various[2]  # bool
# various[0]  # str


# nested_list = [['Moshe', 90], ['Valeria', '87'], ['Tamir', '70']]
# nested_list[1][1]

# l = []
# l.append("Valeria")
# print(l)
# l.append("David")
# print(l)
# l.insert(0, 'David')
# l.append('Tamir')
# l.append('Elad')
# l.append('Valeria')
# print(l)  # ['David', 'Valeria', 'Tamir', 'Elad', 'Valeria']
# l.pop(2)
# print(l)
# l.remove('Valeria')
# print(l)
# print(len(l))
# l1 = []
# l1 = ['Valeria']
# print(l.index('Elad', 1, 2))
#
# grades = [80, 100, 56, 100, 90]
# print(grades.count(100))
#
# print(min(grades))
# print(max(45, 100, 345, 1, 23))

# text = "Hello World, the sun is shining and thw life is beautiful"
# print(text[-1])
# print(type(text[-1]))
# print(text[::-1])
# print(len(text))
# print(text.index("el"))
# print(text.index("o", 5))
# print(text.find("ttt"))
# print(text.split(" ")[-1])
# print(text.split(","))


# Implement a code that receives the layout of the seats in
# the aircraft as letters and returns the layout as numbers.
# For example:
# ABC DEF => 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.
# plane = input('enter plane structure: ')
# spl = plane.split(' ')
#
# if len(spl) == 2:
#      print(f'plane structure is ', len(spl[0]), len(spl[1]))
# elif len(spl) == 3:
#     print(f'plane structure is ', len(spl[0]), len(spl[1]), len(spl[2]))


# str_list = ['asd', 'asdasfhs', 'sdfasdf', 'dfgdafg']
# print(' '.join([str(len(x)) for x in str_list]))




# String slicing
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1



# Implement a code that receives the aircraft seat number (4J, 34A, etc…)
# and aircraft layout like in the previous exercise (ABC DEF, ABC DEFGH IJK,...).
# Your code should print out 3 things:
# Row number
# Seat Character
# Print whether the user is going to sit near the window, in the aisle, or in the middle.
# For example, for the input: 4J and ABC DEFG HIJ: the output should be:
# Row number: 4
# Char: J
# Window
#
# You can assume that row number is a maximum 2-digit number,
# and seat Char is always a one single char.


seat = input("Insert seat number (for example, 13B): ")
structure = input("Insert aircraft structure (for example: ABC DEFG HIJ): ")

# 13B
# 4C

if seat[1].isdigit():
    row = seat[0:2]
else:
    row = seat[0]

# if len(seat) == 2:

seat_char = seat[-1]
print(f"Row: {row} | Seat char: {seat_char}")
# 13B
# 4C
# ABC DEF
seat_char_idx = structure.index(seat_char)
if seat_char_idx == len(structure)-1 or seat_char_idx == 0:
    print("window")
elif structure[seat_char_idx-1] != " " and structure[seat_char_idx+1] != " ":
    print("middle")
else:
    print("aisle")
