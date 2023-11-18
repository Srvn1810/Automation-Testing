# 1.Write a python program using function to which will do the Following:-
# a.) The function will create a text file with the current timestamp
# b.) The file content should have the content of the current stamp

import datetime

def create_text_file_with_timestamp():
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"output_{current_timestamp}.txt"
    with open(file_name, 'w') as file:
        file.write("The function will create a text file with the current timestamp !")
    print(f"File '{file_name}' created with the current timestamp.")
create_text_file_with_timestamp()

# 2.)Write another python function to read from a text file, the function will take the name of
# the text file and display the content of file into the console
def read_and_display_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print(f"Content of file '{file_name}':\n{file_content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
read_and_display_text_file('output_2023-11-18_16-30-12.txt')
