# PASSWORD GENERATOR 

password_gen.py is a script that generates a series of passwords using random words combined with alphanumeric characters. 

## Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies. 

pip install colorama

pip install random-word

## Usage

<code> passwd_gen.py -n number -ll lower_limit -ul upper_limit -l length </code>
                     
NOTE: lower_limit must be less than upper_limit 

## Example 

passwd_gen.py -n 10 -ll 19999 -ul 99999 -l 64

## Note

The passwd_test.py script is included for test purposes and uses hard-coded values for number, lower_limit, upper_limit, and random_string_length variables. 
