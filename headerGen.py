import argparse
import datetime
import sys

def generate_header():
    parser = argparse.ArgumentParser(
        description="自动生成代码头部责任编辑信息工具（支持对齐与自动边框）",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # 1-2. 注释符号
    parser.add_argument("--ml-comment", nargs=2, metavar=('START', 'END'), help="多行注释首尾符号")
    parser.add_argument("-s", "--sl-comment", default="#", help="单行注释符号")

    # 3-4. 文件名与风格
    parser.add_argument("-f", "--filename", default="mylib", help="文件名标识")
    parser.add_argument("--style", default="-", help="装饰风格符号（如 - = *）")

    # 5. 时间格式
    time_help = (
        "时间格式参考: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes\n"
        "常用: %%Y-%%m-%%d (年-月-日)； %%Y-%%m-%%d %%H:%%M:%%S （年-月-日 时:分:秒）"
    )
    parser.add_argument("-t", "--time-format", default="%Y-%m-%d", help=time_help)

    # 6. 基础信息
    parser.add_argument("--author", default="Admin")
    parser.add_argument("--lang", default="Python")
    parser.add_argument("--email", default="admin@example.com")
    parser.add_argument("--ver", help="版本号")
    parser.add_argument("--compiler", help="编译器版本")

    # 7. 其他信息
    parser.add_argument("--extra", nargs='+', metavar='KEY VALUE', help="成对传入其他项")

    args = parser.parse_args()

    # --- 逻辑处理 ---
    
    # 处理额外参数
    extra_data = []
    if args.extra:
        if len(args.extra) % 2 != 0:
            print("错误: --extra 参数必须成对传入。", file=sys.stderr)
            sys.exit(1)
        extra_data = [(args.extra[i], args.extra[i+1]) for i in range(0, len(args.extra), 2)]

    # 准备所有待打印的键值对
    now = datetime.datetime.now().strftime(args.time_format)
    info_list = [
        ("Author", args.author),
        ("DateTime", now),
        ("Language", args.lang),
        ("Email", args.email)
    ]
    if args.ver: info_list.append(("Version", args.ver))
    if args.compiler: info_list.append(("Compiler", args.compiler))
    info_list.extend(extra_data)

    # 计算最长键的长度（用于冒号对齐）
    max_key_len = max(len(k) for k, v in info_list)
    # 格式化内容行
    content_lines = [f"{k.ljust(max_key_len)} : {v}" for k, v in info_list]
    
    # 计算内容区域的最宽长度
    max_content_len = max(len(line) for line in content_lines)
    # 确保边框能容纳文件名
    box_width = max(max_content_len, len(args.filename)) + 2 

    # --- 构造最终行 ---
    
    final_output = []
    
    # 1. 标题居中
    display_title = f" {args.filename} "
    box_width = max(box_width, len(display_title))
    # 使用 center 方法在 box_width 长度内居中，并用 style 填充
    final_output.append(display_title.center(box_width, args.style))
    
    # 2. 中间信息
    final_output.extend(content_lines)
    
    # 3. 底边框
    final_output.append(args.style * box_width)

    # --- 输出渲染 ---
    if args.ml_comment:
        print(args.ml_comment[0])
        for line in final_output:
            print(line)
        print(args.ml_comment[1])
    else:
        for line in final_output:
            print(f"{args.sl_comment} {line}")

if __name__ == "__main__":
    generate_header()
