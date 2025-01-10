import pytest
from tmus.theory import Theory

def test_create_theory():
    """测试创建 Theory 对象"""
    # 有效调性
    assert Theory('C')
    assert Theory('G')
    assert Theory('Bb')
    
    # 无效调性
    with pytest.raises(ValueError):
        Theory('H')  # 不存在的音符
    with pytest.raises(ValueError):
        Theory('B#')  # 无效的升号
        
def test_get_key():
    """测试获取调号"""
    # C大调：无升降号
    assert Theory('C').get_key() == "无"
    
    # G大调：1个升号
    assert Theory('G').get_key() == "F#"
    
    # D大调：2个升号
    assert Theory('D').get_key() == "F# C#"
    
    # F大调：1个降号
    assert Theory('F').get_key() == "Bb"

def test_get_scale():
    """测试获取音阶"""
    # C大调音阶
    scale = Theory('C').get_scale()
    assert scale == ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    
    # G大调音阶
    scale = Theory('G').get_scale()
    assert scale == ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    
    # F大调音阶
    scale = Theory('F').get_scale()
    assert scale == ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']

def test_get_chords():
    """测试获取和弦"""
    # C大调和弦
    chords = Theory('C').get_chords()
    assert chords['I']['notes'] == 'C-E-G'
    assert chords['IV']['notes'] == 'F-A-C'
    assert chords['V']['notes'] == 'G-B-D'
    
    # 检查和弦类型
    assert chords['I']['type'] == '大三和弦'
    assert chords['ii']['type'] == '小三和弦'
    assert chords['iii']['type'] == '小三和弦'

def test_info():
    """测试获取完整信息"""
    info = Theory('C').info()
    assert 'key' in info
    assert 'scale' in info
    assert 'chords' in info
    
def test_str_output():
    """测试字符串输出格式"""
    output = str(Theory('C')).split('\n')
    # 检查基本信息
    assert "调性：C 大调" in output
    assert "调号：无" in output
    assert "音阶：C D E F G A B" in output
    assert "和弦：" in output
    
    # 检查和弦内容（不关心具体格式）
    chord_text = '\n'.join(output)  # 合并所有文本
    assert "C-E-G" in chord_text and "大" in chord_text      # I级
    assert "D-F-A" in chord_text and "小" in chord_text      # ii级
    assert "E-G-B" in chord_text and "小" in chord_text      # iii级
    assert "F-A-C" in chord_text and "大" in chord_text      # IV级
    assert "G-B-D" in chord_text and "大" in chord_text      # V级
    assert "A-C-E" in chord_text and "小" in chord_text      # vi级 