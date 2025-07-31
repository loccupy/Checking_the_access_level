from libs.GXDLMSReader import GXDLMSReader
from libs.GXSettings import GXSettings

COM = 'COM20'
address = 0
baud = 115200


def connect_with_access_reader():
    settings = GXSettings()
    settings.getParameters("COM", COM, password='654321', authentication="Low", serverAddress=address + 16,
                           logicalAddress=1, clientAddress=32, baudRate=baud)
    reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)
    return reader, settings
