# Read, process, and write to output.txt
try:
    # Step 1: Read the contents of input.txt
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Step 2: Count the number of words
    words = content.split()
    word_count = len(words)

    # Step 3: Convert all text to uppercase
    uppercase_content = content.upper()

    # Step 4: Write processed text and word count to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write("Processed Text:\n")
        outfile.write(uppercase_content + "\n")
        outfile.write(f"Word Count: {word_count}\n")

    # Step 5: Print success message
    print("✅ Success! output.txt has been created with processed content.")

except FileNotFoundError:
    print("❌ input.txt not found. Please make sure the file exists.")
