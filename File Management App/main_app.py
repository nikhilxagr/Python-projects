import os

def create_file(file_name, content):
    try:
        with open(file_name, 'x') as file:
            file.write(content)
            print(f"File '{file_name}' created successfully.")
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir('.')
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(f"- {file}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(file_name, new_content):
    try:
        with open(file_name, 'a') as file:
            file.write(new_content)
            print(f"File '{file_name}' updated successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nFile Management App")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            file_name = input("Enter the file name to create: ")
            content = input("Enter content to write to the file: ")
            create_file(file_name, content)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            file_name = input("Enter the file name to delete: ")
            delete_file(file_name)

        elif choice == '4':
            file_name = input("Enter the file name to read: ")
            read_file(file_name)

        elif choice == '5':
            file_name = input("Enter the file name to edit: ")
            new_content = input("Enter the new content to append: ")
            edit_file(file_name, new_content)

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
