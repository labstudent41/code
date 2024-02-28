try:
    file = open('file.txt', 'r')
    file.read()
except FileNotFoundError:
    print("File was not found")
except KeyboardInterrupt:
    print("Exited.")
finally:
    print("Finished")
