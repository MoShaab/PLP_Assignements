# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 67890\n")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())  # strip() removes leading and trailing whitespace, including the newline character
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("Appending more text\n")
        file.write("Yet another line for appending\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending completed.")

