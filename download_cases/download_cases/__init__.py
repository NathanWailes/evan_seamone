# Code from:
# https://medium.com/@rutger_93697/i-thought-this-solution-was-somewhat-complex-3e8bc91f83f8

import os
import json
import pkgutil
import logging

path = "{}/google-cloud-storage-credentials.json".format(os.getcwd())

credentials_content = '''...'''

with open(path, "w") as text_file:
    text_file.write(json.dumps(json.loads(credentials_content)))

logging.warning("Path to credentials: %s" % path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
