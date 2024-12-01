file = open("input")

first_column=[]
second_column=[]

for line in file.readlines():
    line=line.rstrip("\n").split("   ")
    first_column.append(line[0])
    second_column.append(line[1])
first_column.sort()
second_column.sort()

result=0

for (index,element1) in enumerate(first_column):
    element2=second_column[index]
    result+=abs(int(element1)-int(element2))
print(result)
#2375403
