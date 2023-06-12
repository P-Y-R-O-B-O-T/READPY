from READPY.SERVER.server import READPY_SERVER

if __name__ == "__main__" :
    SERVER = READPY_SERVER()
    SERVER.start_node()
    input()
    SERVER.stop_node()
