### References - 'https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase'
###              'https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard'

### User input string (text)
name = raw_input("Write your text to convert:\n")
print " "

### Print input string as option
option = raw_input("Type 'lower' or 'upper' for corresponding case change:\n")
print " "

### If the input option is lower, print lowercase; if input is upper, print uppercase
print "Output:"
if option == "lower":
    print (name.lower())

elif option == "upper":
    print (name.upper())
