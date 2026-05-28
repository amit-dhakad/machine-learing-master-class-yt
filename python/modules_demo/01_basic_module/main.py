# main.py - Demonstrating direct import of custom module
import calculator   # Looks for calculator.py in the current directory

sum_res = calculator.add(12, 8)
diff_res = calculator.subtract(25, 5)

print("Sum:", sum_res)
print("Diff:", diff_res)
print("Author:", calculator.author)
