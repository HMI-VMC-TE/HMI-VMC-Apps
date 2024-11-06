# -*- coding: utf-8 -*-
# support@simufact.de
# This file was created automatically by the packaging tool on 2024.11.06_15h27min26s.

import marshal, os
scriptDir = os.path.dirname(__file__)
appPath = os.path.join(scriptDir, "Heat source app.pyc")
with open(appPath, 'rb') as appFile:
    appFile.read(16)
    code = marshal.load(appFile)
    exec(code)
