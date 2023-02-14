try:
    print(myname)
except NameError:
    print("My name is not defined")
except:
    print("Another issue")