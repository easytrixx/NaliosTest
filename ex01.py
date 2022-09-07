import random


def ex01(nb, dict):
    for key,value in dict.items():
        if nb%key==0 :
            return value;
    return nb;


"""VERSION DE BASE !
    if nb%3==0 and nb%5==0:
        return "FizzBuzz"
    elif nb%3==0:
        return "Fizz"
    elif nb%5==0:
        return "Buzz"
    else:
        return nb;
"""



def test_unit():

    dict = {
        3: "Fizz",
        4: "Buzz",
        10: "Egg"
    }

    assert ex01(15,dict)=="Fizz"
    assert ex01(12,dict)=="Fizz"
    assert ex01(20,dict)=="Egg"

if __name__ == "__main__":

    dict = {
        3: "Fizz",
        4: "Buzz",
        10: "Egg"
    }

    for nb in range(1, 101):
        print(ex01(nb,dict))
    test_unit()
