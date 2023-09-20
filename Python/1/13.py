text = input('enter a text with one space:')
text  = reversed(text.split(" "))
for i in text:
    print(i, end = ' ')