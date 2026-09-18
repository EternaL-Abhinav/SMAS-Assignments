# Q11: Interactive Image Transformation Toolbox
# SMAS-1 Assignment 3
# System Modelling, Analysis and Stories-1

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# ------------------------------------------------
# STEP 1: Load image
# ------------------------------------------------

image_name = "Photo01.jpeg"

original_image = Image.open(
    image_name
).convert("RGB")

original_image = np.array(
    original_image
)

# Current image
current_image = original_image.copy()

print("Image loaded successfully!")


# ------------------------------------------------
# STEP 2: Display image function
# ------------------------------------------------

def display_image(image, title):

    plt.figure(figsize=(7, 5))

    plt.imshow(image)

    plt.title(title)

    plt.axis("off")

    plt.show()


# ------------------------------------------------
# STEP 3: Rotate image
# ------------------------------------------------

def rotate_image(image, angle):

    pil_image = Image.fromarray(image)

    rotated = pil_image.rotate(
        angle,
        expand=True
    )

    return np.array(rotated)


# ------------------------------------------------
# STEP 4: Resize image
# ------------------------------------------------

def resize_image(image, factor):

    height, width = image.shape[:2]

    new_width = int(width * factor)

    new_height = int(height * factor)

    pil_image = Image.fromarray(image)

    resized = pil_image.resize(
        (new_width, new_height)
    )

    return np.array(resized)


# ------------------------------------------------
# STEP 5: Flip image
# ------------------------------------------------

def flip_image(image, direction):

    pil_image = Image.fromarray(image)

    if direction == "horizontal":

        flipped = pil_image.transpose(
            Image.Transpose.FLIP_LEFT_RIGHT
        )

    elif direction == "vertical":

        flipped = pil_image.transpose(
            Image.Transpose.FLIP_TOP_BOTTOM
        )

    else:

        print("Invalid flip direction.")

        return image

    return np.array(flipped)


# ------------------------------------------------
# STEP 6: Shear image
# ------------------------------------------------

def shear_image(image, shear_value):

    height, width = image.shape[:2]

    # New width after shear
    new_width = int(
        width + abs(shear_value) * height
    )

    # Create empty image
    output = np.zeros(
        (height, new_width, 3),
        dtype=np.uint8
    )

    # Move image depending on shear
    offset = 0

    if shear_value < 0:

        offset = int(
            abs(shear_value) * height
        )

    # Copy each pixel
    for y in range(height):

        shift = int(
            shear_value * y
        )

        for x in range(width):

            new_x = x + shift + offset

            if 0 <= new_x < new_width:

                output[y, new_x] = image[y, x]

    return output


# ------------------------------------------------
# STEP 7: Custom matrix transformation
# ------------------------------------------------

def custom_matrix_image(image, A):

    height, width = image.shape[:2]

    center_x = width / 2

    center_y = height / 2

    # Image corners
    corners = np.array([
        [-center_x, -center_y],
        [width - center_x, -center_y],
        [width - center_x, height - center_y],
        [-center_x, height - center_y]
    ])

    # Transform corners
    new_corners = corners @ A.T

    min_x = int(np.floor(new_corners[:, 0].min()))
    max_x = int(np.ceil(new_corners[:, 0].max()))

    min_y = int(np.floor(new_corners[:, 1].min()))
    max_y = int(np.ceil(new_corners[:, 1].max()))

    new_width = max_x - min_x
    new_height = max_y - min_y

    output = np.zeros(
        (new_height, new_width, 3),
        dtype=np.uint8
    )

    # Projection matrix cannot be inverted
    if np.linalg.matrix_rank(A) < 2:

        print("Matrix is singular.")

        print("It cannot be used for normal image transformation.")

        return output

    inv_A = np.linalg.inv(A)

    y_out, x_out = np.indices(
        (new_height, new_width)
    )

    x_new = x_out + min_x

    y_new = y_out + min_y

    original = np.stack(
        [x_new, y_new],
        axis=-1
    )

    original = original @ inv_A.T

    x_original = np.round(
        original[..., 0] + center_x
    ).astype(int)

    y_original = np.round(
        original[..., 1] + center_y
    ).astype(int)

    valid = (
        (x_original >= 0) &
        (x_original < width) &
        (y_original >= 0) &
        (y_original < height)
    )

    output[valid] = image[
        y_original[valid],
        x_original[valid]
    ]

    return output


# ------------------------------------------------
# STEP 8: Main interactive menu
# ------------------------------------------------

while True:

    print("\n")
    print("======================================")
    print(" IMAGE TRANSFORMATION TOOLBOX")
    print("======================================")

    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("7. Exit")

    print("======================================")

    choice = input(
        "Enter your choice (1-7): "
    )


    # --------------------------------------------
    # OPTION 1: Rotate
    # --------------------------------------------

    if choice == "1":

        angle = float(
            input("Enter rotation angle: ")
        )

        current_image = rotate_image(
            current_image,
            angle
        )

        display_image(
            current_image,
            "Rotated Image"
        )


    # --------------------------------------------
    # OPTION 2: Resize
    # --------------------------------------------

    elif choice == "2":

        factor = float(
            input("Enter resize factor: ")
        )

        if factor <= 0:

            print("Factor must be greater than zero.")

        else:

            current_image = resize_image(
                current_image,
                factor
            )

            display_image(
                current_image,
                "Resized Image"
            )


    # --------------------------------------------
    # OPTION 3: Flip
    # --------------------------------------------

    elif choice == "3":

        direction = input(
            "Enter horizontal or vertical: "
        )

        current_image = flip_image(
            current_image,
            direction
        )

        display_image(
            current_image,
            "Flipped Image"
        )


    # --------------------------------------------
    # OPTION 4: Shear
    # --------------------------------------------

    elif choice == "4":

        shear_value = float(
            input("Enter shear factor: ")
        )

        current_image = shear_image(
            current_image,
            shear_value
        )

        display_image(
            current_image,
            "Sheared Image"
        )


    # --------------------------------------------
    # OPTION 5: Custom Matrix
    # --------------------------------------------

    elif choice == "5":

        print("\nEnter the 2x2 custom matrix")

        a = float(input("Enter a: "))

        b = float(input("Enter b: "))

        c = float(input("Enter c: "))

        d = float(input("Enter d: "))

        A = np.array([
            [a, b],
            [c, d]
        ])

        print("\nYour matrix is:")

        print(A)

        current_image = custom_matrix_image(
            current_image,
            A
        )

        display_image(
            current_image,
            "Custom Matrix Image"
        )


    # --------------------------------------------
    # OPTION 6: Reset
    # --------------------------------------------

    elif choice == "6":

        current_image = original_image.copy()

        print("Image reset successfully!")

        display_image(
            current_image,
            "Original Image"
        )


    # --------------------------------------------
    # OPTION 7: Exit
    # --------------------------------------------

    elif choice == "7":

        print("Thank you for using the toolbox!")

        break


    # --------------------------------------------
    # Invalid choice
    # --------------------------------------------

    else:

        print("Invalid choice.")

        print("Please enter a number from 1 to 7.")