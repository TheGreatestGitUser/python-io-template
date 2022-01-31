import sys

all_input = sys.stdin.read().split('\n')
print = sys.stdout.write # this makes the "print()" function much faster
			 # and it makes the code more readable.

# Can add .strip() to the first two methods below before the .split(),
# however the code doesn't already come with it in order to save time.
# Note that .strip() works the exact same as .trim() in Java.

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
print(s + '\n')
print(str(n) + '\n')

# Tt is important to note that if you want to make this code faster, you can
# always use a different compiler, such as PyPy instead of Python. However, note
# that some compilers may use more (maybe even much more) memory than others.

# If you want to save on memory, then you could use the sys.stdin.readline()
# function to read each line instead of reading all of them and then storing
# them in one big string array. Note that this will take a bit longer to run,
# but you will save a significant amount of memory. Also note that you can say
# "input = sys.stdin.readline" and then use "input()" to read each line. This
# re-map of the value of the input() function makes it simpler to use, cleaner
# to use, and much faster.