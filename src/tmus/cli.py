import sys
from .theory import Theory

# 返回码
SUCCESS = 0
ERROR = 1

def show_help():
    """显示帮助信息"""
    print("""用法：tmus <调性> [命令]

命令：
  help   - 显示此帮助信息
  key    - 查看调号
  scale  - 查看音阶
  chords - 查看和弦
  
示例：
  tmus C             # 显示 C 大调的所有信息
  tmus D key         # 查看 D 大调的调号
  tmus G scale       # 查看 G 大调的音阶
  tmus A chords      # 查看 A 大调的和弦""")

def main():
    """命令行工具入口
    
    用法：tmus <调性> [key|scale|chords]
    示例：
        tmus C             # 显示所有信息
        tmus D key         # 显示调号
        tmus G scale       # 显示音阶
        tmus A chords      # 显示和弦
    """
    # 检查帮助选项
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        return SUCCESS

    try:
        # 创建理论对象并获取可选的命令参数
        theory = Theory(sys.argv[1])
        command = sys.argv[2] if len(sys.argv) > 2 else None
        
        # 根据命令显示相应信息
        if command == 'key':
            print(theory.get_key())
        elif command == 'scale':
            print(' '.join(theory.get_scale()))
        elif command == 'chords':
            for degree, chord in theory.get_chords().items():
                print(f"  {degree:<4} {chord['notes']:<10} ({chord['type'].replace('三和弦', '')})")
        elif command is None:
            print(theory)  # 显示完整信息
        else:
            print(f"错误：无效的命令 '{command}'")
            print("有效命令：key, scale, chords")
            return ERROR
            
    except ValueError as e:
        print(f"错误：{str(e)}")
        return ERROR
    
    return SUCCESS

if __name__ == '__main__':
    sys.exit(main()) 