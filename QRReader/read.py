import sys

from pyzbar.pyzbar import decode as _pyzbar_decode

from PIL.Image import open as _pil_open

version = "1.0.0"

def test():
    from pyzbar import __version__ as pyzbar_version
    from PIL import __version__ as pil_version
    print("PyZBar version: ", pyzbar_version)
    print("Pillow version: ", pil_version)
    print("")


def open_image(path: str):
    try:
        return _pil_open(path)
    except Exception as e:
        print(
            "Failed to open the file, Please check if your path is correct ({})".format(e))
        sys.exit(1)


def read(path: str):
    try:
        return _pyzbar_decode(open_image(path))
    except Exception as e:
        if isinstance(e, SystemExit):
            raise
        print("Failed to decode the image ({})".format(e))


def _main(args):
    print("QR-Reader, Read QR codes inside your terminal, Written by TheOddZer0")
    print("See COPYING for more info")
    print("See the original repo for more info, updates: https://github.com/TheOddZer0/QR-Reader")
    print("")
    if "-v" in args:
        test()
    if len(args) != 2:
        print(f"{sys.argv[0]} FILENAME\nMissing arguments or additional arguments passed")
        sys.exit(1)
    codes = read(args[1])
    if codes is None:
        sys.exit(1)
    for code in codes:
        if "-v" in args:
            print("Type: {}\nData: {}".format(
                code.type, code.data.decode("UTF-8")))
        else:
            print("Data: {}".format(code.data.decode("UTF-8")))
        print("")
    if not codes:
        print("No QR code found")

def main(args=None):
    if args is None:
        args = sys.argv
    try:
        _main(args)
    except KeyboardInterrupt:
        print("Eww, Exiting...")

if __name__ == '__main__':
    main()
