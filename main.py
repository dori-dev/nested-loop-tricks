"""We have a challenge to do
print all way answer this expression is 100
operator[o] = ["+" or "-" or " "]
"+" means total
"-" means submission
" " means nothings(1 " " 2 means 12)
1 o 2 o 3 o 4 o 5 o 6 o 7 o 8 o 9 = 100 
"""

operator = "+- "

# Interesting Solution !!!

# Code


# Bad Solution ✖✖✖
# we have 8 o so need 8 nested loop...
for j1 in operator:
    for j2 in operator:
        for j3 in operator:
            for j4 in operator:
                for j5 in operator:
                    for j6 in operator:
                        for j7 in operator:
                            for j8 in operator:
                                value = f"1{j1}2{j2}3{j3}4{j4}5{j5}6{j6}7{j7}8{j8}9"
                                # this replace for --> "1 2 + 4" => "12 + 4"
                                value = value.replace(" ", "")
                                if eval(value) == 100:
                                    print(f"{value} == 100")
