import sys

errPrefix = "ERROR: "
logPrefix = "INFO: "

class Journaler:
    def err(message, object = None):
        sys.stderr.write(errPrefix + str(message) + "\n")
        if object is not None:
            sys.stderr.write(errPrefix + "OBJECT:\n" + str(object) + "\n")

    def log(message, object = None):
        sys.stdout.write(logPrefix + str(message) + "\n")
        if object is not None:
            sys.stdout.write(logPrefix + "OBJECT:\n" + str(object) + "\n")
