
#Gabriel Aboy
#Program uses string operations to convert any SINGLE word into Pyglatin
#PygLatin algorithm first letter cut past to end + add "ay"
pythpyg = 'ay'

original = raw_input('Enter a word:')#Gabriel
if len(original) > 0 and original.isalpha():#True
   word = original.lower()#makes raw_input lowercase
   first = word[0]# Equal to g
   new_word = word + first + pythpyg#gabrielgay
   new_word = new_word[1:len(new_word)]# Equal to 'abrielgay
   print new_word #prints abrielgay
else:
    print 'empty'
    #Error trap if raw_input doesnt meet if conditions
