#Problem J3: The Smart Security Keypad

#You are testing a smart security lock that takes a password string consisting of alphanumeric
#characters. The system evaluates the password by checking adjacent pairs of characters:
#1) If both characters in a pair are of the same type (either both letters or both digits), they form a stable pair.
#2) If one character is a letter and the other is a digit, they form an unstable pair.
#Your task is to calculate the total number of unstable pairs in a given password string.

#Input Specification
#A single line containing a string $S$, where the length of the string $N$ satisfies $2 \le N \le 100$.
#The string contains only uppercase letters (A–Z), lowercase letters (a–z), and digits (0–9). 

#Output Specification
#Output a single integer representing the total number of unstable pairs in the string.

#Code:
n = input()
ans = 0

for i in range(len(n) - 1):
    q = [n[i], n[i+1]]

    if q[0].isdigit() and q[1].isalpha():
        ans += 1
    elif q[0].isalpha() and q[1].isdigit():
        ans += 1
print(ans)