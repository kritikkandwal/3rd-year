# 1) print all number in list 


nums = input("Enter numbers separated by spaces: ").split()

def print_list(list):
    for i in list:
        print(i," ")
        
print_list(nums)


# 2) factorial using function

nums = int(input("Enter a number: "))

def wwe(n):
    if n == 0 or n == 1:
        return 1
    return n * wwe(n-1)

print("Factorial:", wwe(nums))
