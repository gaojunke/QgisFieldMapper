# 插件入口，QGIS自动调用
def classFactory(iface):
    from .QgisFieldMapper import QgisFieldMapper
    return QgisFieldMapper(iface)
