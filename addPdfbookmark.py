#!/usr/bin/env python3
import argparse
import pikepdf
from pikepdf import Pdf, Name
from pathlib import Path

def add_outline(pdf_path, output_path,
                cover_page=None,
                toc_page=None,
                body_start=1,
                body_end=None):
    with pikepdf.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)

        # 合法性检查
        if body_start < 1 or body_start > total_pages:
            raise ValueError("正文起始页超出范围")

        if body_end is None:
            body_end = total_pages
        elif body_end < body_start or body_end > total_pages:
            raise ValueError("正文结束页不合法")

        pdf.Root.PageMode = Name.UseOutlines
        with pdf.open_outline() as outline:

            print(f"cover: {cover_page}, toc: {toc_page}, content from {body_start} to {body_end if body_end else total_pages}")
            # 封面
            if cover_page:
                outline.root.append(
                    pikepdf.OutlineItem(
                        "封面", cover_page - 1
                    )
                )

            # 目录
            if toc_page:
                outline.root.append(
                    pikepdf.OutlineItem(
                        "目录", toc_page - 1
                    )
                )

            # 正文

            # 正文分页书签（从 1 开始编号）
            page_number = 1
            for i in range(body_start - 1, body_end):
                oi = pikepdf.OutlineItem(str(page_number), i)
                outline.root.append(oi)
                page_number += 1

        pdf.save(output_path)

def cli():
    parser = argparse.ArgumentParser(
        description="为 PDF 添加封面 / 目录 / 正文书签"
    )
    parser.add_argument("pdf", help="输入 PDF 文件")
    parser.add_argument("-o", "--output", help="输出文件名")
    parser.add_argument("--cover", type=int, help="封面所在页（从 1 开始）")
    parser.add_argument("--toc", type=int, help="目录所在页（从 1 开始）")
    parser.add_argument("--body-start", type=int, required=True,
                        help="正文起始页（从 1 开始）")
    parser.add_argument("--body-end", type=int,
                        help="正文结束页（默认到最后）")

    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    output = args.output or pdf_path.with_stem(pdf_path.stem + "_outlined")

    add_outline(
        pdf_path=pdf_path,
        output_path=output,
        cover_page=args.cover,
        toc_page=args.toc,
        body_start=args.body_start,
        body_end=args.body_end
    )

    print(f"完成：{output}")

if __name__ == "__main__":
    cli()

