
# Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string

text = input("Please Enter Your Text here:")
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
counter = 0
for letter in text:
    if letter in vowels:
        counter += 1

print("Number of Vowels is : ", counter)

