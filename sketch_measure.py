# -*- coding: utf-8 -*-
'''
Sketch Measure
Author: Hu, Ying-Hao (hyinghao@hotmail.com)
Version: 0.2
Last modification date: 2021-09-15
Copyright 2021 Hu, Ying-Hao

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

import json
import os


# Following codes are generated automatically by 
# prototype.py v0.2 (2021-SEP) 
# Hu, Ying-Hao (hyinghao@hotmail.com)


class BaseObject:
    def __init__(self):
        pass
    def _get_value(self, data, key, defaultValue):
        if data != None and key in data:
            return data[key]
        else:
            return defaultValue
    def _as_dict(self, obj):
        if obj is None:
            return None
        else:
            return obj.as_dict()

# path: /
class SketchMeasure(BaseObject):
    @staticmethod
    def load(filename):
        if filename.endswith("json"):
            with open(filename, "r") as f:
                data = json.loads(f.read())
            return SketchMeasure(data)
        else:
            with open(filename, "r") as f:
                lines = f.read()
                lines = lines[lines.find("$(function(){ SMApp("):].split("\n")[0][20:-5]
                data = json.loads(lines)
            return SketchMeasure(data)
    
    @staticmethod
    def save(sm, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(sm, indent=2))
    
    def __init__(self, data=None):
        super(SketchMeasure, self).__init__()
        self.scale = self._get_value(data, 'scale', "") # scale : str
        self.unit = self._get_value(data, 'unit', "") # unit : str
        self.colorFormat = self._get_value(data, 'colorFormat', "") # colorFormat : str
        if data != None and 'artboards' in data:
            self.artboards = [ Artboard(data['artboards'][i]) for i in range(len(data['artboards']))]  # artboards : list
        else:
            self.artboards = []
        if data != None and 'slices' in data:
            self.slices = [ Slice(data['slices'][i]) for i in range(len(data['slices']))]  # slices : list
        else:
            self.slices = []
        self.colors = self._get_value(data, 'colors', None) # colors : list

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'scale': self.scale,
            'unit': self.unit,
            'colorFormat': self.colorFormat,
            'artboards': [self.artboards[i].as_dict() for i in range(len(self.artboards))],
            'slices': [self.slices[i].as_dict() for i in range(len(self.slices))],
            'colors': self.colors,
        }

# path: /SketchMeasure
class Artboard(BaseObject):
    def __init__(self, data=None):
        super(Artboard, self).__init__()
        if data != None and 'layers' in data:
            self.layers = [ Layer(data['layers'][i]) for i in range(len(data['layers']))]  # layers : list
        else:
            self.layers = []
        self.notes = self._get_value(data, 'notes', None) # notes : list
        self.pageName = self._get_value(data, 'pageName', "") # pageName : str
        self.pageObjectID = self._get_value(data, 'pageObjectID', "") # pageObjectID : str
        self.name = self._get_value(data, 'name', "") # name : str
        self.slug = self._get_value(data, 'slug', "") # slug : str
        self.objectID = self._get_value(data, 'objectID', "") # objectID : str
        self.width = self._get_value(data, 'width', 0) # width : int
        self.height = self._get_value(data, 'height', 0) # height : int
        self.imagePath = self._get_value(data, 'imagePath', "") # imagePath : str

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'layers': [self.layers[i].as_dict() for i in range(len(self.layers))],
            'notes': self.notes,
            'pageName': self.pageName,
            'pageObjectID': self.pageObjectID,
            'name': self.name,
            'slug': self.slug,
            'objectID': self.objectID,
            'width': self.width,
            'height': self.height,
            'imagePath': self.imagePath,
        }

# path: /SketchMeasure/artboards
class Layer(BaseObject):
    def __init__(self, data=None):
        super(Layer, self).__init__()
        self.objectID = self._get_value(data, 'objectID', "") # objectID : str
        self._type = self._get_value(data, 'type', "") # type : str
        self.name = self._get_value(data, 'name', "") # name : str
        if data != None and 'rect' in data:
            self.rect = Rect(data['rect']) # rect : dict
        else:
            self.rect = None
        self.rotation = self._get_value(data, 'rotation', 0) # rotation : int
        self.radius = self._get_value(data, 'radius', 0) # radius : int
        self.borders = self._get_value(data, 'borders', None) # borders : list
        self.fills = self._get_value(data, 'fills', None) # fills : list
        if data != None and 'shadows' in data:
            self.shadows = [ Shadow(data['shadows'][i]) for i in range(len(data['shadows']))]  # shadows : list
        else:
            self.shadows = []
        self.opacity = self._get_value(data, 'opacity', 0) # opacity : int
        self.styleName = self._get_value(data, 'styleName', "") # styleName : str
        self.css = self._get_value(data, 'css', None) # css : list
        if data != None and 'exportable' in data:
            self.exportable = [ Exportable(data['exportable'][i]) for i in range(len(data['exportable']))]  # exportable : list
        else:
            self.exportable = []
        self.content = self._get_value(data, 'content', "") # content : str
        if data != None and 'color' in data:
            self.color = Color(data['color']) # color : dict
        else:
            self.color = None
        self.fontSize = self._get_value(data, 'fontSize', 0) # fontSize : int
        self.fontFace = self._get_value(data, 'fontFace', "") # fontFace : str
        self.textAlign = self._get_value(data, 'textAlign', "") # textAlign : str
        self.letterSpacing = self._get_value(data, 'letterSpacing', 0) # letterSpacing : int
        self.lineHeight = self._get_value(data, 'lineHeight', 0) # lineHeight : int

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'objectID': self.objectID,
            'type': self._type,
            'name': self.name,
            'rect': self._as_dict(self.rect),
            'rotation': self.rotation,
            'radius': self.radius,
            'borders': self.borders,
            'fills': self.fills,
            'shadows': [self.shadows[i].as_dict() for i in range(len(self.shadows))],
            'opacity': self.opacity,
            'styleName': self.styleName,
            'css': self.css,
            'exportable': [self.exportable[i].as_dict() for i in range(len(self.exportable))],
            'content': self.content,
            'color': self._as_dict(self.color),
            'fontSize': self.fontSize,
            'fontFace': self.fontFace,
            'textAlign': self.textAlign,
            'letterSpacing': self.letterSpacing,
            'lineHeight': self.lineHeight,
        }

# path: /SketchMeasure/artboards/layers
class Border(BaseObject):
    def __init__(self, data=None):
        super(Border, self).__init__()
        self.fillType = self._get_value(data, 'fillType', "") # fillType : str
        self.position = self._get_value(data, 'position', "") # position : str
        self.thickness = self._get_value(data, 'thickness', 0) # thickness : int
        if data != None and 'color' in data:
            self.color = Color(data['color']) # color : dict
        else:
            self.color = None

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'fillType': self.fillType,
            'position': self.position,
            'thickness': self.thickness,
            'color': self._as_dict(self.color),
        }

# path: /SketchMeasure/artboards/layers/shadows
# path: /SketchMeasure/artboards/layers/fills/gradient/colorStops
# path: /SketchMeasure/artboards/layers/fills
# path: /SketchMeasure/artboards/layers
# path: /SketchMeasure/artboards/layers/borders
class Color(BaseObject):
    def __init__(self, data=None):
        super(Color, self).__init__()
        self.r = self._get_value(data, 'r', 0) # r : int
        self.g = self._get_value(data, 'g', 0) # g : int
        self.b = self._get_value(data, 'b', 0) # b : int
        self.a = self._get_value(data, 'a', 0) # a : int
        self.colorHex = self._get_value(data, 'color-hex', "") # color-hex : str
        self.argbHex = self._get_value(data, 'argb-hex', "") # argb-hex : str
        self.cssRgba = self._get_value(data, 'css-rgba', "") # css-rgba : str
        self.uiColor = self._get_value(data, 'ui-color', "") # ui-color : str

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'r': self.r,
            'g': self.g,
            'b': self.b,
            'a': self.a,
            'color-hex': self.colorHex,
            'argb-hex': self.argbHex,
            'css-rgba': self.cssRgba,
            'ui-color': self.uiColor,
        }

# path: /SketchMeasure/slices
# path: /SketchMeasure/artboards/layers
class Exportable(BaseObject):
    def __init__(self, data=None):
        super(Exportable, self).__init__()
        self.name = self._get_value(data, 'name', "") # name : str
        self.format = self._get_value(data, 'format', "") # format : str
        self.path = self._get_value(data, 'path', "") # path : str

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'name': self.name,
            'format': self.format,
            'path': self.path,
        }

# path: /SketchMeasure/artboards/layers
class Fill(BaseObject):
    def __init__(self, data=None):
        super(Fill, self).__init__()
        self.fillType = self._get_value(data, 'fillType', "") # fillType : str
        if data != None and 'color' in data:
            self.color = Color(data['color']) # color : dict
        else:
            self.color = None
        if data != None and 'gradient' in data:
            self.gradient = Gradient(data['gradient']) # gradient : dict
        else:
            self.gradient = None

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'fillType': self.fillType,
            'color': self._as_dict(self.color),
            'gradient': self._as_dict(self.gradient),
        }

# path: /SketchMeasure/artboards/layers/fills
class Gradient(BaseObject):
    def __init__(self, data=None):
        super(Gradient, self).__init__()
        self._type = self._get_value(data, 'type', "") # type : str
        if data != None and 'from' in data:
            self._from = GradientPos(data['from']) # from : dict
        else:
            self._from = None
        if data != None and 'to' in data:
            self.to = GradientPos(data['to']) # to : dict
        else:
            self.to = None
        if data != None and 'colorStops' in data:
            self.colorStops = [ ColorStop(data['colorStops'][i]) for i in range(len(data['colorStops']))]  # colorStops : list
        else:
            self.colorStops = []

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'type': self._type,
            'from': self._as_dict(self._from),
            'to': self._as_dict(self.to),
            'colorStops': [self.colorStops[i].as_dict() for i in range(len(self.colorStops))],
        }

# path: /SketchMeasure/artboards/layers/fills/gradient
class ColorStop(BaseObject):
    def __init__(self, data=None):
        super(ColorStop, self).__init__()
        if data != None and 'color' in data:
            self.color = Color(data['color']) # color : dict
        else:
            self.color = None
        self.position = self._get_value(data, 'position', 0) # position : int

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'color': self._as_dict(self.color),
            'position': self.position,
        }

# path: /SketchMeasure/artboards/layers/fills/gradient
# path: /SketchMeasure/artboards/layers/fills/gradient
class GradientPos(BaseObject):
    def __init__(self, data=None):
        super(GradientPos, self).__init__()
        self.x = self._get_value(data, 'x', 0) # x : int
        self.y = self._get_value(data, 'y', 0) # y : int

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'x': self.x,
            'y': self.y,
        }

# path: /SketchMeasure/slices
# path: /SketchMeasure/artboards/layers
class Rect(BaseObject):
    def __init__(self, data=None):
        super(Rect, self).__init__()
        self.x = self._get_value(data, 'x', 0) # x : int
        self.y = self._get_value(data, 'y', 0) # y : int
        self.width = self._get_value(data, 'width', 0) # width : int
        self.height = self._get_value(data, 'height', 0) # height : int
        self.maxX = self._get_value(data, 'maxX', 0) # maxX : int
        self.maxY = self._get_value(data, 'maxY', 0) # maxY : int

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'maxX': self.maxX,
            'maxY': self.maxY,
        }

# path: /SketchMeasure/artboards/layers
class Shadow(BaseObject):
    def __init__(self, data=None):
        super(Shadow, self).__init__()
        self._type = self._get_value(data, 'type', "") # type : str
        self.offsetX = self._get_value(data, 'offsetX', 0) # offsetX : int
        self.offsetY = self._get_value(data, 'offsetY', 0) # offsetY : int
        self.blurRadius = self._get_value(data, 'blurRadius', 0) # blurRadius : int
        self.spread = self._get_value(data, 'spread', 0) # spread : int
        if data != None and 'color' in data:
            self.color = Color(data['color']) # color : dict
        else:
            self.color = None

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'type': self._type,
            'offsetX': self.offsetX,
            'offsetY': self.offsetY,
            'blurRadius': self.blurRadius,
            'spread': self.spread,
            'color': self._as_dict(self.color),
        }

# path: /SketchMeasure
class Slice(BaseObject):
    def __init__(self, data=None):
        super(Slice, self).__init__()
        self.name = self._get_value(data, 'name', "") # name : str
        self.objectID = self._get_value(data, 'objectID', "") # objectID : str
        if data != None and 'rect' in data:
            self.rect = Rect(data['rect']) # rect : dict
        else:
            self.rect = None
        if data != None and 'exportable' in data:
            self.exportable = [ Exportable(data['exportable'][i]) for i in range(len(data['exportable']))]  # exportable : list
        else:
            self.exportable = []

    def __str__(self):
        return str(self.as_dict())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            'name': self.name,
            'objectID': self.objectID,
            'rect': self._as_dict(self.rect),
            'exportable': [self.exportable[i].as_dict() for i in range(len(self.exportable))],
        }

