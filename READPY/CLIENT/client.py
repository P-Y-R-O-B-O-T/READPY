from CYPHER_PROTOCOL.CYPHER_CLIENT.cypher_client import CYPHER_CLIENT
from CYPHER_PROTOCOL.CYPHER_CLIENT.FTP.ftp_client import FTP_CLIENT
import os
import time
import json
import traceback

#$$$$$$$$$$#

# DEFINING ANNOTATIONS
PATH = list[str | int]
SLICE = [int, int, int]
DATA = dict | list | tuple | int | float | complex

#$$$$$$$$$$#

def ONLINE_SIGNAL_PROCESSOR() -> None :
    pass

def OFFLINE_SIGNAL_PROCESSOR() -> None :
    pass

def FILE_RESP_HANDLER(responce: dict) -> None :
    pass

#$$$$$$$$$$#

class READPY_CLIENT() :
    def __init__(self) -> object :
        # FIRST LOAD A CONFIG FILE "readpy_conf.json"
        # AND THEN CREATE A CYPHER_SERVER OBJECT
        # TO SERVER FOR REQUESTS
        #
        # ALL THE PARAMETERS OF CYPHER_CLIENT
        # ARE IN THE CONFIG FILE
        # AND ARE PASSED ACCORDINGLY
        #
        # FINALLY WE CONNECT TO SERVER
        self.load_conf()
        self.DATA = None
        self.META = None
        self.METHOD_MAP = {"READ": self.process_read,
                           "WRITE": self.process_write}
        self.CLIENT = CYPHER_CLIENT(ip=self.CONF["READPY_NODE"],
                                    port=self.CONF["READPY_PORT"],
                                    recv_buffer=self.CONF["RECV_BUFFER"],
                                    transmission_buffer=self.CONF["TRANSMISSION_BUFFER"],
                                    encryption_key=self.CONF["ENCRYPTION_KEY"],
                                    decryption_key=self.CONF["DECRYPTION_KEY"],
                                    responce_handler=self.responce_processor,
                                    timeout=self.CONF["TIMEOUT"])
        self.CLIENT.connect()

    def load_conf(self) -> None :
        # FIRST READ THE JSON CONFIG FILE
        # AND THEN CONVERT THAT TO NATIVE DICTIONARY
        conf_file = open("readpy_conf.json", "r")
        self.CONF = json.load(conf_file)

    def responce_processor(self,
                           responce: dict) -> None :
        self.METHOD_MAP[responce["OPERATION"]](responce)

    def process_read(self,
                     responce: dict) -> None :
        # SET RECIEVED DATA FROM
        # THE SERVER AS self.DATA
        #if "ERROR" != responce["DATA"] :
        self.DATA = responce["DATA"]
        self.META = responce["METADATA"]
        #else :
        #    self.DATA = "{0} : {1}".format("ERROR", responce["DATA"]["ERROR"])

    def process_write(self,
                      responce: dict) -> None :
        self.DATA = responce["DATA"]
        self.META = responce["METADATA"]

    def read(self,
             path: PATH) -> DATA :
        """
        path : list of strings and integers,
               any existing path on server memory
        """
        self.DATA = None
        # MAKING REQUEST TO READ DATA FROM THE
        # SERVER AD THEN RETURNING DATA AND METADATA
        self.CLIENT.make_request(operation="READ",
                                 data=path)
        return {"DATA": self.DATA, "METADATA": self.META}

    def read_slice(self,
                   path: PATH,
                   slice: SLICE) -> DATA :
        #self.CLIENT.make_request(operation="READ",
        #                         data={"PATH": path,
        #                               "SLICE": slice}
        #                         )
        #return self.DATA
        pass

    def write(self,
              path: PATH,
              data: DATA) -> dict :
        """
        path : list of strings and integers,
               the path may or may not exist on server
        data : any native pythonic data type
        """
        # MAKE REQUEST TO SERVER FOR STORING THE DATA
        self.CLIENT.make_request(operation="WRITE",
                                 data={"PATH": path,
                                       "VALUE": data})
        return {"DATA": self.DATA, "METADATA": self.META}

#$$$$$$$$$$#
