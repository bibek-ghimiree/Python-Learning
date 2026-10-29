try:
    print("Program started")
    result = 10 / 0

except ZeroDivisionError:
    print("An error occurred.")

finally:
    print("Program finished.")

