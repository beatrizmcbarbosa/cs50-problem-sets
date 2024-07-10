import sys, os

from PIL import Image, ImageOps

def main():
    # Command line arguments check
    # Exit if the user does not specify exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few or many arguments")
    # Exit if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
    elif sys.argv[1].endswith([".jpg", ".jpeg", ".png"]) == False or sys.argv[2].endswith([".jpg", ".jpeg", ".png"]) == False:
        sys.exit("Wrong format")
    # Exit if the input’s name does not have the same extension as the output’s name
    elif os.path.splitext(sys.argv[1]) != os.path.splitext(sys.argv[2]):
        sys.exit("Different formats")
    else:
        image_overlay()

def image_overlay():
    try:
        # Open input: image
        inputimage, shirt = Image.open(sys.argv[1], sys.argv[2])
        size = shirt.size
        # Resize input: image
        cropped = ImageOps.fit(inputimage, size)
        # Overlay tshirt on input image
        overlay = cropped.paste(inputimage, shirt)
        print(type(overlay))         # This type(...) has helped me out
                                        # of a jam many times !!!
        # Produce output: tshirt on image in a new file
        overlay.save(sys.argv[2])

    # Exit if the specified input does not exist.
    except FileNotFoundError:
        sys.exit("File not readable")

if __name__ == "__main__":
    main()

