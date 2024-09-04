def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(object + " is in the kitchen : " + str(type(object)))
    else:
        try:
            print(str(type(object))[8:-2].capitalize() + " : "
                  + str(type(object)))
        except TypeError:
            print("Type not found")
    return 42

# Running this alone does nothing. It is used as a module.