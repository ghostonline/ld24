import zlib
import base64
from xml.etree import ElementTree as ET
import struct

from pyglet import resource

def row_walker(tiles, width):
    row = []
    for tile in tiles:
        row.append(tile)
        if len(row) == width:
            yield tuple(row)
            row = []

def mapreader(filename):
    f = resource.file(filename)
    xml = ET.XML(f.read())
    f.close()
    layer = xml.find("layer")
    width = int(layer.attrib['width'])
    height = int(layer.attrib['height'])
    tilewidth = int(xml.attrib['tilewidth'])
    tileheight = int(xml.attrib['tileheight'])
    data = zlib.decompress(base64.b64decode(xml.find("layer/data").text))
    unpack_format = 'I' * (width * height)
    data = struct.unpack(unpack_format, data)
    rev_tiles = [row for row in row_walker(data, width)]
    tiles = []
    for row in reversed(rev_tiles):
        tiles.extend(row)
    objectlayer = xml.find("objectgroup")
    objects = {'other':[]}
    for obj in objectlayer:
        obj_type = obj.attrib['type']
        x = int(obj.attrib['x']) / tilewidth
        y = height - int(obj.attrib['y']) / tileheight - 1
        data = (x, y)
        if obj_type == 'other':
            objects[obj_type].append(data)
            data = objects[obj_type]
        elif obj_type == 'seed':
            seed = int(obj.attrib['name'])
            data += (seed,)
        objects[obj_type] = data
    return width, height, tiles, objects
