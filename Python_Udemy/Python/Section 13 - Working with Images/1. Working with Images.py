# ---------------------------------------------------------------------------- #
#                              Working with Images                             #
# ---------------------------------------------------------------------------- #

from PIL import Image

# ------------------------------- Opening Image ------------------------------ #

# NOTE: need to convert it to RBG
flag = Image.open("C://Users//aiman//OneDrive//Desktop//Malaysia_Flag.jpg").convert('RGB')
# print(flag.mode)
# flag.show()

# -------------------------------- Attributes -------------------------------- #
""" print(flag.size)
print(flag.filename)
print(flag.format_description) """

# --------------------------------- Cropping --------------------------------- #

# Coordinate format: start from width, start from height, to width, to height
flag_cropped = flag.crop((0,0,66,35))
# flag_cropped.show()

# ------------------------------ Copying Images ------------------------------ #

# Now past the cropped image onto flag image
    # NOTE: this doesnt affect original image, this is happening in memory 
# flag.paste(im=flag_cropped, box=(63,1))
# flag.show()

# ------------------------------ Resizing Images ----------------------------- #

resized = flag.resize((4000,100))
# resized.show()

# ------------------------------ Rotating Images ----------------------------- #

rotated = flag.rotate(90)
# rotated.show()

# ------------------------------- Transparency ------------------------------- #

# flag.putalpha(100)
# flag.show()

# ------------------------------- Saving Images ------------------------------ #

# rotated.save('C://Users//aiman//OneDrive//Desktop//rotated_flag.png')
