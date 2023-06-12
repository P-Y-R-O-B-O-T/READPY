from CYPHER_PROTOCOL.CYPHER_SERVER.cypher_server import CYPHER_SERVER
import json

#$$$$$$$$$$#

class READPY_SERVER() :
    def __init__(self) -> object :
        # DEFINING A DICTIONATR TO STORE ALL
        # THE DATA RECIEVED FROM CLIENTS
        #
        # THIS VARIABLE ACTS AS MEMORY VARIABLE
        self.DATA = {}
        # FIRST LOAD A CONFIG FILE "readpy_conf.json"
        # AND THEN CREATE A CYPHER_SERVER OBJECT
        # TO SERVER FOR REQUESTS
        #
        # ALL THE PARAMETERS OF CYPHER_SERVER
        # ARE IN THE CONFIG FILE
        # AND ARE PASSED ACCORDINGLY
        self.load_conf()
        self.METHOD_MAP = {"READ": self.read,
                           "WRITE": self.write}
        self.SERVER = CYPHER_SERVER(host=self.CONF["READPY_NODE"],
                                    port=self.CONF["READPY_PORT"],
                                    recv_buffer=self.CONF["RECV_BUFFER"],
                                    transmission_buffer=self.CONF["TRANSMISSION_BUFFER"],
                                    encryption_key=self.CONF["ENCRYPTION_KEY"],
                                    decryption_key=self.CONF["DECRYPTION_KEY"],
                                    request_handler=self.handle_request,
                                    timeout=self.CONF["TIMEOUT"],
                                    debug1=self.CONF["DEBUG1"],
                                    debug2=self.CONF["DEBUG2"])

    def handle_request(self,
                       request: dict,
                       ip_port: tuple) -> dict :
        # DEFINING REQUEST HANDLER FOR ALL THE REQUESTS
        # REQUESTS OPERATIONS ARE FOR READING FROM MEMORY
        # AND WRITING TO MEMORY
        #
        # FINALLY RETURN request
        if self.CONF["PRINT_REQ"] :
            print(ip_port, request)
        self.METHOD_MAP[request["OPERATION"]](request)
        return request

    def read(self,
             request: dict) -> None :
        # WHEN A READ FROM MEMORY REQUEST COMES
        # WE TAKE REFERENCE OF self.DATA
        #
        # request["DATA"] IS A LIST HAVING PATH
        # TO DATA LOCATION FROM WHERE TO READ
        #
        # WE REACH TO LOCATION BY DOING
        # data = data[_]
        # FOR _ IN request["DATA"]
        # IF ANY ERROR OCCURS THEN SET
        # request["DATA"] = None
        # AND request["METADATA"] = "NOT FOUND"
        #
        # IF NO ERROR OCCURED THEN
        # FINALLY request["DATA"] = data
        data = self.DATA
        for _ in request["DATA"] :
            try :
                data = data[_]
            except Exception as E :
                request["DATA"] = None
                request["METADATA"] = "NOT FOUND"
                return
        request["DATA"] = data

    def write(self,
              request: dict) -> None :
        # WHEN A WRITE TO MEMORY REQUEST COMES
        # WE TEKE REFERENCE OF self.DATA
        #
        # request["DATA"] IS A LIST HAVING PATH
        # TO DATA LOCATION FROM WHERE TO WRITE
        #
        # WE REACH TO LOCATION BY DOING
        # DATA = DATA[_]
        # FOR _ IN request["DATA"]
        # IF ANY ARROR OCCURS THEN SET
        # request["DATA"] = "PATH NOT EXIST"    AND THEN RETURN
        #
        # IF NO ERROR OCCURED THEN
        # FINALLY data[request["DATA"]["PATH"][-1]] = request["DATA"]["VALUE"]
        # AND THEN  request["DATA"] = "WRITTEN"
        data = self.DATA
        for _ in range(len(request["DATA"]["PATH"])-1) :
            try :
                data = data[request["DATA"]["PATH"][_]]
            except Exception as E :
                request["DATA"] = "PATH NOT EXIST"
                return
        data[request["DATA"]["PATH"][-1]] = request["DATA"]["VALUE"]
        request["DATA"] = "WRITTEN"

    def load_conf(self) :
        # FIRST READ THE JSON CONFIG FILE
        # AND THEN CONVERT THAT TO NATIVE DICTIONARY
        conf_file = open("readpy_conf.json", "r")
        self.CONF = json.load(conf_file)

    def start_node(self) -> None :
        # START CYPHER SERVER
        self.SERVER.start_server()

    def stop_node(self) -> None :
        # STOP CYPHER SERVER
        self.SERVER.stop_server()

#$$$$$$$$$$#
