def sayHello(name, age):
    if age < 11:
        print("Hi " + name )
    elif age >= 10 and age <= 20: 
        print("Hello " + name)
    else:
        print("How are you? " + name)


sayHello("zero", 10)
sayHello("big", 20)
sayHello("zerobig", 40)

    