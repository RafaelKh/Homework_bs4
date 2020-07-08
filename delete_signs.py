import unicodedata

text_data = [
'Test!!!! hello. esim. test2...',
'100% ola!! #HashTag',
'testText???!!?'
]

new_list = ['', '', '']
for i in range(len(text_data)):
    for j in range(len(text_data[i])):
        if unicodedata.category(text_data[i][j])[0] != 'P':
            new_list[i] += text_data[i][j]
print(new_list)
