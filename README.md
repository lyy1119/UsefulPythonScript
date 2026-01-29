# UsefulPythonScript
Python脚本工具，来自解决日常问题过程中的ai生成、上网搜集或手写

## 使用方法介绍

### 1. addPdfbookmark.py

一个简单的pdf自动加书签脚本。可以添加 **封面** 、 **目录** 、 **正文** 的对应书签。其中正文部分，可以根据标注页码来标记，比如pdf中某一页码是正文第10页，则在书签中标记为10。  

使用如下：  
```bash
python addPdfbookmark.py report.pdf \
  --cover 1 \
  --toc 2 \
  --body-start 3
```
若有封底等，也能指定结束页：  
```bash
python addPdfbookmark.py book.pdf \
  --body-start 5 \
  --body-end 50
```

## 2. fixFileName.py

将以数字排列的文件名 `x.jpg` 补全为三位数，左侧补零。  
例如 `1.jpg` 补全为 `001.jpg` 。  

使用方法：直接在文件相应目录下运行即可。  


## 3. jpg2pdf.py

将一系列jpg文件合并为一个pdf文件。  

**注意，是字典顺序！**

使用方法：直接在文件相应目录下运行即可。  
