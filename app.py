from ascii import ascii_art
import os

print(ascii_art)
def calculator():
    usr_select = (input("Type 1 For Division \nType 2 for Mulitplication \nType 3 for Addition \nType 4 for Subtraction \nType answer here: "))
    # for Division
    if usr_select == "1":
        val1 = float(int(input("Enter Value 1: ")))
        val2 = float(int(input("Enter Value 2: ")))
        output = val1 / val2
        print(f"the answer is {output}")
    # for Multiplication
    elif usr_select == "2":
        val1 = float(int(input("Enter Value 1: ")))
        val2 = float(int(input("Enter Value 2: ")))
        output = val1 * val2
        print(f"the answer is {output}")
    # for Addition
    elif usr_select == "3":
        val1 = float(int(input("Enter Value 1: ")))
        val2 = float(int(input("Enter Value 2: ")))
        output = val1 + val2
        print(f"the answer is {output}")
    # for Subtraction
    elif usr_select == "4":
        val1 = float(int(input("Enter Value 1: ")))
        val2 = float(int(input("Enter Value 2: ")))
        output = val1 - val2
        print(f"the answer is {output}")
    use_num = input(f"Do you want to do more math with {output}  Type y/n ").lower()
    while use_num == "y":
        usr_select = (input("Type 1 For Division \nType 2 for Mulitplication \nType 3 for Addition \nType 4 for Subtraction \nType answer here: "))
        # for Division
        if usr_select == "1":

            val2 = float(int(input("Enter Value 2: ")))
            output = output / val2
            print(f"the answer is {output}")
        # for Multiplication
        elif usr_select == "2":
            val2 = float(int(input("Enter Value 2: ")))
            output = output * val2
            print(f"the answer is {output}")
        # for Addition
        elif usr_select == "3":
            val2 = float(int(input("Enter Value 2: ")))
            output = output + val2
            print(f"the answer is {output}")
        # for Subtraction
        elif usr_select == "4":
            val2 = float(int(input("Enter Value 2: ")))
            output = output - val2
            print(f"the answer is {output}")
        use_num = input(f"Do you want to do more math with {output}  Type y/n ").lower()
    while use_num == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        calculator()
calculator()