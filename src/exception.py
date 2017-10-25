class OrderingError(Exception):
    """
        Class used to define an exception when there's any kind of problem
        during the ordering process. In general, used when the configuration
        file has problems.
    """
    def __init__(self):
        self.message = "Tivemos um problema"
