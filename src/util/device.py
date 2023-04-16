
class Device():
    _instances = {}

    def __new__(cls, device_id):
        if device_id in cls._instances:
            return cls._instances[device_id]
        else:
            return super().__new__(cls)

    def __init__(self, device_id, device_name='__no_name__'):
        self.device_id = device_id
        self.device_name = device_name
        Device._instances[device_id] = self