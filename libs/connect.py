from libs.GXDLMSReader import GXDLMSReader
from libs.GXSettings import GXSettings

global COM
global ADDRESS
global BAUD


def connect_with_access_reader():
    settings = GXSettings()
    settings.getParameters("COM", f'COM{COM}', password='654321', authentication="Low", serverAddress=ADDRESS + 16,
                           logicalAddress=1, clientAddress=32, baudRate=BAUD)
    reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)
    return reader, settings
