"""We have a challenge to solve
print all way calculate the expression is 100
operator[o] = ["+" or "-" or " "]
"+" means total
"-" means submission
" " means nothings(1 " " 2 means 12)
1 o 2 o 3 o 4 o 5 o 6 o 7 o 8 o 9 = 100
"""

from itertools import product

OPERATOR = "+- "


print("---------------- Smart-Solution ----------------")

# Smart Solution ✔✔✔
# We can use itertools.product(iter, repeat=int)

for j1, j2, j3, j4, j5, j6, j7, j8 in product(OPERATOR, repeat=8):
    expression = f"1{j1}2{j2}3{j3}4{j4}5{j5}6{j6}7{j7}8{j8}9"
    # this replace for --> "1 2 + 4" => "12 + 4"
    expression = expression.replace(" ", "")
    if eval(expression) == 100:
        print(f"{expression} == 100")


print("---------------- Interesting-Solution ----------------")

# Interesting Solution !!!
# we have 8 o so need 8 nested loop
# we can make a list with 2 nested loop and
# use list in 4 nested loop (2*4 == 8)

two_nested_loop = [(i, j) for i in OPERATOR for j in OPERATOR]

for j1, j2 in two_nested_loop:
    for j3, j4 in two_nested_loop:
        for j5, j6 in two_nested_loop:
            for j7, j8 in two_nested_loop:
                expression = f"1{j1}2{j2}3{j3}4{j4}5{j5}6{j6}7{j7}8{j8}9"
                # this replace for --> "1 2 + 4" => "12 + 4"
                expression = expression.replace(" ", "")
                if eval(expression) == 100:
                    print(f"{expression} == 100")


print("---------------- Bad-Solution ----------------")

# Bad Solution ✖✖✖
# we have 8 o so need 8 nested loop...

for j1 in OPERATOR:
    for j2 in OPERATOR:
        for j3 in OPERATOR:
            for j4 in OPERATOR:
                for j5 in OPERATOR:
                    for j6 in OPERATOR:
                        for j7 in OPERATOR:
                            for j8 in OPERATOR:
                                expression = f"1{j1}2{j2}3{j3}4{j4}5{j5}6{j6}7{j7}8{j8}9"
                                # this replace for --> "1 2 + 4" => "12 + 4"
                                expression = expression.replace(" ", "")
                                if eval(expression) == 100:
                                    print(f"{expression} == 100")
