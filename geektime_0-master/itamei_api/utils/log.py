import logging

log = logging.getLogger("Itaimei")
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
log.addHandler(ch)
