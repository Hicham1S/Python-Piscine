def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothin: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    else:
        print("Type Not Found")
        return 1
    return 0
