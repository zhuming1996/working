
class Calculator():
    def __init__(self,recordA,recordB,symbol):
        self.recordA = recordA
        self.recordB = recordB
        self.symbol = symbol
    def compute(self):
        if self.symbol == "+":
            a = self.recordA + self.recordB
        elif self.symbol == "-":
            a = self.recordA - self.recordB
        elif self.symbol == "*":
            a = self.recordA * self.recordB
        elif self.symbol == "/":
            a = self.recordA / self.recordB
        else:
            ex = print("请输入正确的计算符号")
            raise ex
        return a
try:
    jisuan = Calculator(3,4,"%")
    b = jisuan.compute()
    print(b)
except Exception as e:
    print(f"错误:{e}")
else:
    print("OK")