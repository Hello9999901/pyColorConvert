#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
# —————————————————————————————————————————————
# CREATED BY HELLO9999901                      |
# Licensed Under the MIT License               |
# —————————————————————————————————————————————

import re

put = input("Input: ")

try:
    # clean it
    put = put.replace("#", "").replace(",", "")
    # check it
    RGBcheck = put.strip("rgb( )").split(" ")
    HEXcheck = re.findall('.'*2 , str(put))

    def rgbToHex():
        parsedRGB = put.strip("rgb( )").split(" ")
        for i in parsedRGB:
            if int(i) < 0 or int(i) > 255:
                raise ValueError("Only integers between 0 and 255 are allowed")
            else:
                pass
        redRGBtoHEX = (str(hex(int(parsedRGB[0]))).replace("0x", "")).upper()
        grnRGBtoHEX = (str(hex(int(parsedRGB[1]))).replace("0x", "")).upper()
        bluRGBtoHEX = (str(hex(int(parsedRGB[2]))).replace("0x", "")).upper()
        # For other purposes
        # finishedRGBtoHexList = [redRGBtoHEX, grnRGBtoHEX, bluRGBtoHEX] 
        print ("\n")
        print (redRGBtoHEX + grnRGBtoHEX + bluRGBtoHEX)
        print ("\n")
        print ("#" + redRGBtoHEX + grnRGBtoHEX + bluRGBtoHEX)

    def hexToRgb():
        parsedHex = re.findall('.'*2 , str(put))

        redHEXtoRGB = str(int(parsedHex[0], 16))
        grnHEXtoRGB = str(int(parsedHex[1], 16))
        bluHEXtoRGB = str(int(parsedHex[2], 16))
        finishedHextoRGBList = [redHEXtoRGB, grnHEXtoRGB, bluHEXtoRGB] 

        for i in finishedHextoRGBList:
            if int(i) < 0 or int(i) > 255:
                raise ValueError("Please Enter a Valid Hex Code")
            else:
                pass

        print ("\n")
        print (redHEXtoRGB + " " + grnHEXtoRGB + " " + bluHEXtoRGB)
        print ("\n")
        print ("rgb(" + redHEXtoRGB + ", " + grnHEXtoRGB + ", " + bluHEXtoRGB + ")")


    if len(RGBcheck) == 3:
        rgbToHex()
    elif len(HEXcheck) == 3:
        hexToRgb()

    else:
        print ("ERROR - Please try again")

except ValueError:
    raise ValueError("Only integers between 0 and 255 or a valid hex code are allowed")
