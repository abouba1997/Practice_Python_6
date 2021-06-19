from random import sample, shuffle, choice
from string import ascii_letters, digits

#1
def bingo_loto_gen():
    gen_row = sample(range(1, 76), 25)
    res = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(gen_row[j + i * 5])
        res.append(row)
    res[2][2] = 0
    return res

#2
def russian_loto_gen():
    gen_row = sample(range(1, 91), 15)
    res = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(gen_row[j + i * 3])
        for j in range(3, 9):
            row.append(0)
        shuffle(row)
        res.append(row)
    
    return res

#3
def generate_password(m): # generate password from 4 caracters to 20 caracters (included) 
    if m > 3 and m < 21:
        r = ascii_letters + digits
        return "".join(choice(r) for _ in range(m))
    else:
        return "Can't generate that king of passowrd"

#4
def generate_list_of_passwords(n, m):
    res = list()
    if n > 0 and m > 3 and n < 1000 and m < 21:
        while n > 0:
            k = generate_password(m)
            if k not in res:
                res.append(k)
            else:
                n += 1
            n -= 1
        return res
    else:
        return "Can't generate the passwords"


print("\n********************* Test Case *********************\n")
print("Bingo Loto Generator", end='\n\n')
print(*bingo_loto_gen(), sep='\n')
print("\n\nRussian Loto Generator", end='\n\n')
print(*russian_loto_gen(), sep='\n')
print("\n\nPassword Generated", end='\n\n')
print('Password : ', generate_password(20))
print("\nList of Passwords Generated", end='\n\n')
print(*generate_list_of_passwords(10, 4), sep='\n')