

class analyzer():
    """图片分析类"""
    def __init__(self, path):
        self.path = path
        # 从磁盘读取图片二进制字节流数据
        with open(path, 'rb') as f:
            image_data = f.read()
            self.image_data = ['%x' % image_data[i] for i in range(len(image_data))]
        
    @property

# def getMarkerS
# 从磁盘读取图片二进制字节流数据
with open('123.jpg', 'rb') as f:
    image_data = f.read()
    image_data = ['%x' % image_data[i] for i in range(len(image_data))]

# 解析标记数据，保存到字典 tagmarker
tagmarker = dict()
tag = ''
tag_start = False
data_start = False
for i, b in enumerate(image_data):
    if len(b) == 1:
        b = '0' + b
    if b == 'ff':
        tag_start = True
        continue
    if tag_start:
        if b != 'ff' and (b != '00'):            
            tag = 'ff' + b
            if not tag in tagmarker:
                tagmarker[tag] = list()
            tag_start = False
            data_start = True
            continue
        else:
            tag_start = False
            tagmarker[tag].append('ff')
    if data_start:
        tagmarker[tag].append(b)

# 创建字节码对应的标记符
tag_map = {
    "ffd8": "SOI",
    "ffc4": "DHT",
    'ffc8': "JPG",
    'ffcc': "DAC",
    "ffda": "SOS",
    "ffdb": "DQT",
    "ffdc": "DNL",
    "ffdd": "DRI",
    "ffde": "DHP",
    "ffdf": "EXP",
    "fffe": "COM",
    "ff01": "TEM",
    "ffd9": "EOI"
}

for i in range(16):
    tag = 'ffe%x' % i
    tag_map[tag] = 'APP'+str(i)

for i in [0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]:
    tag = 'ffc%x' % i
    tag_map[tag] = 'SOF'+str(i)

for i in range(8):
    tag = 'ffd%x' % i
    tag_map[tag] = 'RST'+str(i)

for i in range(14):
    tag = 'fff%x' % i
    tag_map[tag] = 'JPG'+str(i)

map_tag = { v: k for k, v in tag_map.items() }

print(map_tag)

# 查看解析后，有那些标记数据，以及对应数据的长度
for tag, arr in tagmarker.items():
    s = len(arr)
    if tag in tag_map:
        tag = tag_map[tag]
    if s == 0:
        print(tag)
        continue

    print("{}:\t{}\tbytes".format(tag, s))