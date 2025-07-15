# QgisFieldMapper - QGIS字段映射工具

[English](#english) | [中文](#中文)

## English

### Introduction

QgisFieldMapper is a QGIS plugin that allows users to map or append external vector data to existing layers. It provides a simple interface for field mapping between the target layer and external data sources.

### Features

- Map or append external vector data to existing QGIS layers
- Support for various vector data formats (SHP, GeoJSON, SQLite, GeoPackage)
- Flexible field mapping between target and external data
- Two operation modes: mapping (clear and replace) or appending
- Compatible with QGIS 3.0 and above
- Support for both loaded layers and local files

### Installation

1. Download the plugin zip file from the GitHub repository
2. In QGIS, go to Plugins > Manage and Install Plugins
3. Click on "Install from ZIP" and select the downloaded file
4. Alternatively, extract the zip file to your QGIS plugins directory:
   - Windows: `C:\Users\{username}\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

### Usage

1. After installation, find the plugin in the QGIS menu under "Field Mapping Tool" or use the toolbar icon
2. Select the target layer (can be a loaded QGIS layer or browse for a local file)
3. Select the external data file (SHP, GeoJSON, etc.)
4. Choose the operation mode (mapping or appending)
5. Set up field mapping relationships (left: target fields, right: external fields)
6. Click "Execute" to perform the operation

### Notes

- The structure of the target layer (field types, order, aliases) remains unchanged
- Field content is filled from external data according to the mapping table
- Geometry is taken from external data
- Supports all QGIS vector layers

### License

This plugin is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

---

## 中文

### 简介

QgisFieldMapper（QGIS字段映射工具）是一个QGIS插件，允许用户将外部矢量数据映射或追加到现有图层。它提供了一个简单的界面，用于目标图层和外部数据源之间的字段映射。

### 功能特点

- 将外部矢量数据映射或追加到现有QGIS图层
- 支持多种矢量数据格式（SHP、GeoJSON、SQLite、GeoPackage）
- 灵活的目标和外部数据字段映射
- 两种操作模式：映射（清空并替换）或追加
- 兼容QGIS 3.0及以上版本
- 支持已加载图层和本地文件

### 安装方法

1. 从GitHub仓库下载插件zip文件
2. 在QGIS中，转到"插件">"管理和安装插件"
3. 点击"从ZIP安装"并选择下载的文件
4. 或者，将zip文件解压到QGIS插件目录：
   - Windows: `C:\Users\{用户名}\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

### 使用说明

1. 安装后，在QGIS菜单中的"字段映射工具"下找到插件，或使用工具栏图标
2. 选择本身图层（可以是已加载的QGIS图层或浏览本地文件）
3. 选择外部数据文件（SHP、GeoJSON等）
4. 选择操作模式（映射或追加）
5. 设置字段对应关系（左侧：本身字段，右侧：外部字段）
6. 点击"执行操作"完成

### 注意事项

- 本身图层结构（字段类型、顺序、别名）保持不变
- 字段内容优先用外部数据填充（按映射表）
- 几何形状采用外部数据
- 支持QGIS所有矢量图层

### 许可证

本插件采用GNU通用公共许可证v3.0授权。详情请参阅LICENSE文件。
