def all_thing_is_obj(object: any) -> int:
    length = 0
    if isinstance(object, str):
        print(object + " is in the kitchen : " + str(type(object)))
    else:
        try:
            length = len(object)
            print(str(type(object))[8:-2].capitalize() + " : "
                    + str(type(object)))
        except TypeError as e:
            print(f"Type not found")
    return 42
