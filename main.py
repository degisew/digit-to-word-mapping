digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
output = ""
digits = '0123456789'
phone = input("Enter your phone number: ")
for char in phone:
    if char not in digits:
        print("Please enter digits only!")
        phone = input("Enter your phone number: ")
    else:
        output += (digits_mapping.get(char) + " ")
print(output)
