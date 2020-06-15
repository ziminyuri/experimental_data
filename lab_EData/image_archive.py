def noise(type_of_noise, place_to_show_image, path_img: str, factor=0.3) -> None:
    pil_img = Image.open(path_img)
    pil_draw = ImageDraw.Draw(pil_img)
    width = pil_img.size[0]
    height = pil_img.size[1]

    if type_of_noise == "sold_peper":

        percentage_noise = int(width * height * factor)
        for i in range(percentage_noise):
            x = random.randrange(1, width, 1)
            y = random.randrange(1, height, 1)
            choice = random.randint(1, 2)
            if choice == 1:
                red = 0

            else:
                red = 255

            try:
                pil_draw.point((x, y), (red, red, red))
            except:
                pil_draw.point((x, y), red)

    elif type_of_noise == "gaussian":
        mean = 0
        # var = factor * 255
        # sigma = var ** 0.5
        sigma = factor * 255 / 2
        gauss = np.random.normal(mean, sigma, (width, height))
        pix = pil_img.load()
        for i in range(width):
            for j in range(height):
                try:
                    old_pix = pix[i, j][0]
                    pixel = old_pix + int(gauss[i][j])
                    if pixel > 255:
                        print('больше 255')
                        pil_draw.point((i, j), (255, 255, 255))

                    elif pixel < 0:
                        print('меньше 0')
                        pil_draw.point((i, j), (0, 0, 0))

                    else:
                        pil_draw.point((i, j), (pixel, pixel, pixel))
                except:
                    old_pix = pix[i, j]
                    pixel = old_pix + int(gauss[i][j])
                    if pixel > 255:
                        print('больше 255')
                        pil_draw.point((i, j), 255)

                    elif pixel < 0:
                        print('меньше 0')
                        pil_draw.point((i, j), 0)

                    else:
                        pil_draw.point((i, j), pixel)

    save_img(pil_img, place_to_show_image)