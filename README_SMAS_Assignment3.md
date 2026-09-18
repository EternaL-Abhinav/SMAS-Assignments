# SMAS-1 Assignment 3 – Linear Transformations

This folder contains the two Python programs made for Assignment 3 of **System Modelling, Analysis and Stories-1**.

The first program is for **Question 10**, where different matrix transformations are applied to an actual image.

The second program is for **Question 11**, where an python toolbox is designed for performing different transformations on an actual image.

---

## Files in this folder


Assignment

Q10_image_transform.py
Q11_image_toolbox.py
Photo01.jpeg
README.md
```

`Photo01.jpg` is just an example image. Any JPG or PNG image can be used, but the file name in the Python code should match the actual image name.

---

# 1. Q10 – Transform an Actual Image

## Aim

The purpose of this program is to see how a matrix changes an image.

The assignment gives five matrices:

### A1 – Scaling

[ 2    0 ]
[ 0   0.5]

This makes the image wider and reduces its height.

### A2 – 90 degree rotation

[ 0  -1 ]
[ 1   0 ]

This rotates the image 90 degrees counterclockwise.

### A3 – Horizontal shear

[ 1   1 ]
[ 0   1 ]

This slants the image horizontally.

### A4 – Reflection in the y-axis

[-1   0 ]
[ 0   1 ]

This gives a mirror image with respect to the y-axis.

### A5 – Projection onto the x-axis

[ 1   0 ]
[ 0   0 ]

This removes the y-coordinate, so one dimension of information is lost.

---

## How the Q10 program works

First, the program reads the image using Pillow and converts it into a NumPy array.

Then, it creates the five given matrices. 

For each matrix, the program:

1. Finds the image of `e1`.
2. Finds the image of `e2`.
3. Finds the rank of the matrix.
4. Checks whether information is lost.
5. Applies the matrix to the image.
6. Displays the transformed image.

The image is treated as a collection of 2-D pixel coordinates. The centre of the image is taken as the origin so that the transformations happen around the centre.

The program uses the inverse matrix method for the image transformation. This is useful because it finds where each output pixel came from in the original image.

---

## Why the rank is calculated?

The rank tells us how many independent dimensions are still present after the transformation.

For the first four matrices:

    Rank = 2

So the full 2-D information is still present.

For the projection matrix A5:

    Rank = 1

So one dimension is lost. This is why the projection is different from the other transformations.

---

## Running Q10

Make sure Python is installed on the computer.

Open the terminal in VS Code and install the required libraries:

pip install numpy matplotlib pillow

Then keep the image in the same folder as the Python file.

For example:

Assignment
Q10_image_transform.py
Photo01.jpg

Run the program using:

python Q10_image_transform.py

If the image has a different name, change this line in the program:

image_name = "image.jpg"

For example:

image_name = "myphoto.png"

---

# 2. Q11 – Interactive Image Transformation Toolbox

## Aim

The second program is a simple image transformation toolbox.

Instead of changing the code every time, the user can choose an operation from a menu and enter the required value.

The menu contains:

1. Rotate
2. Resize
3. Flip
4. Shear
5. Custom Matrix
6. Reset
7. Exit

---

## How each option works

### 1. Rotate

The user enters an angle, for example:

Enter rotation angle: 90

The program rotates the current image by that angle.

---

### 2. Resize

The user enters a resize factor.

For example:

Enter resize factor: 2

This makes the image twice as large.

A factor of `0.5` makes the image half the size.

---

### 3. Flip

The program asks:

Enter horizontal or vertical:

For example:

horizontal

The image is then flipped horizontally.

---

### 4. Shear

The user enters a shear factor.

For example:

Enter shear factor: 0.5


This makes the image slant.

---

### 5. Custom Matrix

The user can enter their own 2 x 2 matrix.

For example, entering:

a = 1
b = 1
c = 0
d = 1

creates:

[ 1  1 ]
[ 0  1 ]

which is the horizontal shear matrix from Question 5.

This option is included so that different matrix transformations can be tested without changing the main program.

---

### 6. Reset

This brings the image back to the original image.

This is useful when several transformations have been applied and I want to start again without restarting the program.

---

### 7. Exit

This closes the toolbox.

---

## How the Q11 program works

The program first loads the original image and stores a copy of it.

Another variable called `current_image` keeps the image that is currently being displayed.

Each menu option calls a different function:

rotate_image()
resize_image()
flip_image()
shear_image()
custom_matrix_image()

After the selected operation is completed, the new image is displayed.

The program keeps showing the menu inside a `while` loop, so more than one operation can be performed without reopening the program.

---

## Running Q11

The required libraries are the same as Q10:

pip install numpy matplotlib pillow

Keep the image in the same folder as the Python program.

For example:

Assignment
├── Q11_image_toolbox.py
└── image.jpg

Run it using:

python Q11_image_toolbox.py

The terminal will show the menu and wait for the user's choice.

---

# 3. Libraries used

### NumPy

NumPy is used for:

- Storing matrices
- Matrix multiplication
- Finding matrix rank
- Performing numerical calculations

Example:

```python
A @ e1
```

is used to multiply a matrix by a vector.

### Matplotlib

Matplotlib is used to display the original and transformed images.

Example:

```python
plt.imshow(image)
```

### Pillow

Pillow is used to open, resize, rotate and flip image files.

Example:

```python
Image.open(image_name)
```

---

# 4. Difference between Q10 and Q11

**Q10** is mainly for showing the five transformations given in the assignment and studying their matrices, rank and information loss.

**Q11** is more like a small application. It gives the user a menu and lets the user choose what transformation to apply.

So, Q10 is more focused on the mathematical part of the assignment, while Q11 is focused on making an interactive tool.

---

# 5. Things to remember before running the programs

- Keep the image file in the correct folder.
- Check that the file name written in the code is correct.
- Install NumPy, Matplotlib and Pillow before running the program.
- Use Python 3.
- Run the programs from the folder where the `.py` files are saved.

The projection matrix in Q10 is:

[ 1  0 ]
[ 0  0 ]

It has rank 1 and loses one dimension of information. Since it is a singular matrix, the normal inverse-matrix method cannot be used for it in the same way as the other four matrices. This is why the program treats the projection case separately.

---

# 6. What I learned from this assignment

While making these programs, I understood better how a matrix can be used to represent a transformation. I also got to see the connection between the mathematical idea of linear transformations and something visual like an image.

The rank part was also useful because it shows that a transformation does not just change the shape of an object. It can also remove information, as in the case of projection.

The second program helped me understand how functions, loops, conditions and user input can be combined to make a simple interactive Python program.
