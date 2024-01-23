import numpy as np
import matplotlib.pyplot as plt

#The following three variables can be changed
mod = 10
#"mod" must be a postive integer
gen1 = 1
#"gen1" must be a non-negative integer STRICTLY less than "mod"
gen2 = 5
#"gen2" has the same restrictions as "gen1"

#The following code checks that the restrictions are met, and that 'mod' isn't too large (mostly for completeness)
if isinstance(mod, int) == False:
    print ("Error: 'mod' must be a positive integer. To avoid errors and nonsensical results, 'mod' has been rounded to the nearest integer.")
    mod = round(mod)
if mod<0:
    print ("Error: 'mod' must be a positive integer. To avoid errors and nonsensical results, the minus sign in 'mod' has been removed.")
    mod = -mod
if mod == 0:
    print("Error: 'mod' cannot be 0. To avoid errors and nonsensical results, you will be shown the zero chain.")
    mod = 1
    gen1 = 0
    gen2 = 0
if isinstance(gen1, int) == False:
    print ("Error: 'gen1' must be an integer. To avoid errors and nonsensical results, 'gen1' has been rounded to the nearest integer.")
    gen1 = round(gen1)
if isinstance(gen2, int) == False:
    print ("Error: 'gen2' must be an integer. To avoid errors and nonsensical results, 'gen2' has been rounded to the nearest integer.")
    gen2 = round(gen2)
if gen1<0 or gen1 >= mod:
    print ("Error: 'gen1' must be at least 0 and strictly less than 'mod'. To avoid errors and nonsensical results, you will be shown the chain where 'gen1' =", gen1 % mod)
    gen1 = gen1 % mod
if gen2<0 or gen2 >= mod:
    print ("Error: 'gen1' must be at least 0 and strictly less than 'mod'. To avoid errors and nonsensical results, you will be shown the chain where 'gen1' =", gen1 % mod)
    gen2 = gen2 % mod
if mod>=100 and mod<1000:
    print("Warning: Your value for 'mod' is quite large. This process may take a few seconds, and may not produce a full chain.")
if mod>=1000 and mod<10000000000000:
    print("Warning: Your value for 'mod' is extremely large. This process may not complete for a very long time, is unlikely to produce a full chain, and may result in a memory error. Consider using a smaller value for 'mod'.")
if mod>=10000000000000:
    print("Warning: Why on earth did you pick a value this large??? You deserve whatever error you get.")
      
#Setting up values and arrays
Nmax = mod*mod + 5
#(This value was chosen to make sure the chain would loop by this point)
n = np.arange(1, Nmax)
hplot = np.zeros_like(n)
hplot[0] = gen1
hplot[1] = gen2

#This code calculates the chain
for N in np.arange(2, int(Nmax)-1):
    hplot[N] = (hplot[N-1] + hplot[N-2]) % mod

#The code below checks for repitions in the chain, to make it easier to see how long the chain is before repition
check1 = hplot[0]
check2 = hplot[1]
k = 1
while k<int(Nmax)-2:
    for N in np.arange(k, int(Nmax)-2):
        if hplot[N] == check1 and hplot[N+1] == check2:
            for P in np.arange(N+2, int(Nmax)-1):
                hplot[P] = 0
            k = Nmax-3
    check1 = hplot[k]
    check2 = hplot[k+1]
    k = k+1
    
#This code calculates the length of the chain before it repeats
q = 1
leng = Nmax+5
while q<leng:
    if hplot[q] == 0 and hplot[q+1] == 0:
        leng = q
    else: q = q+1

#This checks if "gen2" = 0. If it is, leng needs to be 1 larger, to avoid deleting too many zero elements
if gen2 == 0:
    leng = leng+1

#This code shortens the chain to just after the loop
m = np.arange(1, leng+1)
finalchain = np.zeros_like(m)
x = 0
while x<leng:
    finalchain[x] = hplot[x]
    x = x+1

#This prints the results
print ("The chain with generators", gen1, "and", gen2, "with addition modulo", mod, "is:")
print (finalchain)
if hplot[0] == hplot[1] == 0:
    print ("The length of this chain is 1.")
else: print ("The length of this chain is", leng-2, "(although", leng, "elements were displayed for clarity).")
