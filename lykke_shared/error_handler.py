import logging
from grpc import RpcError

def grpc_error_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RpcError as e:
            logger = logging.getLogger()
            if e.details() == "Stream removed":
                logger.error('ERROR: The gRPC stream was removed unexpectedly. Handling the error gracefully.')
            else:
                logger.exception('An error occurred')

    return wrapper
