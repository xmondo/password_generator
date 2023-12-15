# PASSWORD GENERATOR 

password_generator_opts.py is a script that generates a series of passwords using random words combined with alphanumeric characters. 

## Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies. 

pip install colorama

pip install random-word

## Usage

passwd_generator_opts.py number_of_passwords lower_limit upper_limit random_string_length
                     
NOTE: lower_limit must be less than upper_limit 

## Example 

passwd_generator_opts.py 10 19999 99999 64

## Note

The passwd_generator.py script is included for test purposes and uses hard-coded values for lower_limit, upper_limit, and random_string_length variables. 
