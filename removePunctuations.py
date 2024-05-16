# Define a string of punctuation characters
punctuation = "!,.? "

# Define the original string
original_string = "Hello, world! How are you today?"
print("The original string is:", original_string)

# Initialize an empty string to store the filtered string
string_without_punctuation = ""

# Iterate through each character in the original string
for char in original_string:
    # Check if the character is not in the punctuation string or if it's a space
    if char not in punctuation or char == ' ':
        string_without_punctuation += char  # Append non-punctuation characters to the filtered string

# Print the string after removing punctuations
print("The string after punctuation filter:", string_without_punctuation)
