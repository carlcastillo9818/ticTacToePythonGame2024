'''
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(word):
    middle_letter = ""
    # % is the modulo operator
    if len(word) % 2 == 0:
        print("even number size string")
    else:
        print("odd number size string")
        middle_letter = word[(len(word) // 2)]

    return middle_letter

middle_letter = mid("apple")
print(f"middle_letter is {middle_letter}")

middle_letter = mid("grape")
print(f"middle_letter is {middle_letter}")

middle_letter = mid("cup")
print(f"middle_letter is {middle_letter}")

middle_letter = mid("bowl")
print(f"middle_letter is {middle_letter}")

middle_letter = mid("xbox")
print(f"middle_letter is {middle_letter}")