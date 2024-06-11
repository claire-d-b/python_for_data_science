def all_thing_is_obj(object):
#your code here
    try:
        if isinstance(object, str):
            print(object + " is in the kitchen : " + str(type(object)))
        elif len(object):
            print(str(type(object))[8:-2].capitalize() + " : " + str(type(object)))
    except:
        print("Type not found")
    return 42

