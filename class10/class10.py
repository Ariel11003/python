d={}
n=int(input("input number:"))
for i in range(n):
    k=input("input key:")
    v=input("input value:")
    d[k]=v
    print(d)

c=input("input del key")
a=d.pop(c,'哈哈哈哈沒東西')
print(f"移除:{a}")

for key,v in d.items():
    print(f'{key}={v}')

s=input("input seach key:")
if s in d:
    print(True)
else:
    print(False)
