
##1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

thirty = "Thirty"
days = "Days"
of = "Of"
py = "Python"
space = " "
Tdop = thirty + space + days + space + of + space + py
print(Tdop)

##2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

cdng = "Coding"
F = "For"
All = "All"
space = " "
CDA = cdng + space + F + space + All
print(CDA)

##3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

##4. Print the variable company using _print()_.

print(company)

##5. Print the length of the company string using _len()_ method and _print()_.

length_company = len(company)
print(length_company)

##6. Change all the characters to uppercase letters using _upper()_ method.

print(company.upper())

##7. Change all the characters to lowercase letters using _lower()_ method.

print(company.lower())

##8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.

print(company.capitalize())
print(company.title())
print(company.swapcase())

##9. Cut(slice) out the first word of _Coding For All_ string.

pany = company[7:14]
print(pany)

##10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.

comp = "Coding"
print(company.find(comp))

##11. Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python'))

##12. Change Python for Everyone to Python for All using the replace method or other methods.

change = "Python for Everyone"
print(change.replace('Everyone', 'All'))

##13. Split the string 'Coding For All' using space as the separator (split()) .

print(company.split( ))

##14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

sv = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sv.split(','))

##15. What is the character at index 0 in the string _Coding For All_.

co = company[0]
print(co)

##16. What is the last index of the string _Coding For All_.

ny = company[-1]
print(ny)

##17. What character is at index 10 in "Coding For All" string.

com10 = company[10]
print(com10)

##18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

py = change[0:2]
cort = "4"
every1 = change[-8:-3]
print(py + space + cort + space + every1 + "1")

##19. Create an acronym or an abbreviation for the name 'Coding For All'.

cod = company[0:3]
f = '4'
all = company[-3:-1]
print(cod + space + f + space + all)

##20. Use index to determine the position of the first occurrence of C in Coding For All.

C = "C"
print(company.index(C))

##21. Use index to determine the position of the first occurrence of F in Coding For All.

Fo = "F"
print(company.index(Fo))

##22. Use rfind to determine the position of the last occurrence of l in Coding For All People.

Cdoa = "Coding For All People"
print(Cdoa.rfind("l"))

##23. Use index or find to find the position of the first occurrence of the word 'because' 
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

##24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'


