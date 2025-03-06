
# Two lists of equal length
list1 = [10, 20, 30, 40]
list2 = [2, 0, 5, 10,]

for i in range(len(list1)):
    try:
            print(f"Dividing {list1[i]} by {list2[i]}")
            result = list1[i] / list2[i]  # This may cz either IndexError or ZeroDivisionError
            print(f"Result: {result}")

    except IndexError:
        print(f"IndexError: List index is out of range.")
    except ZeroDivisionError:
        print(f"ZeroDivisionError {list1[i]} by {list2[i]}.")
    except ArithmeticError:
        print(f"ArithmeticError: There was a general arithmetic error.")

    finally:
        print("It will run everytime")