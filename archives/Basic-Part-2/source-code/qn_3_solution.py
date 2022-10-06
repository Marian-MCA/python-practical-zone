import re
print("Input number of data sets:")
class c(int):
    def __add__(self,n):
        return c(int(self)+int(n))
    def __sub__(self,n):
        return c(int(self)-int(n))
    def __mul__(self,n):
        return c(int(self)*int(n))
    def __truediv__(self,n):
        return c(int(int(self)/int(n)))
   
for _ in range(int(input())):
  print("Input an expression:")
  print(eval(re.sub(r'(\d+)',r'c(\1)',input()[:-1])))
