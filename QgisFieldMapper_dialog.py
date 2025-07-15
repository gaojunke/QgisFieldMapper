# coding:utf-8
# 插件主窗口逻辑，带完整注释
from qgis.PyQt.QtWidgets import (
    QDialog, QFileDialog, QMessageBox, QTableWidgetItem, QComboBox
)
from qgis.PyQt.QtCore import Qt
from .QgisFieldMapper_dialog_base import Ui_QgisFieldMapperDialogBase
from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsMapLayer
from qgis.gui import QgsFileWidget

class QgisFieldMapperDialog(QDialog, Ui_QgisFieldMapperDialogBase):
    def filter_vector_layers(self):
        """过滤非矢量图层，只在QgsMapLayerComboBox中显示矢量图层"""
        # 获取所有图层
        all_layers = QgsProject.instance().mapLayers().values()
        # 创建非矢量图层列表
        non_vector_layers = [layer for layer in all_layers if layer.type() != QgsMapLayer.VectorLayer]
        # 设置排除列表
        self.mapLayerComboBox.setExceptedLayerList(non_vector_layers)
    
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setupUi(self)
        
        # 初始化图层选择组件
        self.mapLayerComboBox.setAllowEmptyLayer(True)   # 允许不选择图层
        # 过滤非矢量图层
        self.filter_vector_layers()
        self.mapLayerComboBox.layerChanged.connect(self.on_layer_selection_changed)
        
        # 初始化文件选择组件
        self.fileWidget.setStorageMode(QgsFileWidget.GetFile)
        self.fileWidget.fileChanged.connect(self.on_file_selection_changed)
        
        # 初始化外部数据文件选择组件
        self.externalFileWidget.setStorageMode(QgsFileWidget.GetFile)
        self.externalFileWidget.fileChanged.connect(self.on_external_file_changed)
        
        # 初始化操作模式
        self.cmbMode.addItems(["映射（清空并替换）", "追加（在后追加）"])
        self.btnDo.clicked.connect(self.do_action)
        
        # 临时变量，记录通过文件方式加载的"本身图层"
        self.temp_target_layer = None
        self.external_layer = None
        self.field_map = {}

        # 帮助说明
        self.textHelp.setPlainText(
            "【工具操作说明】\n"
            "1. 选择本身图层（可为QGIS已加载图层，或点击下拉“浏览文件...”选择本地shp/geojson等文件）\n"
            "2. 点击“浏览”选择外部数据文件（shp、geojson等）\n"
            "3. 选择操作模式（映射/追加）\n"
            "4. 设置字段对应关系（左为本身字段，右为外部字段）\n"
            "5. 点击“执行操作”按钮完成\n"
            "注意：\n"
            "- 本身图层结构（字段类型、顺序、别名）保持不变，只更改要素内容\n"
            "- 字段内容优先用外部数据填充（按映射表）\n"
            "- geometry采用外部数据，支持QGIS所有矢量图层\n"
        )

        # 临时变量，记录通过文件方式加载的“本身图层”
        self.temp_target_layer = None
        self.external_layer = None
        self.field_map = {}

    # 旧方法已移除，使用QgsMapLayerComboBox和QgsFileWidget替代

    def get_target_layer(self):
        """
        返回当前选中的"本身图层"对象
        支持QGIS已有图层和临时加载文件型图层
        """
        # 检查是否有选择图层
        selected_layer = self.mapLayerComboBox.currentLayer()
        if selected_layer and isinstance(selected_layer, QgsVectorLayer):
            return selected_layer
        
        # 检查是否有通过文件选择器加载的临时图层
        file_path = self.fileWidget.filePath()
        if file_path and hasattr(self, 'temp_target_layer') and self.temp_target_layer:
            # 文件路径比对
            if file_path == self.temp_target_layer.source():
                return self.temp_target_layer
        return None

    def on_layer_selection_changed(self, layer):
        """
        响应图层选择组件的变更事件
        """
        if layer:
            # 清空文件选择框，避免冲突
            self.fileWidget.setFilePath("")
            self.temp_target_layer = None
            self.update_field_map_table()
    
    def on_file_selection_changed(self, path):
        """
        响应文件选择组件的变更事件
        """
        if path:
            # 清空图层选择框，避免冲突
            self.mapLayerComboBox.setCurrentIndex(-1)
            
            # 以临时图层方式加载
            lyr = QgsVectorLayer(path, f"文件:{path.split('/')[-1]}", "ogr")
            if not lyr.isValid():
                QMessageBox.critical(self, "错误", "图层文件加载失败！")
                self.fileWidget.setFilePath("")
                self.temp_target_layer = None
                return
                
            self.temp_target_layer = lyr
            self.update_field_map_table()
    
    def on_external_file_changed(self, path):
        """
        响应外部数据文件选择的变更事件
        """
        if path:
            self.load_external_layer(path)
            self.update_field_map_table()

    def load_external_layer(self, path):
        """
        加载外部数据为QGIS矢量图层（不添加到QGIS工程，仅内存中用）
        """
        self.external_layer = QgsVectorLayer(path, "external", "ogr")
        if not self.external_layer.isValid():
            QMessageBox.critical(self, "错误", "外部数据加载失败！")
            self.external_layer = None

    def update_field_map_table(self):
        """
        字段对应关系表刷新逻辑。
        左为本身字段，右为外部字段（支持手动调整对应关系）。
        """
        target_layer = self.get_target_layer()
        ext_file = self.externalFileWidget.filePath()
        # 若本身图层或外部数据未选中，清空表格
        if not target_layer or not ext_file:
            self.tableFieldMap.clear()
            return
        self.load_external_layer(ext_file)
        if not self.external_layer:
            self.tableFieldMap.clear()
            return

        target_fields = [f for f in target_layer.fields()]
        ext_fields = [f for f in self.external_layer.fields()]
        self.tableFieldMap.clear()
        self.tableFieldMap.setRowCount(len(target_fields))
        self.tableFieldMap.setColumnCount(2)
        self.tableFieldMap.setHorizontalHeaderLabels(['本身字段', '外部字段'])

        # 构建映射表
        for i, tgt_field in enumerate(target_fields):
            item = QTableWidgetItem(tgt_field.name())
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableFieldMap.setItem(i, 0, item)
            combo = QComboBox()
            combo.addItem("(空)")  # 可不做映射
            match_idx = 0
            for j, ext_field in enumerate(ext_fields):
                combo.addItem(ext_field.name())
                if ext_field.name() == tgt_field.name():
                    match_idx = j+1
            combo.setCurrentIndex(match_idx)
            self.tableFieldMap.setCellWidget(i, 1, combo)

    def get_field_map(self):
        """
        获取当前用户设置的字段映射关系
        返回dict：{目标字段: 外部字段或None}
        """
        field_map = {}
        for i in range(self.tableFieldMap.rowCount()):
            tgt_field = self.tableFieldMap.item(i, 0).text()
            combo = self.tableFieldMap.cellWidget(i, 1)
            ext_field = combo.currentText()
            if ext_field == "(空)":
                field_map[tgt_field] = None
            else:
                field_map[tgt_field] = ext_field
        return field_map

    def do_action(self):
        """
        执行操作：映射或追加
        """
        # 获取本身图层
        target_layer = self.get_target_layer()
        if not target_layer:
            QMessageBox.warning(self, "警告", "请选择本身图层！")
            return

        # 获取外部图层
        external_path = self.externalFileWidget.filePath()
        if not external_path or not self.external_layer:
            QMessageBox.warning(self, "警告", "请选择外部数据！")
            return

        # 获取字段映射关系
        field_map = self.get_field_map()
        if not field_map:
            QMessageBox.warning(self, "警告", "请至少设置一个字段映射关系！")
            return

        # 获取操作模式
        mode = self.cmbMode.currentText()

        # 执行操作
        if "映射" in mode:
            # 映射模式：清空并替换
            self.transfer_features(target_layer, self.external_layer, field_map, clear_target=True)
        else:
            # 追加模式：在后追加
            self.transfer_features(target_layer, self.external_layer, field_map, clear_target=False)

        # 刷新图层
        target_layer.triggerRepaint()
        QMessageBox.information(self, "成功", f"操作完成！")

        # 如果是临时图层，则添加到QGIS
        if self.temp_target_layer and self.temp_target_layer.isValid():
            # 检查是否已经添加
            layer_exists = False
            for layer in QgsProject.instance().mapLayers().values():
                if layer.source() == self.temp_target_layer.source():
                    layer_exists = True
                    break
            if not layer_exists:
                QgsProject.instance().addMapLayer(self.temp_target_layer)
                self.temp_target_layer = None  # 添加后清空临时图层引用

    def transfer_features(self, target_layer, external_layer, field_map, clear_target=False):
        """
        真正的数据拷贝操作。
        支持映射/追加两种模式。字段类型自动适配。
        :param clear_target: 是否清空目标图层（映射模式=True，追加模式=False）
        """
        target_fields = target_layer.fields()
        ext_fields = external_layer.fields()
        ext_field_idx = {f.name(): i for i, f in enumerate(ext_fields)}

        # "映射"模式先清空目标图层
        if clear_target:
            target_layer.startEditing()
            target_layer.dataProvider().truncate()
        else:
            target_layer.startEditing()

        new_feats = []
        for ext_feat in external_layer.getFeatures():
            feat = QgsFeature(target_fields)
            feat.setGeometry(ext_feat.geometry())
            ext_attrs = ext_feat.attributes()
            attrs = []
            for f in target_fields:
                tgt_name = f.name()
                ext_name = field_map.get(tgt_name)
                if ext_name and ext_name in ext_field_idx:
                    ext_value = ext_attrs[ext_field_idx[ext_name]]
                    try:
                        # 尝试类型转换，确保兼容
                        attrs.append(f.convertCompatible(ext_value))
                    except:
                        attrs.append(None)
                else:
                    attrs.append(None)
            feat.setAttributes(attrs)
            new_feats.append(feat)
        r = target_layer.dataProvider().addFeatures(new_feats)
        target_layer.commitChanges()
        return r
