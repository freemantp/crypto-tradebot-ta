from grpc import RpcError

def grpc_error_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RpcError as e:
            if e.details() == "Stream removed":
                print("ERROR: The gRPC stream was removed unexpectedly. Handling the error gracefully.")
            else:
                print("An error occurred:", e)

    return wrapper
