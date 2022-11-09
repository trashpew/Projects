print("What should we summate to:")
sum_end = int(input())
print("Choose two factors which will be in all numbers we summate "
      "(I.E, 3 and 5 would summate all numbers with either as a factor up to {}): \n\n".format(sum_end))

print("Factor 1:")
f1 = int(input())
print("Factor 2:")
f2 = int(input())

last = 0
for i in range(sum_end - 1):  # [1]
    i = i + 1
    if (i % f1) == 0 or (i % f2) == 0:
        last = last + i
        continue
print(last)

'''
1: The range needs to be one less than sum_end, since we want up to it but not including it.

This code is really simplistic but the directions might be confusing.

It stems from the question: "What is the sum of all numbers
less than 1000 that have 3 or 5 as factors?"

Inputting 3 and 5 as our factors outputs that answer.

If you don't get it, might I recommend experimenting a bit.
''' 
 
