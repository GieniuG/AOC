file = open("input")

first_column=[]
second_column=[]

for line in file.readlines():
    line=line.rstrip("\n").split("   ")
    first_column.append(int(line[0]))
    second_column.append(int(line[1]))
first_column.sort()
second_column.sort()

result = 0
for el in first_column:
    result+=el*second_column.count(el)
print(result)
#23082277
