# Q10: Image Transformation using Matrices
# SMAS-1 Assignment 3
# System Modelling, Analysis and Stories-1

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# ------------------------------------------------
# STEP 1: Read the image
# ------------------------------------------------

# Change this to your image file name
image_name = "Photo01.jpeg"

img = Image.open(image_name).convert("RGB")

# Convert image into numpy array
img_array = np.array(img)

# Get image height and width
height, width = img_array.shape[:2]

print("Image loaded successfully!")
print("Image width:", width)
print("Image height:", height)


# ------------------------------------------------
# STEP 2: Define the five matrices
# ------------------------------------------------

# A1: Scaling
A1 = np.array([
    [2, 0],
    [0, 0.5]
])


# A2: 90 degree counterclockwise rotation
A2 = np.array([
    [0, -1],
    [1, 0]
])


# A3: Horizontal shear
A3 = np.array([
    [1, 1],
    [0, 1]
])


# A4: Reflection in y-axis
A4 = np.array([
    [-1, 0],
    [0, 1]
])


# A5: Projection onto x-axis
A5 = np.array([
    [1, 0],
    [0, 0]
])


# Store all matrices in a list
matrices = [A1, A2, A3, A4, A5]


# Names of transformations
names = [
    "Scaling",
    "90 Degree Rotation",
    "Horizontal Shear",
    "Reflection in y-axis",
    "Projection onto x-axis"
]


# ------------------------------------------------
# STEP 3: Print images of e1 and e2
# ------------------------------------------------

e1 = np.array([1, 0])
e2 = np.array([0, 1])

print("\nRESULTS OF FIVE MATRICES")
print("--------------------------------")


for i in range(5):

    A = matrices[i]

    print("\n", names[i])

    print("Matrix:")
    print(A)

    # Image of e1
    Te1 = A @ e1

    # Image of e2
    Te2 = A @ e2

    print("T(e1) =", Te1)
    print("T(e2) =", Te2)

    # Find rank
    rank = np.linalg.matrix_rank(A)

    print("Rank =", rank)

    # Information loss
    if rank < 2:
        print("Information loss: YES")
    else:
        print("Information loss: NO")


# ------------------------------------------------
# STEP 4: Image transformation function
# ------------------------------------------------

def transform_image(image, A):

    # Get image dimensions
    height, width = image.shape[:2]

    # Image centre
    center_x = width / 2
    center_y = height / 2

    # Four corners about image centre
    corners = np.array([
        [-center_x, -center_y],
        [width - center_x, -center_y],
        [width - center_x, height - center_y],
        [-center_x, height - center_y]
    ])

    # Transform the corners
    new_corners = corners @ A.T

    # Find new image boundaries
    min_x = int(np.floor(new_corners[:, 0].min()))
    max_x = int(np.ceil(new_corners[:, 0].max()))

    min_y = int(np.floor(new_corners[:, 1].min()))
    max_y = int(np.ceil(new_corners[:, 1].max()))

    # New image size
    new_width = max_x - min_x
    new_height = max_y - min_y

    # Create empty output image
    output = np.zeros(
        (new_height, new_width, 3),
        dtype=np.uint8
    )

    # Create output pixel coordinates
    y_out, x_out = np.indices((new_height, new_width))

    x_new = x_out + min_x
    y_new = y_out + min_y

    # Inverse transformation
    # Used to find original pixel locations
    if np.linalg.matrix_rank(A) < 2:

        print("Projection matrix cannot be inverted.")

        return output

    inv_A = np.linalg.inv(A)

    original = np.stack(
        [x_new, y_new],
        axis=-1
    )

    original = original @ inv_A.T

    # Convert back to image coordinates
    x_original = np.round(
        original[..., 0] + center_x
    ).astype(int)

    y_original = np.round(
        original[..., 1] + center_y
    ).astype(int)

    # Check valid pixels
    valid = (
        (x_original >= 0) &
        (x_original < width) &
        (y_original >= 0) &
        (y_original < height)
    )

    # Copy valid pixels
    output[valid] = image[
        y_original[valid],
        x_original[valid]
    ]

    return output


# ------------------------------------------------
# STEP 5: Display original image
# ------------------------------------------------

plt.figure(figsize=(6, 4))

plt.imshow(img_array)

plt.title("Original Image")

plt.axis("off")

plt.show()


# ------------------------------------------------
# STEP 6: Apply all five transformations
# ------------------------------------------------

for i in range(5):

    A = matrices[i]

    name = names[i]

    # Projection is a special case
    if i == 4:

        print("\nProjection matrix is singular.")

        print("It collapses the image onto the x-axis.")

        print("True matrix:")
        print(A5)

        # Small y-scale only for visualization
        A_visual = np.array([
            [1, 0],
            [0, 0.01]
        ])

        transformed = transform_image(
            img_array,
            A_visual
        )

    else:

        transformed = transform_image(
            img_array,
            A
        )

    # Display transformed image
    plt.figure(figsize=(6, 4))

    plt.imshow(transformed)

    plt.title(name)

    plt.axis("off")

    plt.show()