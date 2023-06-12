# READPY

![](ZZZ/ZZZ.jpg)

* [PROJECT LINK GITHUB](https://github.com/P-Y-R-O-B-O-T/READPY)
* [PROJECT LINK PYPI](https://pypi.org/project/readpy-P-Y-R-O-B-O-T/)

* A mini redis server written in python using CYPHER-PROTOCOL
* For many purposes, 4GB 8GB RAM is not enough, we need services like REDIS, or what we RAM/MEMORY servers, this project makes using that task very easy.
# COMPATIBLITY

* READPY works with Linux, OS-X, and Windows (OS INDEPENDENT).

* Supported on python 3.10 and above

# INSTALLATION

> Install it using pip.

* Goto [PYPI](https://pypi.org/project/readpy-P-Y-R-O-B-O-T/)

# USAGE

## CONFIGURATION
* For configuration of server and client need a configuration file named readpy_conf.json

### CONFIG PARAMETERS
* RECV_BUFFER and TRANSMISSION_BUFFER are parameters both should have same corresponding value for both server and client configuration.

* ENCRYPTION_KEY and DECRYPTION_KEY are parameters which ensure encryption of data sent over connection, see CYPHER-PROTOCOL documentation for more information.

* TIMEOUT is the time after which a connection is closed or reset from client side or server side.

* READPY_NODE defines the interface address at which the server will be running (IP).

* READPY_PORT defines port number on which server runs.

* Example readpy_conf is given in CONF_FILES folder, consider that for more details.

## CLIENT USAGE
* Put the readpy_conf.json and TEST_SCRIPT/client.py in same folder and run in same directory space.

* Consider the following code :

```python3
from READPY.CLIENT.client import READPY_CLIENT

if __name__ == "__main__" :
	# INITIALISING THE READPY_CLIENT
	CLIENT = READPY_CLIENT()

	# WRITING THE DATA {"VAR1": "Hello from VAR1"} ON LOCATION ["CONSTANTS"] IN SERVER
	print(CLIENT.write(["CONSTANTS"], {"VAR1": "Hello from VAR1"}))

	# WRITING THE DATA {"PI": 3.14} ON LOCATION ["CONSTANTS", "MATH"] IN SERVER
	print(CLIENT.write(["CONSTANTS", "MATH"], {"PI": 3.14}))

	# UPDATING THE DATA {"PI": 3.14} TO {"PI": 3.1428} ON LOCATION ["CONSTANTS", "MATH"]
	print(CLIENT.write(["CONSTANTS", "MATH"], {"PI": 3.14}))

	# READING FROM THE LOCATION ["CONSTANTS"] FROM THE SERVER
	print(CLIENT.read(["CONSTANTS"]))

	# READING FROM THE LOCATION ["CONSTANTS", "MATH"] FROM THE SERVER
	print(CLIENT.read(["CONSTANTS", "MATH"]))
```

## SERVER USAGE
* Put the readpy_conf.json and TEST_SCRIPT/server.py in same folder and run in same directory space.

* Consider the following code :

```python3
from READPY.SERVER.server import READPY_SERVER

if __name__ == "__main__" :
	# INITIALISING THE READPY_SERVER
	SERVER = READPY_SERVER()
	# STARTING THE SERVER
	SERVER.start_node()
	input()
	# STOPPING THE SERVER AS SOON AS FILE INPUT FACES NEWLINE CHARACTER
	SERVER.stop_node()
```
