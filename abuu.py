def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify content (example: make all text uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"\n✅ File read successfully. Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write the file.")

# Ask user for input
user_filename = input("Enter the name of the file to read: ")
read_and_modify_file(user_filename)
