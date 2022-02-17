remainders5 = [i**2 % 5 for i in range(1,101)]
print(remainders5)

remainders11 = [i**2 % 11 for i in range(1,12)]
print(remainders11)

#when you look at the reminders when you divide by a prime number (p) for range(0, p+1),
# the len(remainders_p) = (p+1)/2. when you divide by 11 you get 6 remainders. The problem about finding which
#problems appear on the list is a complex puzzle from number theory known as quadratic reciprocity.

