### References - 'https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase'
###              'https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard'

### User input string (text)
name = raw_input("Write your text to convert:\n")

### Determine if string is uppercase, and print corresponding output. If characters are mixed, print error

if name.isupper():
    print "This is an uppercase word"

elif name.islower():
    print "This is a lowercase word"

else:
    print "Invalid type - mixed characters"
