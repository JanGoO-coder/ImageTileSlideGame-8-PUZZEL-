from PIL import Image

def crop_picture():
    input_img = Image.open("./images/input/input.jpg")
    width, height = input_img.size

    # crop input image to 9 equal squares
    # and save them in a list
    squares = []
    for i in range(3):
        for j in range(3):
            left = width / 3 * i
            top = height / 3 * j
            right = width / 3 * (i + 1)
            bottom = height / 3 * (j + 1)
            squares.append(input_img.crop((left, top, right, bottom)))
            # export the cropped images to the "./images/output" folder
            squares[-1].save("./images/output/output_" + str(i) + str(j) + ".jpg")
