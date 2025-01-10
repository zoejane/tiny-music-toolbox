from .constants import (
    NOTES, FLAT_TO_SHARP_MAP, SHARP_TO_FLAT_MAP, 
    SCALE_STEPS, KEY_SIGNATURES, CHORD_TYPES, CHORD_INTERVALS
)

class Theory:
    def __init__(self, key):
        # 处理基本音符大写
        base_note = key[0].upper()
        accidental = key[1:] if len(key) > 1 else ''
        self.key = base_note + accidental
        
        # 将升号调性转换为等价的降号调性
        sharp_to_flat = {
            'C#': 'Db',
            'D#': 'Eb',
            'G#': 'Ab',
            'A#': 'Bb',
        }
        if self.key in sharp_to_flat:
            self.key = sharp_to_flat[self.key]
            
        self._validate_key()
        # 记录是否使用降号表示
        self.use_flats = 'b' in self.key

    def _validate_key(self):
        if self.key not in KEY_SIGNATURES:
            valid_keys = sorted(KEY_SIGNATURES.keys())
            raise ValueError(
                f"无效的调性: '{self.key}'\n"
                f"有效的调性：{', '.join(valid_keys)}"
            )

    def info(self):
        return {
            'key': self.get_key(),
            'scale': self.get_scale(),
            'chords': self.get_chords()
        }

    def get_key(self):
        signatures = KEY_SIGNATURES[self.key]
        return "无" if not signatures else " ".join(signatures)

    def get_scale(self):
        # 获取基准音符的索引
        base_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # 不含升降号的基本音符
        idx = base_notes.index(self.key[0])
        
        # 获取调号中的音符映射
        signatures = KEY_SIGNATURES[self.key]
        note_map = {}
        for note in signatures:
            note_map[note[0]] = note
        
        # 生成音阶
        scale = []
        for i in range(7):  # 大调音阶有7个音符
            note = base_notes[(idx + i) % 7]
            # 如果音符在调号中有对应的升降号形式，使用它
            if note in note_map:
                note = note_map[note]
            scale.append(note)
            
        return scale

    def _roman_to_int(self, roman):
        """将罗马数字转换为阿拉伯数字（1-based）"""
        roman_map = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'i': 1,
            'ii': 2,
            'iii': 3,
            'iv': 4,
            'v': 5,
            'vi': 6,
            'vii': 7,
        }
        return roman_map[roman]

    def get_chords(self):
        scale = self.get_scale()
        chords = {}
        
        # 基本音符列表（不含升降号）
        base_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        
        for degree, chord_type in CHORD_TYPES.items():
            # 获取根音
            degree_num = self._roman_to_int(degree)  # 不再需要 strip('iv')
            root_note = scale[degree_num - 1]
            root_base = root_note[0]  # 基本音符（不含升降号）
            
            # 计算和弦音符
            chord_notes = [root_note]  # 根音
            
            # 三度音（上行3个音）
            third = scale[(degree_num + 1) % 7]
            chord_notes.append(third)
            
            # 五度音（上行5个音）
            fifth = scale[(degree_num + 3) % 7]
            chord_notes.append(fifth)
            
            chords[degree] = {
                'notes': '-'.join(chord_notes),
                'type': chord_type
            }
        return chords

    def __str__(self):
        info = self.info()
        output = [
            f"调性：{self.key} 大调",
            f"调号：{info['key']}",
            f"音阶：{' '.join(info['scale'])}",
            "和弦："
        ]
        
        # 计算最长的和弦音符长度，用于对齐
        max_notes_len = max(len(chord['notes']) for chord in info['chords'].values())
        
        # 格式化和弦输出
        for degree, chord in info['chords'].items():
            output.append(
                f"  {degree:<3} {chord['notes']:<{max_notes_len}}  ({chord['type'].replace('三和弦', '')})"
            )
        return '\n'.join(output) 