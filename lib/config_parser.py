import json
from sys import stderr
class Config:
    def __init__(self, configPath, journaler = None):
        try:
            fileHandle = open(configPath)
            configText = file.read(fileHandle)
        except IOError as e:
            if journaler:
                journaler.log("ERROR", e)
            else:
                stderr.write(e)
            raise

        try:
            self.values = json.loads(configText.encode('utf8'))
        except ValueError as e:
            if journaler:
                journaler.log("ERROR", e)
            else:
                stderr.write(e)
            raise
