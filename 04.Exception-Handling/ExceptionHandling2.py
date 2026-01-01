import traceback
def addition():
    try:
        a = int(input("Provide value of a : "))
        b = int(input("Provide value of b : "))
        print("Division of a and b is ", a/b)
    except ZeroDivisionError as err:
        print("Not divided by Zero, Provide some valid value")
        print("Error : ", err)
        traceback.print_exc()
    except ValueError:
        print("Please provide valid integer as Value of a or b")
    except:
        traceback.print_exc()
    else:
        print("Within the Else Block")
    finally:
        print("This is finally block")

addition()