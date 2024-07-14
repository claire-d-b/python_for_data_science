def NULL_not_found(object: any):
    match str(type(object))[8:-2].capitalize():
        case 'Nonetype':
            print("Nothing: ", object, type(object))
            return 0
        case 'Float':
            if object != object:
                print("Cheese: ", object, type(object))
                return 0
            else:
                print("Type not found")
                return 1
        case 'Int':
            print("Zero: ", object, type(object))
            return 0
        case 'Str':
            if object:
                print("Type not found")
                return 1
            else:
                print("Empty: ", object, type(object))
                return 0
        case 'Bool':
            print("Fake: ", object, type(object))
            return 0
        case _:
            print("Type not found")
            return 1
