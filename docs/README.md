# Overview
This documentation provides a detailed guide on how to use the calculate.py script to perform area and perimeter calculations for basic geometric shapes. The script supports calculations for circles and squares.


# How to Use the Calculator
Step-by-Step Instructions
## 1. Run the Script:

 Open a terminal or command prompt.

 Navigate to the directory containing calculate.py.

 Run the script by typing:
```
python calculate.py
```
## 2. Enter the Figure Name:

 The script will prompt you to enter the name of the figure.

 Available options are:
 Circle
 Square

 Type the name of the figure and press Enter.

## 3. Enter the Function:

 The script will prompt you to enter the function you want to perform.

 Available options are:
 Area
 Perimeter

 Type the function name and press Enter.

## 4. Enter Figure Sizes:

 Depending on the figure and function selected, the script will prompt you to enter the necessary dimensions.

 For a Circle, you will be asked to enter the Radius.

 For a Square, you will be asked to enter the length of one Side.

 Enter the value and press Enter.
## 5. Get the Answer:

 The script will calculate the requested value (area or perimeter) and display the result.


# Math formulas
создала функцию

## Area
The area of a shape is the amount of space enclosed within its boundaries. The formulas for calculating the area of a circle, rectangle, and square are as follows:

- Circle: `S = πR²`
The area S of a circle is calculated by multiplying the square of the radius R by the constant π (approximately 3.14159).
### Example:
```
 return math.pi * r * r
```
If the radius R is 5 units, then the area S is 𝜋 × 5^2 = 25π square units.

- Square: `S = a²`
The area S of a square is calculated by squaring the length of one of its sides a.
### Example
```
 return a * a
```
If the side length a is 6 units, then the area S is 6^2 = 36 square units.

- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter
The area S of a triangle is calculated using Heron's formula, where p is the semiperimeter (half of the triangle's perimeter).
### Example
```
 return sqrt(p * (p-a) * (p-b) * (p-c))
```
If the sides a, b, and c are 3, 4, and 5 units respectively, then the area S is sqrt(6 * (6-3) * (6-4) * (6-5)) = sqrt(6 * 3 * 2 * 1) = sqrt(36) = 6 square units.

- Rectangle: `S = ab`
Calculates the area of a rectangle given the lengths of sides a and b.
### Example
```
 return a * b

```

## Perimeter
The perimeter of a shape is the total length of its boundary. The formulas for calculating the perimeter of a circle, rectangle, and square are as follows

- Circle: `P = 2πR`
The perimeter P (also known as the circumference) of a circle is calculated by multiplying the diameter (which is twice the radius R) by the constant π.
### Example: 
```
 return 2 * math.pi * r
```
If the radius R is 5 units, then the perimeter P is 2π×5 = 10π units.

- Square: `P = 4a`
The perimeter P of a square is calculated by multiplying the length of one of its sides a by 4.
### Example: 
```
 return 4 * a
```
If the side length a is 6 units, then the perimeter P is 4×6=24 units.

- Rectangle: `P = 2a + 2b`
The perimeter P of a rectangle is calculated by adding twice the length a and twice the width b.
### Example: 
```
 return 2*a + 2*b
```
If the lengths a and b are 4 and 6 units respectively, then the perimeter P is 2*4 + 2*6 = 8 + 12 = 20 units.

- Triangle: `P = a + b + c`
The perimeter P of a triangle is calculated by summing the lengths of its three sides a, b, and c
### Example:
```
 return a + b + c
```
If the sides a, b, and c are 3, 4, and 5 units respectively, then the perimeter P is 3 + 4 + 5 = 12 units.

# история изменения проекта
* commit af945eeab31d08458dbe437701fc78d2ad88439b (HEAD -> documentation)
| Author: PolinaPrilepo <polushona@yandex.ru>
| Date:   Tue Oct 15 14:32:11 2024 +0300
| 
|     add documentation to triangle.py
| 
* commit c5821e15a26cc727c5766a14d7dc569cd8e3849b
| Author: PolinaPrilepo <polushona@yandex.ru>
| Date:   Tue Oct 15 14:28:59 2024 +0300
| 
|     add documentation to square.py
| 
* commit b26a1a0d08da0a4d1cbedd1e8abc16df42f105dd
| Author: PolinaPrilepo <polushona@yandex.ru>
| Date:   Tue Oct 15 14:28:29 2024 +0300
| 
|     add documentation to circle.py
| 
* commit b6d9599b9eb4ac5bbd4d0fe10a190e88109821d0
| Author: PolinaPrilepo <polushona@yandex.ru>
| Date:   Tue Oct 15 14:27:39 2024 +0300
| 
|     add documentation to calculate.py

