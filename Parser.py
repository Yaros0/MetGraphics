import re
import numpy

def last(list):
    if len(list) == 0: return None
    else: return list[-1]

class Dictionary:
    # Словарь операторов
    operators = {"+": (0, lambda a, b: a + b),
                 "*": (1, lambda a, b: a * b),
                 "/": (1, lambda a, b: a / b),
                 "%": (1, lambda a, b: a % b),
                 "^": (2, lambda a, b: a ** b),
                 }

    # Словарь функций
    functions = {"sin": lambda a: numpy.sin(a),
                 "cos": lambda a: numpy.cos(a),
                 "tan": lambda a: numpy.tan(a),
                 "cot": lambda a: numpy.cos(a) / numpy.sin(a),
                 }

    # Словарь констант
    consts = {"e": numpy.e,
              "π": numpy.pi,
              }


class Parser:
    def __init__(self, user_expr):
        self.user_expr = user_expr


    # def error(message):
    #     print(message)

    def check_user_expr(self):
        allowed_names = ["pi", "e", "sin", "cos", "tan", "x"]
        words = re.findall("[A-Za-z]+", self.expr)
        for i in range(len(words)):
            word = words[i]
            if word not in allowed_names: print('"' + word + '" не является функцией или константой')

    def simplify_user_expr(self):
        # Удаление лишних символов и превращение бинарного минуса в унарный
        self.user_expr = self.user_expr.replace(" ", "")
        self.user_expr = self.user_expr.replace("--", "+")
        self.user_expr = self.user_expr.replace("-", "+-")
        self.user_expr = self.user_expr.replace("++", "+")
        self.user_expr = self.user_expr.replace("*+", "*")
        self.user_expr = self.user_expr.replace("/+", "/")
        self.user_expr = self.user_expr.replace("%+", "%")
        self.user_expr = self.user_expr.replace("^+", "^")
        if self.user_expr[0] == "+":
            self.user_expr = self.user_expr[1:]

        # Замена констант
        for i in Dictionary.consts:
            self.user_expr = self.user_expr.replace(i, str(Dictionary.consts[i]))


    def calculate_user_expr(self, debug_mode: bool):
        minusize: int = 1

        i = 0
        stack = []
        rpn = []

        if debug_mode:
            print(f"expression: {self.user_expr}")
            print("analyzing...")
        #Анализ по символам
        while i < len(self.user_expr):
            #Обработка скобок
            #"(" сразу помещается в стек
            if self.user_expr[i] == "(":
                stack.append("(")
            #Все операторы в стеке идущие после "(" перемещаются в RPN
            elif self.user_expr[i] == ")":
                while stack[-1] != "(":
                    rpn.append(stack.pop())
                stack.pop()


            #Обработка цифр
            elif self.user_expr[i] in "-0123456789.":
                if self.user_expr[i] == "-" and self.user_expr[i+1].isalpha():
                    i += 1
                    minusize = -1
                    continue
                num: str = self.user_expr[i]
                while i+1 != len(self.user_expr) and self.user_expr[i+1] in "0123456789.":
                    i += 1
                    num += self.user_expr[i]
                rpn.append(float(num))


            #Обработка операторов
            elif self.user_expr[i] in "+*/%^":
                    while True:
                        #Если стек пуст просто добавляем оператор в него
                        if len(stack) == 0 or stack[-1] == "(":
                            stack.append(self.user_expr[i])
                            break
                        #Если приоритет последнего оператора в стеке выше тоже просто добавляем оператор в него
                        elif Dictionary.operators[self.user_expr[i]][0] > Dictionary.operators[stack[-1]][0]:
                            stack.append(self.user_expr[i])
                            break
                        #Если приоритет не выше, то убираем последний оператор из стека в RPN
                        else:
                            rpn.append(stack.pop())

            #Обработка функций и констант
            elif self.user_expr[i].isalpha():
                beggining = i
                func: str = self.user_expr[i]
                while self.user_expr[i] != "(":
                    i += 1
                    func += self.user_expr[i]
                func = func[:-1]
                i += 1
                inner_expr: str = self.user_expr[i]
                j = 1
                while True:
                    if self.user_expr[i] == "(":
                        j += 1
                    elif self.user_expr[i] == ")":
                        j -= 1
                        if j == 0: break
                    i += 1
                    inner_expr += self.user_expr[i]
                inner_expr = inner_expr[:-1]
                if inner_expr[0] == "+":
                    inner_expr = inner_expr[1:]
                if debug_mode:
                    print("inner expr", inner_expr)
                inn_pa = Parser(inner_expr)
                inner_number = inn_pa.calculate_user_expr(debug_mode)

                inner_number = float(Dictionary.functions[func](inner_number))
                inner_number *= minusize
                minusize *= minusize
                self.user_expr = self.user_expr[:beggining] + str(inner_number) + self.user_expr[i + 1:]
                if debug_mode:
                    print("inner_number -", inner_number)
                    print(f"new expression - {self.user_expr}")
                i = beggining-1

            if debug_mode:
                print(f"stack: {stack} \nrpn: {rpn} \n")
            i += 1

        if debug_mode:
            print("moving stack to rpn...")
        while len(stack) != 0:
            rpn.append(stack.pop())

        i = 0
        if debug_mode:
            print("calculating...")
        while len(rpn) != 1:
            if str(rpn[i]) in "+*/%^":
                if debug_mode:
                    print(rpn)
                rpn.insert(i-2, Dictionary.operators[rpn[i]][1](rpn[i-2], rpn[i-1]))
                rpn.pop(i+1)
                rpn.pop(i)
                rpn.pop(i-1)
                i -= 2
            i += 1

        return rpn[0]

#Тесты
# pa = Parser("-20^-1+-20")
# pa.simplify_user_expr()
# print(pa.calculate_user_expr(True))