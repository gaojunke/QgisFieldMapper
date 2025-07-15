# QgisFieldMapper - QGIS Field Mapping Tool

## Introduction

QgisFieldMapper is a QGIS plugin that allows users to map or append external vector data to existing layers. It provides a simple interface for field mapping between the target layer and external data sources.

## Features

- Map or append external vector data to existing QGIS layers
- Support for various vector data formats (SHP, GeoJSON, SQLite, GeoPackage)
- Flexible field mapping between target and external data
- Two operation modes: mapping (clear and replace) or appending
- Compatible with QGIS 3.0 and above
- Support for both loaded layers and local files

## Installation

1. Download the plugin zip file from the GitHub repository
2. In QGIS, go to Plugins > Manage and Install Plugins
3. Click on "Install from ZIP" and select the downloaded file
4. Alternatively, extract the zip file to your QGIS plugins directory:
   - Windows: `C:\Users\{username}\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

## Usage

1. After installation, find the plugin in the QGIS menu under "Field Mapping Tool" or use the toolbar icon
2. Select the target layer (can be a loaded QGIS layer or browse for a local file)
3. Select the external data file (SHP, GeoJSON, etc.)
4. Choose the operation mode (mapping or appending)
5. Set up field mapping relationships (left: target fields, right: external fields)
6. Click "Execute" to perform the operation

## Notes

- The structure of the target layer (field types, order, aliases) remains unchanged
- Field content is filled from external data according to the mapping table
- Geometry is taken from external data
- Supports all QGIS vector layers

## License

This plugin is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
