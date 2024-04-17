def find_my_shape(name,number_of_side,property):
    if name.islower()=="rectangle" and number_of_side==4  and property.islower()=="all sides equal":
        print(f"Right!!! Shape is a {name}")
    elif name.islower()=="triangle" and number_of_side==3  and property.islower()=="all sides equal":
        print(f"Right!!! Shape is a {name}")
    elif name.islower()=="square" and number_of_side==4  and property.islower()=="two opposite sides are equal":
        print(f"Right!!! Shape is a {name}")
    elif name.islower()=="circle" and number_of_side.islower()=="infinity" and property.islower()=="regular":
        print(f"Right!!! Shape is a {name}")
    else:
        print("Try again, shape is either not correct or advanced.")