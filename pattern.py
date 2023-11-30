
star = "*"

nr_stars = 0
nr_lines = 8
max_stars = 5
add_star = 1
remove_star = -1


for x in range (nr_stars ,max_stars,):
    nr_stars += 1 
    print(nr_stars * star)

for y in range (nr_stars, max_stars,):
    max_stars -= 1
    print(max_stars * star)


    





""" if x in range ( 4, 8) :
        nr_stars -= 1
        max_stars -= 1
        print(star * (nr_stars) )
"""


        
"""    print(x * star) 

for y in range (0,4):
    z -= 1

    print(z * star)"""
        




