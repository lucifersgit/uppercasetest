### References - 'https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase'
###              'https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard'

### User input string (text)
name = raw_input("Write your text to convert:\n")

### Print input string as option
option = raw_input("Select upper or lower for case change:\n")

### If the input option is lower, print lowercase; if input is upper, print uppercase

if option == "lower":
    print (name.lower())

elif option == "upper":
    print (name.upper())
