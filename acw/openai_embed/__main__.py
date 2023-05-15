from .. import server_sock
from . import lib
from . import config
server_sock.run(lib.main,config.port)
