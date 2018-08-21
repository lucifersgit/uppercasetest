#!/bin/bash

### Declare 'VAR1' as a string of letters (i.e. alphabet)

VAR1=abcdefghijklmnopqrstuvwxyz

### Convert lowercase to uppercase using string manipulation (https://www.linuxnix.com/shell-scripting-convert-a-string-from-lowercase-to-uppercase/) 

VAR2=${VAR1^^}

echo $VAR2
