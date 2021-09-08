# Import whatever

# Get the secrets
secretsFile = open("secrets.txt", "r")

data = secretsFile.readlines()

def get_data_from_line(str: str, separator: str = " "):
    arr = str.split(" ")
    arr.pop(0)

    separator = separator.join(arr)

    return separator.strip()

admission_number = get_data_from_line(data[0])
password = get_data_from_line(data[1])

print(admission_number)

print(password)

# Logic Stuff
