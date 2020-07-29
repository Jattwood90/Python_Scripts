print("Insert the name you want to turn to report case: ", end="")
name = input(str())

def reportCase(name):
    name = name.title()
    name = name.split()
    last = name[-1]
    last = last.upper()
    name.pop(-1)
    name.append(last)
    return ' '.join(name)

print(reportCase(name))