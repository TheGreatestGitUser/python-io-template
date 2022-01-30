import sys

all_input = sys.stdin.read().split('\n')

# The two lines of code below are there just to copy/paste to reduce
# the amount of time spent typing code.
#sys.stdin.readline()
#sys.stdout.write()


# Can add .strip() to the first two methods before the .split(), however
# the code doesn't already come with it in order to save time. Note that
# .strip() works the exact same as .trim() in Java.

# Note that the functions below aren't used because all of the standard
# input is in the "all_input" variable

def get_ints(): return map(int, sys.stdin.readline().split())
def get_ints_list(): return list(map(int, sys.stdin.readline().split()))
def print_list(outputted_list): sys.stdout.write(" ".join(map(str,outputted_list)) + '\n')

# the function "print_list" is used to write a bunch of integers all on
# one line, each one separated from the other by one line, such as "1 2 3 4 5".


n = int(all_input[0])
for i in range(1, n + 1):
    strsplit = all_input[i].split()

# this is for an example where you have the first line with value "n"
# and the next n lines have space separated values that you want to
# access. If you want to access them as integers, then you can always
# use map(int, all_input[i].split()) or list(map(int, all_input[i].split()))

s = "" # this is just a blank string that is used as an example to show how
       # string output works
sys.stdout.write(s + '\n')
sys.stdout.write(str(n) + '\n')