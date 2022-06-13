a = 'Введите первое число: '
b = 'Введите второе число: '
oper = 'Выберите операцию из следующих +-*/%**// : '
res = 'Ответ:'
miss = 'Данной операции нет в системе'
a1 = float(input(a))
b1 = float(input(b))
operation = input(oper)
if operation == '+':
  print (res, a1 + b1)
elif operation == '-':
  print (res, a1 - b1)
elif operation == '*':
  print (res, a1 * b1)
elif operation == '/':
  print (res, a1 / b1)
elif operation == '%':
  print (res, a1 % b1)
elif operation == '**':
  print (res, a1 ** b1)
elif operation == '//':
  print (res, a1 // b1)
else:
  print (miss)