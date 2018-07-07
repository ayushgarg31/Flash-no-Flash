import numpy as np
import cv2


def flash_no_flash(img1, img2, d, sig_col, sigma):
    flash = cv2.imread(img1, 0)
    no_flash = cv2.imread(img2, 0)

    if d == -1:
        d = 9
    if sig_col == -1:
        sig_col = 30
    if sigma == -1:
        sigma = (((flash.shape[0]**2)+(flash.shape[1]**2))**0.5)*0.025

    base_f = cv2.bilateralFilter(flash, d, sig_col, sigma)
    base_nf = cv2.bilateralFilter(no_flash, d, sig_col, sigma)

    flash = flash.astype('float')
    base_f = base_f.astype('float')
    detail = cv2.divide(flash, base_f)

    base_nf = base_nf.astype('float')
    intensity = cv2.multiply(base_nf, detail)

    no_flash = no_flash.astype('float')
    nflash_color = cv2.imread(img2, 1)
    nflash_color = nflash_color.astype('float')
    b = nflash_color[:, :, 0]
    g = nflash_color[:, :, 1]
    r = nflash_color[:, :, 2]
    b = cv2.divide(b, no_flash)
    g = cv2.divide(g, no_flash)
    r = cv2.divide(r, no_flash)

    intensity=intensity.astype('float')
    b = cv2.multiply(b, intensity)
    g = cv2.multiply(g, intensity)
    r = cv2.multiply(r, intensity)

    result = np.zeros((flash.shape[0], flash.shape[1],3), np.uint8)
    result[:, :, 0] = b
    result[:, :, 1] = g
    result[:, :, 2] = r

    cv2.imwrite('result.jpg', result)
