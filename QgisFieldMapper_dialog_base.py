# coding:utf-8
# 插件主界面UI代码（可用Qt Designer生成，也可直接用此代码）
from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.gui import QgsMapLayerComboBox, QgsFileWidget
from qgis.core import QgsVectorLayer

class Ui_QgisFieldMapperDialogBase(object):
    def setupUi(self, QgisFieldMapperDialogBase):
        QgisFieldMapperDialogBase.setObjectName("QgisFieldMapperDialogBase")
        QgisFieldMapperDialogBase.resize(800, 520)  # 增加窗口宽度以适应水平布局
        
        # 创建主水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(QgisFieldMapperDialogBase)
        
        # 创建左侧容器和垂直布局
        self.leftWidget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        
        # 选择本身图层
        self.labelTarget = QtWidgets.QLabel("① 选择本身图层：")
        self.verticalLayout.addWidget(self.labelTarget)
        
        # 添加图层选择组合框
        self.mapLayerComboBox = QgsMapLayerComboBox()
        # 在QgisFieldMapper_dialog.py中设置过滤器
        self.verticalLayout.addWidget(self.mapLayerComboBox)
        
        # 添加文件选择组件
        self.fileWidget = QgsFileWidget()
        self.fileWidget.setFilter("矢量数据 (*.shp *.geojson *.sqlite *.gpkg)")
        self.fileWidget.setDialogTitle("选择本身图层文件")
        self.fileWidget.setStorageMode(QgsFileWidget.GetFile)
        self.verticalLayout.addWidget(self.fileWidget)
        
        # 选择外部数据
        self.labelExternal = QtWidgets.QLabel("② 选择外部数据：")
        self.verticalLayout.addWidget(self.labelExternal)
        self.externalFileWidget = QgsFileWidget()
        self.externalFileWidget.setFilter("矢量数据 (*.shp *.geojson *.sqlite *.gpkg)")
        self.externalFileWidget.setDialogTitle("选择外部数据文件")
        self.verticalLayout.addWidget(self.externalFileWidget)
        
        # 操作模式
        self.labelMode = QtWidgets.QLabel("③ 操作模式：")
        self.verticalLayout.addWidget(self.labelMode)
        self.cmbMode = QtWidgets.QComboBox()
        self.verticalLayout.addWidget(self.cmbMode)
        
        # 字段对应表
        self.labelMap = QtWidgets.QLabel("④ 字段对应关系：")
        self.verticalLayout.addWidget(self.labelMap)
        self.tableFieldMap = QtWidgets.QTableWidget()
        self.tableFieldMap.setMinimumHeight(180)
        self.verticalLayout.addWidget(self.tableFieldMap)
        
        # 执行按钮
        self.btnDo = QtWidgets.QPushButton("执行操作")
        self.btnDo.setMinimumHeight(40)
        self.verticalLayout.addWidget(self.btnDo)
        
        # 将左侧部件添加到主水平布局
        self.horizontalLayout.addWidget(self.leftWidget)
        
        # 创建右侧帮助说明
        self.rightWidget = QtWidgets.QWidget()
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        
        # 帮助说明标题
        self.labelHelp = QtWidgets.QLabel("工具操作说明：")
        self.rightLayout.addWidget(self.labelHelp)
        
        # 帮助说明文本框
        self.textHelp = QtWidgets.QTextEdit()
        self.textHelp.setReadOnly(True)
        self.textHelp.setStyleSheet("background:#fafcff;font-size:13px;")
        self.rightLayout.addWidget(self.textHelp)
        
        # 设置右侧部件的宽度
        self.rightWidget.setMinimumWidth(250)
        self.rightWidget.setMaximumWidth(300)
        
        # 将右侧部件添加到主水平布局
        self.horizontalLayout.addWidget(self.rightWidget)
        
        self.retranslateUi(QgisFieldMapperDialogBase)
        QtCore.QMetaObject.connectSlotsByName(QgisFieldMapperDialogBase)

    def retranslateUi(self, QgisFieldMapperDialogBase):
        QgisFieldMapperDialogBase.setWindowTitle("外部数据字段映射/追加到QGIS图层工具")
