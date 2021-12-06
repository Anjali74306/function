def fun():
    a_variable=0
    local_var="a_variable"in globals()
    print(local_var)
fun()

