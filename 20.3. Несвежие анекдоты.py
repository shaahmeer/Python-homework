def print_only_new(message):
   global arr
   if message not in arr:
       print(message)
       arr.append(message)

arr = []
print_only_new("Шутка номер 5")
print_only_new("Шутка номер 23")
print_only_new("Шутка номер 10")
print_only_new("Шутка номер 9")
print_only_new("Шутка номер 5")
print_only_new("Шутка номер 400")
print_only_new("Шутка номер 23")