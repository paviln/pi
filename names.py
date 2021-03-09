names = []

isRunning = True
while isRunning:
    name = raw_input("Name: ")
    if(name == "end"):
        isRunning = False
    else:    
        names.append(name)

print(len(names))
