# read documents
# Open the text file for reading
with open('20newsgroups_subset.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Split the content into a list using the delimiter "~~~"
    my_list = content.split("~~~")

# Print the resulting list
print(my_list[0])

# if __name__ == '__main__':
#     pass