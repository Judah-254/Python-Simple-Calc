def process_file():
    # Ask user for the filename to read
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open("modified_output.txt", "w") as new_file:
            new_file.write("Modified Content:\n")
            new_file.write(modified_content)

        print("✅ File processed successfully! Check 'modified_output.txt'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")

    except IOError:
        print(f"❌ Error: Could not read from or write to the file '{filename}'.")

# Run the function
process_file()
