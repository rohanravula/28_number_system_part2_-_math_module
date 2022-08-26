from fractions import Fraction as f


# print(f(6,2)) #3 .  by this we can know the  6/2 is fraction of the 3.
# print(f(122.5)) #245/2. By this we can know that the 122.5 is fraction of the 245/2.
# print(f("122.5")) #245/2. we can keep in single quotes or dubble quotes also.

# a=2+8j
# print(a,type(a)) #(2+8j) complex
# print(a.real) #2.0 the answer is shown in float
# print(a.imag) #3.0 the amswer is showm in float

" ** when their are 2 star symobles then it is known as the power "

# print(4*5) #20 . when it has single star then it is known as the multiplication i,e 4*5=20
# print(2**3) #8 . 2*2*2=8
# print(1.5**2) #2.25

"L.C.M"
# import math as l

# print(l.lcm(8,14))#56 . this is to check weather we got the LCM answer is correct or not which we done in maths
# print(l.lcm(12,18)) #36

"G.C.D"

# print(l.gcd(24,32)) #8
# print(l.gcd(28,48)) #4

"prod" "whcih means product which means multiplicaiton of myltiple number this method is used"

# import math as p

# a=1,2,3,4,5 
# print(p.prod(a)) #1*2*3*4*5=120

"factorial" "whcih means muliiplication of reverse"
 
# import math as f

# print(f.factorial(5)) #120  .which means 5*4*3*2*1=120
# print(f.factorial(8)) #40320 . which means 8*7*6*5*4*3*2*1=40320

"abs" "absuluate value which means it will remove the negative value and gives the postive value"
# print(abs(-5)) #5
# print(abs(-9+6)) #3 . actual answer is -3 but it has removed the negaitve symbole so the answer will give us in positive value  only.

"fabs" "which means the answer will remove the negative value but the answer is represented in terms of float"

import math as fa

print(fa.fabs(-8+10)) #