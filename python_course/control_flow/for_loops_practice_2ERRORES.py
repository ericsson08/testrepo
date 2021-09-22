#exercise for loop:

#1 For loop print

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)


#2 Creat multiple of 5

for number in range(5,31,5):
    print(number)

#3 Creating a new list

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

usernames = []

for name in names:
    usernames.append(name.lower().replace(" ","_"))
print(usernames)

#porque no puedo poner un #usernames = """" #ERROOOOOORRRRRR#

#4 Modifying a list

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in range(len(names)):
    names[name] = names[name].lower().replace(" ", "_")
print(names)


#5 Tag Counter

tokens = ["<caca>", "pipi", "<culo>", "pedo", "pis"]

counter = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        counter  +=1
print(counter)

#6 HTML list ERRRROOOOORRRR

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)





# Create an HTML list
