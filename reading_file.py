def read_and_modify_file():
    try:
        # Step 1: Ask the user for the filename
        input_file = input("Enter the name of the file to read: ").strip()
        
        # Step 2: Try opening and reading the file
        with open(input_file, 'r') as file:
            content = file.read()
            print(f"Original Content:\n{content}")
        
        # Step 3: Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Step 4: Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to '{output_file}' successfully!")

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please try again.")
    except PermissionError:
        print("Error: You dogn't have permission to read or write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
