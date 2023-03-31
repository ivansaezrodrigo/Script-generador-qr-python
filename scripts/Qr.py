import qrcode

class Qr:
    def __init__(self,versionVar=1,box_sizeVar=10,borderVar=2):
            self.qr = qrcode.QRCode(
            version=versionVar,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_sizeVar,
            border=borderVar,
        )

    def stringToQr(self,string,output, fill_colorVar="black",back_colorVar="white"):
        self.qr.add_data(string)
        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color=fill_colorVar, back_color=back_colorVar)
        img.save(output+"/"+string+".png")



if __name__ == "__main__":
    qr = Qr(1,10,4)
    qr.stringToQr('tuerca','.',"white","red")