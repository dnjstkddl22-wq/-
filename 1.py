a = 3
b = 4
print(a + b)
print("Hi" * 5)
print("-" * 80)


t1 = 'python'
t2 = 'java'

t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: " + name1 + " 나이: " + str(age1))
print("이름: " + name2 + " 나이: " + str(age2))

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

data = "   삼성전자    "

data1 = data.strip()
print(data1)
data2 = data.strip()
print(data2)
data3 = data.strip()
print(data3)

ticker = 'btc_krw'
ticker1 = ticker.upper()
print(ticker1)

a = "hello"
a = a.capitalize()

