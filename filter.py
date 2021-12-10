import sys
import os

from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageTk
from skimage.filters import frangi
import numpy as np
from imageio import imwrite

def bacon(img, blur, contrast, brightness, sigma_low, sigma_high, edge_enhence, inverse):
    img_gray = ImageOps.grayscale(img)

    if inverse:
        img_invert = ImageOps.invert(img_gray)
    else:
        img_invert = img_gray

    # img_gray.show()
    img_blur = img_invert.filter(ImageFilter.BoxBlur(blur))

    # img_blur.show()
    img_contrast = ImageEnhance.Contrast(img_blur).enhance(contrast)

    # img_contrast.show()

    img_edge = img_contrast.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, edge_enhence-1, -1, -1, -1, -1)))

    img_np = np.array(img_edge)

    img_frangi = frangi(img_np, sigmas=range(sigma_low, sigma_high))
    # img_frangi = frangi(img_np, sigmas=range(1, 10))

    normalized_img = (img_frangi/np.max(img_frangi)*255).astype(np.uint8)

    pil_image = Image.fromarray(normalized_img)
    pil_image = pil_image.convert("L")

    img_lighten = ImageEnhance.Brightness(pil_image).enhance(brightness)
    outimg = img_lighten
    # print(outimg)
    # imwrite(f"foo{blur}_{contrast}.png", (outimg/np.max(outimg)*255).astype(np.uint8))

    return ImageTk.PhotoImage(image=outimg)

