def all_thing_is_obj(object: any) -> int:

    convert = {
        list: f"List : {type(object)}",
        tuple: f"Tuple : {type(object)}",
        set: f"Set : {type(object)}",
        dict: f"Dict : {type(object)}",
        str: f"{object} is in the kitchen : {type(object)}",
        int: "Type not found"
    }

    print(convert[type(object)])
    return (42)
