try:
    a = int(input("Enter number: "))
    b = int(input("Enter index: "))
    c = a ** b
    print(c)
except ValueError:
    print("Numbers only")
except KeyboardInterrupt:
    print("Exited.")
