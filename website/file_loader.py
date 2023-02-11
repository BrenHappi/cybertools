"""
Author: Happi
Version: 1.0
Description: Load a temporary file on a random endpoint on a website.
example : ./myScript.php -> /website/tmp-myScript-a5kSWtu0x5.php
"""
import subprocess
import argparse
import os

from typing import List


# PARAMS
parser = argparse.ArgumentParser()

authorized_ext = ["php", "txt"]
path = "/var/www/happi.com/public_html"
file: List[str]  # will get filename (ie: args.file) for processing it
parser.add_argument("-f", "--file", help=f"File to load on website. Authorized extension are : {authorized_ext}")
args = parser.parse_args()


# FUNC
def extract_filename(string):
    res = os.path.basename(string)
    res = res.replace('tmp.', '')
    return res


# assertion
try:
    if args.file is None:  # not empty
        raise Exception("File argument is required.")
    # process param
    file = args.file.split(".")
    filename = file[-2].split("/")[-1]
    ext = file[-1]
except Exception as e:
    print(e)
    print("Verify that the file provided is correct.")
    parser.print_help()
    exit(1)

try:
    if len(filename) > 100:  # size
        raise Exception("Filename too long.")
    elif ext not in authorized_ext:
        raise Exception(f"{ext} is not in {authorized_ext}.")
except Exception as e:
    print(e)
    parser.print_help()
    exit(1)

# MAIN THREAD

# create tmp file at $path
try:
    mktemp = subprocess.run(
        ["mktemp", "--suffix", f".{ext}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )
    output = mktemp.stdout.decode()
    output = output[:-1]  # remove CR LF & cie

    new_filename = extract_filename(output)

    new_file = f"{path}/tmp-{filename}-{new_filename}"

    mv = subprocess.run(
        ["mv", f"{output}", f"{path}/tmp-{filename}-{new_filename}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )
    # print(output, f"{path}/{filename}-{new_filename}")
except subprocess.CalledProcessError as error:
    print("error")
    print(f"Command failed with error code {error.returncode}")
    print(error.output.decode())
    exit(1)

# update the newly created file with the original file content
try:
    with open(args.file, 'r') as src:
        with open(new_file, 'w') as dst:
            dst.write(src.read())
except IOError as e:
    print("Cannot open/write in files:", e)

# set permissions
user_input = input("Do you want to make this file executable ? (y/n) ")
print(user_input)
try:
    # r/w permissions
    chmod = subprocess.run(
        ["chmod", "664", f"{new_file}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )
    print(chmod.stdout.decode())
    if user_input[:-1].lower() in ['y', 'n']:
        raise Exception("Incorrect value. Use \"y\" or \"n\".")
    # executable
    if user_input == 'y':
        executable = subprocess.run(
            ["chmod", "ugo+x", f"{new_file}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        print(executable.stdout.decode())

except Exception as e:
    print(e)
    parser.print_help()
    exit(1)

print(new_file)
