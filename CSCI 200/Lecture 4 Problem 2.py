import math

def sd(x):
    #pass will be substituted with your code
    """
    what function does?
    input:
        x: int
    output:
        sd(x) according to the formula@slides
    """
    a, b = 5.6057, 1.06657
    return math.ceil(a * (x ** 2) + b * x)

def speed(x):
    """
    This function takes distance in feet and returns the least
    input:
        x: int, distance in feet
    return
        float or int
    """
    

if __name__ == "__main__":
    for mph in 5, 25, 50:
        print(mph, sd(mph), speed(sd(mph)))