def get_operand_by_index(list_elements, index):
  """
      (list, int) -> float or None

      Function get operand by index from expression (while for two operands, maybe in the future will be more operands)

  """
  if index not in (1, 2):
    return

  try:
    operand_string = list_elements[index]
    # print(f"операнд {index} = {operand_string}")
  except IndexError:
    print(f"Не введены требуемые данные, а именно \"операнд №{index}\"")
    return None

  try:
    operand = float(operand_string)
  except ValueError:
    print(f"\"{operand_string}\" не является числом")
    return None
  return operand

def execute(input_string):
  """
    (string) -> int or float or None

    Function executes the command

  """

  # Cutting spaces on the left and right sides of input string
  input_string = input_string.strip()

  if len(input_string) == 0:
    print("Введенная строка пуста.")
    return

  # Delete double spaces in the input string
  while input_string.find('  ') > 0:
    input_string = input_string.replace('  ', ' ')

  string_list = input_string.split(" ")

  # Checking on amount elements of expression
  if len(string_list) > 3:
    print("В выражении найдено более 3-х параметров.")
    return

  # Geting and checking elements of expression
  operation_string = string_list[0]
  if len(operation_string) > 1:
    print("Операция должна состоять из одного символа либо '+' либо '-' либо '*' либо '/'.")
    return
  else:
    # Checking operation string
    # operation must be only these + or - or * or /
    try:
      assert operation_string in ('+', '-', '*', '/')
    except AssertionError:
      print("Операция должна быть либо '+' либо '-' либо '*' либо '/'")
      return

    operand1 = get_operand_by_index(string_list, 1)
    # print(operand1)
    if operand1 != None:
      operand2 = get_operand_by_index(string_list, 2)
      if operand2 == None:
        return
    else:
      return

  # Checking on negatives valuse
  if operand1 < 0:
    print(f"Операнд №1 не является положительным числом.")
    return
  elif operand2 < 0:
    print(f"Операнд №2 не является положительным числом.")
    return

  # All input are correct

  # Execute operation
  if operation_string == '+':
    result = operand1 + operand2
  elif operation_string == '-':
    result = operand1 - operand2
  elif operation_string == '*':
    result = operand1 * operand2
  elif operation_string == '/':
    try:
      result = operand1 / operand2
    except:
      print("Предупреждение: деление на ноль.")
      return

  result_int = int(result)
  if (result_int == result):
    return result_int
  else:
    return round(result, 4)

def main():
  """
    (None) -> None

    Main function which organizes a dialog with user

  """
  print("Для выхода из программы введите \"q\".")
  while (1):
    input_string = input("Введите выражение через пробел в формате (\"операция(+ - * /)\" \"операнд1\" \"операнд2\"): ")

    if input_string != 'q':
      print(f"Результат: {execute(input_string)}")
    else:
      break

def test():
  """
    (None) -> None

    Function which organizes a many tests for this code

  """
  test_expressions = ('', '+', '+ 1', '+ 1 2', '+1 2', '+12', '+12', '1 1 2', 'f 1 2', '/ 0 0', '/ 0 1', '/ 345 -5', '- 7 8 8 8',
                    '- a 2', '+ 1 a', '+a', '+ dv', '+  345634  34534', '+    5    5', '3 dh')
  for expression in test_expressions:
    print(f"Входные данные: \"{expression}\"")
    print(f"Результат работы функции: {execute(expression)}", end="\n\n")

main()
# test()