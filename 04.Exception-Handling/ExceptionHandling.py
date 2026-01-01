# import traceback

def SimpleInterest(amount, time, rate):
    try: 
        if rate > 100 or rate < 0:
            raise ValueError("Rate of Interest should be between 0 and 100.")
        if time > 30 or time < 0:
            raise ValueError("Time period should be between 0 and 30 years.")
        simple_interest = (amount * time * rate)/100
        return simple_interest
    except ValueError as e:
        raise ValueError("Invalid Input: " + str(e))
    

    print("Case 1")
    print(SimpleInterest("Harish", 4, 9))
    print("Case 2")
    print(SimpleInterest(10000, 50, 9))
    print("Case 3")
    print(SimpleInterest(10000, 50, -9))