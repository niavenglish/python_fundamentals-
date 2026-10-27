# Python Fundamentals – Area Calculator

## Project Description

For this assignment, I decided to use an Area Calculator that I created a few years ago. The program calculates the area of a circle, rectangle, or triangle based on the measurements entered by the user. I went back and made some changes to my original code to include input validation, string manipulation, and exception handling.

## How the Program Works

The program starts by asking the user to select a shape. They can enter C for circle, R for rectangle, or T for triangle. Depending on the shape selected, the program asks for the measurements needed to calculate the area. Once the measurements are entered, the program calculates and displays the area. The user can then choose to complete another calculation or exit the program.

## Python Concepts Used

- **Input Handling:** I used `input()` to collect information from the user and `float()` to convert the measurements into numbers.
- **String Manipulation:** I used `strip()`, `upper()`, `lower()`, and `count()` to format the user's input and work with strings.
- **Exception Handling:** I added `try/except` to prevent the program from crashing if the user enters something other than a number.
- **Functions:** I created separate functions to calculate the area of each shape and added another function to check numerical input.
- **Loops:** I used `while` loops so the user can try again if they enter an invalid number and continue using the calculator until they decide to quit.

## How to Run the Program

1. Download the `area_calculator.py` file from this repository.
2. Open the file in VS Code or another Python editor.
3. Make sure Python 3 is installed.
4. Run the program using `python area_calculator.py`.
5. Follow the prompts to select a shape and enter the measurements.

## Testing

I tested the program using different inputs to make sure the calculations were correct and that it could handle invalid information.

| Test | Input | Expected Result |
|---|---|---|
| Circle | Radius = 5 | 78.54 |
| Rectangle | Length = 4, Width = 6 | 24.0 |
| Triangle | Base = 10, Height = 5 | 25.0 |
| Invalid Number | abc | Error message and asks user to try again |
| Negative Number | -5 | Error message and asks user to try again |
| Lowercase Letter | c | Recognizes the circle selection |
| Invalid Shape | X | Displays an invalid input message |

## Edge Cases and Assumptions

One thing I wanted to make sure of was that the program would not crash if someone entered the wrong information. For example, if the user enters letters instead of numbers or enters a negative number, the program displays a message asking them to enter a valid number. I also made it where the user can enter lowercase letters when selecting a shape.

I assumed that the measurements entered would use the same unit since the program does not ask for a specific unit of measurement.

## Conclusion

This assignment gave me the opportunity to go back and improve a program I had already created. I was able to keep most of my original code while adding new features to make it work better and handle errors. It also helped me get more practice with Python concepts that I have used before.
