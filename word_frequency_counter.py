#  With file
file_name = input('Enter the filename -> ')
try:
    file = open(file_name)
    d1 = dict()
    for line in file:
        words = line.split()
        for word in words:
            d1[word] = d1.get(word , 0) + 1
        print(d1)
except:
    print('file not found')

# by user
data = {}
text = input('enter some text -> ')
for word in text.split():
    data[word] = data.get(word,0)+1
words = sorted(data.keys())

for key in words:
    print('%s:%d'%(key,data[key]))