from zlib import Z_HUFFMAN_ONLY

HOURS = int(input('Enter number of hours you worked this week: '))
NORMAL_RATE = 51.45
OVERLOAD_RATE = 88.9

if HOURS > 35 :
    PAYMENT = (35 * NORMAL_RATE) + (HOURS - 35) * OVERLOAD_RATE
else :
    PAYMENT = HOURS * NORMAL_RATE
print(f'This weekly payment is: {PAYMENT} dollars')


print("HazelZhu, z5313486")
numbers = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
temp_largest = numbers[0]
print('Before', temp_largest)
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest value is {temp_largest}')


