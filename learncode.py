
### This myfunc test was to understand the scope of a function parameter, which appears to live in the same
### Scope as the function itself.
### def myfunc(test =[]):  # If test is defined within the Parameter list it becomes static test =[]):
###     try: test
###     except NameError: test =[]
###     if test == []:
###         test.append(1)
###         print(f"Test: {test}")
###     else:
###         test.append(test[-1]+1)
###         print(f"Test: {test}")


### myfunc()
### print("running again")
### myfunc()
### print("running again")
### myfunc()

