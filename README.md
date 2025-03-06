# Factorial Calculator (Python)

Welcome to the **Factorial Calculator** repository! This mini project demonstrates a simple, **recursive** approach to computing the factorial of a positive integer in Python.

## Overview

- **Function Name**: `factorial(num)`
- **Core Logic**: Recursively multiplies `num` by `factorial(num - 1)`.
- **User Input**: Prompts the user to enter a positive integer.
- **Output**: Prints the factorial of the entered number in the format:  
  \`\`\`
  [num] ! = [factorial_value]
  \`\`\`

## What is Factorial?

In mathematics, the factorial of a positive integer *n*, denoted by *n!*, is the product of all positive integers less than or equal to *n*. Formally:
\[
n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1
\]
For example:
- \(1! = 1\)
- \(2! = 2\)
- \(3! = 6\)
- \(4! = 24\)

## How It Works

1. **Input**: The program prompts you to enter a positive integer (e.g., 5).
2. **Recursive Function**:
   - If the number is 1, the function returns 1.
   - Otherwise, it returns \(`num * factorial(num - 1)`\).
3. **Result**: The factorial of the number is printed to the screen.

## Code Snippet

```python
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Kérem a pozitív egész számot: "))
print(num, "!", "=", factorial(num))
```

## Usage

1. **Clone or Download** this repository (or simply copy the code).
2. Ensure you have **Python 3** installed on your system.
3. Open a terminal or command prompt in the directory containing the `factorial.py` file.
4. Run the script:
   ```bash
   python factorial.py
   ```
5. When prompted, enter a positive integer. The program will then display the factorial of the number.

## Notes & Limitations

- **Recursion Limit**: Python has a default recursion depth limit. Very large inputs (usually above a few thousand) might cause a runtime error due to exceeding this limit.  
- **Performance**: Factorials grow extremely fast, so very large factorials can take a long time to compute or exceed memory limits.
- If you need to handle **larger integers** or improve **performance**, consider using an **iterative approach** or other specialized libraries/functions.

## Contributing

Feel free to suggest improvements or optimizations! Submit a pull request or open an issue if you find any bugs or want to propose new features.

## License

This project is released under the [MIT License](LICENSE). You’re free to use, modify, and distribute this code for personal or commercial purposes.

---

**Enjoy computing factorials!** If you find this snippet helpful, feel free to leave a star or share it with others. Happy coding!
