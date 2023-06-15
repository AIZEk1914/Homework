def quarter_of(mon):
    quarter_of = {
        'Ноль': [0],
        'Один': [1], 
        'Два': [2],
        'Три': [3],
        'Четыре': [4],
        'Пять': [5],
        'Шесть': [6],
        'Семь': [7],
        'Восемь': [8],
        'Девять': [9],
       
        }
        
    for i in quarter_of.keys():   
        if mon in quarter_of[i]:  
            return i

print( quarter_of(6)) 