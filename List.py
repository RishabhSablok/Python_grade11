def wow(*args, **kwargs):
    print("The main difference between List and Tuple is that List can be modified in our code but tuples cannot.")
    print("This is tuple", args)
    print("This is a dictionary", kwargs)

cources = ["Math", "Science", "English"]
info = {"age" : 22, "clas" : 3, "name" : "BJD"}

wow(*cources, **info)
wow("Math", "Science", a = "a", b = "b")
