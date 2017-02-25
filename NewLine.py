x = 'There is a dog and fox fighting in the park and there is an apple falling down.'

x = x.split(' ')#insert veriable 

for i,word in enumerate(x):
    if i != 0 and i % 3 == 0:
        x[i] = word + '\n'

print ' '.join(x)
