# Tiny Music Toolbox | 小小音乐工具箱

[English](#english) | [中文](#中文)

<a name="english"></a>
## Tiny Music Toolbox

A simple music theory toolbox for learning music, composing melodies, and exploring chord progressions.  
Supports both command-line and Python API to make your music journey more enjoyable! (。・∀・)ノ

### Features

- Key Signatures: Quick access to sharp/flat information
- Scales: Learn the notes in each key
- Chords: Reference for common chord progressions
- Supports both CLI and Python API

### Quick Start

```bash
# Installation
pip install tmus

# Command Line Usage
tmus C             # View all info for C major
tmus D key         # View key signature
tmus G scale       # View scale: G A B C D E F#
tmus A chords      # View chords: I ii iii IV V vi
```

```python
# Python Usage
from tmus import Theory

theory = Theory('C')
theory.info()         # Show all info (key signature, scale, chords)
theory.get_key()      # Show key signature (e.g., sharps: F# C#)
theory.get_scale()    # Show scale (e.g., C D E F G A B)
theory.get_chords()   # Show chords (e.g., I: C-E-G, IV: F-A-C, V: G-B-D)
```

### Examples

```bash
# View All Information
$ tmus C
Key: C major
Signature: none
Scale: C D E F G A B
Chords:
  I:   C-E-G     (maj)
  ii:  D-F-A     (min)
  iii: E-G-B     (min)
  IV:  F-A-C     (maj)
  V:   G-B-D     (maj)
  vi:  A-C-E     (min)

# View Key Signature
$ tmus D key
Sharps: F# C#

# View Scale
$ tmus G scale
G A B C D E F#

# View Chords
$ tmus A chords
I:   A-C#-E    (maj)
ii:  B-D-F#    (min)
iii: C#-E-G#   (min)
IV:  D-F#-A    (maj)
V:   E-G#-B    (maj)
vi:  F#-A-C#   (min)
```

### Roadmap

- Chord Progressions: Smart progression recommendations
- Transposition: Quick key changes
- Web Interface: Visual operations
- Music Theory: More concept support

### Contributing

Welcome to join this project:

- Found a bug? Open an issue
- Want a feature? Open an issue
- Code improvements? PRs welcome
- Questions? Open an issue

Thanks to all contributors! (◍•ᴗ•◍)

---

<a name="中文"></a>
## 小小音乐工具箱

无论是学习音乐、创作旋律，还是探索和弦搭配，Tiny Music Toolbox 都能轻松搞定。  
支持命令行和 Python API，让你的音乐旅程更有趣！(。・∀・)ノ

### 功能介绍

- 查看调号：快速获取升降号信息
- 音阶组成：了解每个调的音符构成
- 和弦推荐：常用和弦搭配参考
- 支持命令行和 Python API

### 快速开始

```bash
# 安装
pip install tmus

# 命令行使用
tmus C             # 查看 C 大调的所有信息
tmus D key         # 查看调号：升降记号
tmus G scale       # 查看音阶：G A B C D E F#
tmus A chords      # 查看和弦：I ii iii IV V vi
```

```python
# Python 使用
from tmus import Theory

theory = Theory('C')
theory.info()         # 显示所有信息（调号、音阶、和弦）
theory.get_key()      # 显示调号（如：升号 F# C#）
theory.get_scale()    # 显示音阶（如：C D E F G A B）
theory.get_chords()   # 显示和弦（如：I: C-E-G, IV: F-A-C, V: G-B-D）
```

### 使用示例

```bash
# 查看完整信息
$ tmus C
调性：C 大调
调号：无
音阶：C D E F G A B
和弦：
  I:   C-E-G     (大)
  ii:  D-F-A     (小)
  iii: E-G-B     (小)
  IV:  F-A-C     (大)
  V:   G-B-D     (大)
  vi:  A-C-E     (小)

# 查看调号
$ tmus D key
升号：F# C#

# 查看音阶
$ tmus G scale
G A B C D E F#

# 查看和弦
$ tmus A chords
I:   A-C#-E    (大)
ii:  B-D-F#    (小)
iii: C#-E-G#   (小)
IV:  D-F#-A    (大)
V:   E-G#-B    (大)
vi:  F#-A-C#   (小)
```

### 开发计划

- 和弦进行：智能推荐和弦进程
- 移调工具：快速转换调性
- 网页界面：可视化操作
- 音乐理论：更多概念支持

### 参与贡献

欢迎加入这个小项目：

- 发现 bug？来提 Issue
- 想要新功能？来提 Issue
- 代码改进？欢迎 PR
- 建议或疑问？欢迎提 Issue

感谢每一位参与和支持的小伙伴 (◍•ᴗ•◍)

## Changelog

- 20250109 zoejane init