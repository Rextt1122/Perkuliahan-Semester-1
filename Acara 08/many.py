try:
    print(x)
except NameError:
    print ("variable x not defined")
except:
    print ("something else went wrong ")