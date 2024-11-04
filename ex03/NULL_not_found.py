import math
def NULL_not_found(object: any) -> int:

    if not object:
        if object == None:
            print(f"Nothing: {object} {type(object)}")
        elif type(object) == str:
            print(f"Empty: {object} {type(object)}")
        elif type(object) == int:
            print(f"Zero: {object} {type(object)}")
        elif type(object) == bool:
            print(f"Fake: {object} {type(object)}")
    else:
        if type(object) == float and math.isnan(object):
            print(f"Cheese: {object} {type(object)}")
        else:
            print("Type not Found")
            return 1

    return 0
