import logging

log = logging.getLogger("WeWorkApp")
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
log.addHandler(ch)
