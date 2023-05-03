import hashlib


text = "Hello world"



result = hashlib.sha3_256(text.encode())


print("The SHA256 is :",result.hexidigest())
import hashlib

text1 = "Jhon gave 10 dollars"
result = hashlib.sha3_256(text1.encode)
print("The SHA256 of text 1 is : ",result.hexidigest())

text2 = "Bob gave 5 dollars to Jhon"
result = hashlib.sha3_256(text2.encode())
print("The SHA256 of text 2 is : ",result.hexidigest())

text3 = "Jhon gave 5 ddollars to Bob on 13 October"
result = hashlib.sha3_256(text3.encode())
print("The SHA256 of text 3 is : ",result.hexidigest())

text4 = "Bob gave 10 dollars to Jhon on 16 October"
result = hashlib.sha3_256(text4.encode())
print("The SHA256 of text 4 is : ",result.heidigest())

text5 = "Jhon gave 100 dollars to Alex"
result = hashlib.sha3_256(text5.encode())
print("The SHA256 of text 5 is : ",result.heidigest())

text6 = "Bob gave Jhon 300 dollars"
result = hashlib.sha3_256(text6.encode())
print("The SHA256 of text 6 is : ",result.heidigest())

text7 = "Alex gave 600 dollars to Jhon"
result = hashlib.sha3_256(text7.encode())
print("The SHA256 of text 7 is : ",result.heidigest())

text8 = "Bob gave Jhon 900 dollars"
result = hashlib.sha3_256(text8.encode())
print("The SHA256 of text 8 is : ",result.heidigest())

text9 = "Alex gave Bob 1000 dollars"
result = hashlib.sha3_256(text9.encode())
print("The SHA256 of text 9 is : ",result.heidigest())

text10 = "Jhon gave 1500 dollars to Bob"
result = hashlib.sha3_256(text10.encode())
print("The SHA256 of text 10 is : ",result.heidigest())

root.mainloop()