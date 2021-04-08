largest = None
smallest = None


while True:
    try:
        num = input("Enter a number: ")
        if num == "done" :
            break

        num = int(num)
    except:
        print("Invalid input")

for list in [num]:
    if list > largest :
        largest = num
    if list > smallest :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
