def all_thing_is_obj(object: any):
    try:
        assert isinstance(object, str), "Type not found"
        if isinstance(object, str):
            print(object + " is in the kitchen : " + str(type(object)))
        elif len(object):
            print(str(type(object))[8:-2].capitalize() + " : "
                  + str(type(object)))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return 42
