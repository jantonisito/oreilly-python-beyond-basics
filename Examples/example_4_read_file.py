"""
Read a file with a number on each line. Print the sum of those numbers.
"""
sum_ = 0 #to avoid name clash
with open('data/input.txt') as file:
    print(file.read())
    print("read again")

    # need to rewind thew cursor
    file.seek(0)
    print(file.read())

    file.seek(0)
    for line in file.readlines():
        sum_ += int(line)

print(f"The sum was {sum_}")
