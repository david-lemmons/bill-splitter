# Bill Splitter

This Python terminal program is designed for the user to input the bill total, tip percentage, and the number of people splitting the bill, to calculate how much everyone will pay and the total bill amount.

## Features

- Requires a positive bill amount and a positive whole-number group size
- Allows zero or positive tip percentages
- loops each question if answered with invalid inputs
- loops program if the user selects to split another bill

## How to Run

Requires Python 3

run `python main.py` from the project folder

## Assumptions

- The bill and tip are split equally
- zero-percent tips are allowed
- displayed amounts are rounded to two decimal places

## Result Example

```Enter the bill amount: 80
Enter the tip percentage (e.g., 15 for 15%): 15
Enter the number of people splitting the bill: 4
Total bill amount (including tip): $92.00
Expected tip amount: $12.00
Amount per person: $23.00
Would you like to calculate another bill? (y/n): Y
Enter the bill amount: 80
Enter the tip percentage (e.g., 15 for 15%): 15
Enter the number of people splitting the bill: 4
Total bill amount (including tip): $92.00
Expected tip amount: $12.00
Amount per person: $23.00
Would you like to calculate another bill? (y/n): N
Thank you for using the tip calculator. Goodbye!```