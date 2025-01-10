# 音符定义（包含所有可能的升降号形式）
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']

# 音符的等价关系
NOTE_EQUIVALENTS = {
    'E#': 'F',
    'B#': 'C',
    'Fb': 'E',
    'Cb': 'B',
}

# 降号到升号的映射
FLAT_TO_SHARP_MAP = {
    'Bb': 'A#',
    'Eb': 'D#',
    'Ab': 'G#',
    'Db': 'C#',
    'Gb': 'F#',
    'Cb': 'B',
    'Fb': 'E',
}

# 升号到降号的映射
SHARP_TO_FLAT_MAP = {v: k for k, v in FLAT_TO_SHARP_MAP.items()}

# 大调音阶步进（全全半全全全半）
SCALE_STEPS = [2, 2, 1, 2, 2, 2, 1]

# 调号信息
KEY_SIGNATURES = {
    'C':  [],
    'G':  ['F#'],
    'D':  ['F#', 'C#'],
    'A':  ['F#', 'C#', 'G#'],
    'E':  ['F#', 'C#', 'G#', 'D#'],
    'B':  ['F#', 'C#', 'G#', 'D#', 'A#'],
    'F#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
    'C#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],
    'F':  ['Bb'],
    'Bb': ['Bb', 'Eb'],
    'Eb': ['Bb', 'Eb', 'Ab'],
    'Ab': ['Bb', 'Eb', 'Ab', 'Db'],
    'Db': ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],
    'Gb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
}

# 和弦类型
CHORD_TYPES = {
    'I':   '大三和弦',
    'ii':  '小三和弦',
    'iii': '小三和弦',
    'IV':  '大三和弦',
    'V':   '大三和弦',
    'vi':  '小三和弦',
}

# 和弦组成音程
CHORD_INTERVALS = {
    '大三和弦': [0, 4, 7],    # 根音、大三度、纯五度
    '小三和弦': [0, 3, 7],    # 根音、小三度、纯五度
} 