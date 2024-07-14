import datetime
# Function to create a text file with the current timestamp
def create_timestamp_file(filename):
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the timestamp to a file
    with open(filename, 'w') as file:
        file.write(current_timestamp)


# Function to read from a text file and display its content
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


# Example usage
create_timestamp_file('timestamp.txt')
read_file('timestamp.txt')
