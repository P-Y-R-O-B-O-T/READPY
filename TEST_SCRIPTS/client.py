from READPY.CLIENT.client import READPY_CLIENT

if __name__ == "__main__" :
    CLIENT = READPY_CLIENT()
    print(CLIENT.write(["qwe"], {"HUH": None}))
    print(CLIENT.write(["qwe", "123", "qwe"], {"HUH": None}))
    print(CLIENT.read(["qwe", "HUH"]))
    print(CLIENT.read(["123", "123", "123"]))
