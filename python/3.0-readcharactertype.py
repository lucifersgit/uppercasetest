### References - 'https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase'
###              'https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard'

### User input string (text)
name = raw_input("Write your text to confirm if it is uppercase or lowercase:\n")

### Determine if string is uppercase or lowercase, and print corresponding output:

if name.isupper():
    print "This is an uppercase word"

elif name.islower():
    print "This is a lowercase word"

### If characters are mixed, print error:

else:
    print "Invalid type - mixed character cases"
