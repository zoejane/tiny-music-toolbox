# Tiny Music Toolbox | 小小音乐工具箱

无论是学习音乐、创作旋律，还是探索和弦搭配，Tiny Music Toolbox 都能轻松搞定。  
支持命令行和 Python API，让你的音乐旅程更有趣！(。・∀・)ノ

## 功能介绍

- 快速查找调号：输入任意调性，一秒告诉你升降号信息。
- 探索音阶组成：了解每个音阶的音符，轻松掌握音阶结构。
- 获取和弦搭配：推荐常用和弦，帮你更好地编曲和创作。
- 双重使用方式：支持命令行操作，或者用 Python API 深度集成到你的项目中。

## 快速开始

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
theory.info()         # 显示 C 大调的所有信息（调号、音阶、和弦）
theory.get_key()      # 显示调号（如：升号 F# C#）
theory.get_scale()    # 显示音阶（如：C D E F G A B）
theory.get_chords()   # 显示和弦（如：I: C-E-G, IV: F-A-C, V: G-B-D）
```

## 使用示例

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

## 开发计划 

- 和弦进行推荐：根据调性推荐和弦进程，为创作提供灵感。
- 移调工具：轻松将旋律或和弦移调到任意调性。
- 网页可视化界面：用图形化界面展示调号、音阶和和弦。
- 更多音乐理论支持：加入更多和弦种类、调式和音乐概念。

## 参与贡献

欢迎加入这个小项目：

- 发现 bug？来提 Issue
- 想要新功能？来提 Issue
- 代码改进？欢迎 PR
- 建议或疑问？欢迎提 Issue 

感谢每一位参与和支持的小伙伴 (◍•ᴗ•◍)

## Changelog

- 20250109 zoejane init