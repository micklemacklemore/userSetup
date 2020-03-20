from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

import sys
import json


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class UserSetup():
    def __init__(self):
        self.data = None
        self.pz_config = cmds.internalVar(usd=True) + "PZ_Config.json"
        self.pipeline_check()

    def pipeline_check(self):
        self.load_json()

        if not self.data["Pipeline Tools Setup"]["00_Pipeline"]:
            self.confirmDialog = cmds.confirmDialog( title='00_Pipeline Folder Not Found', message='Please find the 00_Pipeline Directory', button=['Okay'], defaultButton='Okay')
            if self.confirmDialog:
                self.find_dir()

            self.write_to_json()

    def find_dir(self):
        print True
        self.data["Pipeline Tools Setup"]["00_Pipeline"] = QtWidgets.QFileDialog.getExistingDirectory(maya_main_window(), "Find Directory", "C:/")

    def load_json(self):
        with open(self.pz_config) as f:
            self.data = json.load(f)

    def write_to_json(self):
        with open(self.pz_config, "w") as f:
            json.dump(self.data, f, indent=4)


UserSetup()