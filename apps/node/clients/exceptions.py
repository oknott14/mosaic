class HttpPostException(Exception):
    def __init__(self, e: Exception):
        Exception.__init__(e)
