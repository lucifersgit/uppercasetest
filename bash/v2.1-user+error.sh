#!/bin/bash

### References: https://www.linuxnix.com/shell-scripting-convert-a-string-from-lowercase-to-uppercase/

### This is where the user will input the desired case format,
### and the output will be in the desired string maniplulation:

VAR1=AbcdefGhijklmnOPqrSTuvwxyz

echo "Please state output case type - write 'lower' for lowercase, or 'upper' for uppercase:"
read userinput

### If userinput is 'lower' or 'Lower', output is lowercase (via string manipulation):
	if [[ $userinput == "lower" || $userinput == "Lower" ]]; then
		echo ${VAR1,,}

### If userinput is 'upper' or Upper', output is uppercase (via string manipulation):
	elif [[ $userinput == "upper" || $userinput == "Upper" ]]; then
       		echo ${VAR1^^}

### Litle bit of an error output for 'junk' input - prints output, then exists:
	else
		echo "That is not a valid input - try again"
fi
