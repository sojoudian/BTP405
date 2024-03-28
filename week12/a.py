import time 

def print_numbers():
    for i in range (1, 6):
        time.sleep(0.5)
        print(i)

def print_letters():
    for letter in 'abcde':
        time.sleep(0.5)
        print(letter)

print_numbers()
print_letters()