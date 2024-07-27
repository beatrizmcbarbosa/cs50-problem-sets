import sys

from PIL import Image, ImageOps

def main():
    # Command line arguments check
    # Exit if the user does not specify exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few or many arguments")
    # Exit if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
    # Exit if the input’s name does not have the same extension as the output’s name
    elif (sys.argv[1]).split(".")[1] == (sys.argv[2]).split(".")[1]:
        # Exit if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
        if(
            (sys.argv[1]).endswith(".jpg")
            or (sys.argv[1]).endswith(".jpeg")
            or (sys.argv[1]).endswith(".png")
            ):
            image_overlay()
        else:
            sys.exit("Invalid format")
    else:
        sys.exit("Different extensions")

def image_overlay():
    try:
        # Open input: image
        inputimage = Image.open(sys.argv[1])
    # Exit if the specified input does not exist.
    except FileNotFoundError:
        sys.exit("File not found")
    shirt = Image.open("shirt.png")
    size = shirt.size
    # Resize input: image
    cropped = ImageOps.fit(inputimage, size)
    # Overlay tshirt on input image
    cropped.paste(shirt, shirt)
    # Produce output: tshirt on image in a new file
    cropped.save(sys.argv[2])

if __name__ == "__main__":
    main()