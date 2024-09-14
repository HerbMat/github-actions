import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM")
github_output = os.getenv("GITHUB_OUTPUT")
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
    num = 1

# to set output, print to shell in following syntax
with open(github_output, 'a') as output_file:
    output_file.write(f'num_squared={num ** 2}\n')
