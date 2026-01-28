s = input("Enter a string: ")
print(s[::-1])
temp = (s[::-1])
if s == temp:
    print("palindrone")
else:
    print("no")     

count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)   
  
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)  

           