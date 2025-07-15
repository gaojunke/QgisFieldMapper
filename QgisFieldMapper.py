# coding:utf-8
# 插件主控制器，管理菜单和插件窗口
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsProject
import os.path
from .QgisFieldMapper_dialog import QgisFieldMapperDialog

class QgisFieldMapper:
    def __init__(self, iface):
        self.iface = iface   # QGIS主界面句柄
        self.action = None
        self.dlg = None      # 插件主对话框

    def initGui(self):
        # 菜单和工具栏添加入口
        self.action = QAction("外部数据字段映射/追加", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&字段映射工具", self.action)

    def unload(self):
        # 卸载插件时清理菜单/工具栏
        if self.action:
            self.iface.removePluginMenu("&字段映射工具", self.action)
            self.iface.removeToolBarIcon(self.action)

    def run(self):
        # 打开主窗口
        if not self.dlg:
            self.dlg = QgisFieldMapperDialog(self.iface)
        self.dlg.show()
        self.dlg.raise_()
        self.dlg.activateWindow()
