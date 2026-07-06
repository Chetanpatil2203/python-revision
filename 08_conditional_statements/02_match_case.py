status = 400

match status:
    case 200:
        print("error not match")
    case 300:
        print("error not match")   
    case _:
        print("by default")


     