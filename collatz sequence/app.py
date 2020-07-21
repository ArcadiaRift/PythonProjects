def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input("Enter number:"))
except ValueError:
    print("Enter an integer homie")
while num != 1:
    print(collatz(num))
    num = collatz(num)
    