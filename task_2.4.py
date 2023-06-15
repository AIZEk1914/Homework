# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

foo = "Hi! Hello!, Oh, no!!!"
new_foo = foo.replace("!", "")  
print(new_foo)

# Пункт B.S
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

remove = "Hi!"
result_str = "" 
for i in range(0, len(remove)): 
    if i != 2: 
        result_str = result_str + remove[i] 

print ("Строка после удаления i-го элемента: " + result_str)

# def remove_last_em(s):
#     if s[-1] == '!':
#         bc = s[:-1]
#     else:
#         bc = s
#     return bc

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# def remove_word_with_one_em(s):
#     pass