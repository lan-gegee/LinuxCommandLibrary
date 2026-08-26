# TAGLINE

检测漫画分格并写入 .cbxy 伴随文件

# TLDR

**检测** CBZ 中的分格并在旁边写入同名的 .cbxy

```cbxy-detect [path/to/book.cbz]```

**将输出写入**显式指定的路径

```cbxy-detect [path/to/book.cbz] -o [path/to/book.cbxy]```

**强制使用 OpenCV** 检测（快速，无需下载模型）

```cbxy-detect [path/to/book.cbz] --engine cv```

**对不规则版式强制使用 ML** 检测

```cbxy-detect [path/to/book.cbz] --engine ml```

**只处理前 N 页**

```cbxy-detect [path/to/book.cbz] --limit [N]```

**写出标注后的预览 JPEG**

```cbxy-detect [path/to/book.cbz] --preview-dir [dir]```

**安装** cbxy 工具

```pip install cbxy```

# SYNOPSIS

**cbxy-detect** [_options_] _comic_

# DESCRIPTION

**cbxy-detect** 在漫画书中查找分格，并在其旁写出一个 **.cbxy** 伴随归档。**.cbxy** 文件是一个按页存放 JSON 的 ZIP 包（思路与 CBZ 相同，只是内容是分格几何信息而非图像）。坐标采用页面的归一化比例（**0–1**），因此缩放后依然有效；数组顺序即为阅读顺序。

输入可以是 **.cbz**、**.cbr**、图片文件夹或单页图片。检测引擎：**auto**（默认）先尝试 OpenCV，当页面看起来不规则（例如出现一整块巨大的分格）时回退到 ML；**cv** 使用传统的基于装订留白的检测（快速，无需下载模型）；**ml** 使用带预训练漫画分格权重的 Ultralytics YOLO（Hugging Face 上的 **mosesb/best-comic-panel-detection**），首次运行 ML 时下载。

属于 **cbxy** Python 软件包的一部分，该包还提供 **cbxy-reader** 和 **cbxy-editor**。

# PARAMETERS

_comic_
> **.cbz**、**.cbr**、图片文件夹或单页图片的路径。

**-o**, **--out** _path_
> 输出 **.cbxy** 的路径（默认：与漫画同名的文件放在其旁边）。

**--engine** **auto**|**cv**|**ml**
> 检测后端（默认：**auto**）。

**--min-area** _fraction_
> 分格面积占页面比例的下限（默认：**0.03**）。

**--gutter** _0-255_
> CV 模式的近白色留白阈值（默认：**230**）。

**--conf** _threshold_
> ML 置信度阈值（默认：**0.25**）。

**--limit** _N_
> 只处理前 N 页。

**--preview-dir** _dir_
> 将标注后的预览 JPEG 写入该文件夹。

# CAVEATS

OpenCV 最适合有清晰白色留白的传统网格版式；无边框或相互重叠的版式往往需要 **--engine ml**，它会在首次使用时下载一个 YOLO 模型。检测质量因扫描质量和页面设计而异——必要时请用 **cbxy-editor** 复查结果。输入归档必须可读；某些 CBR 工具可能需要额外的系统库，具体取决于平台打包方式。

# HISTORY

**cbxy** 是由 **ngafar** 编写的漫画分格几何伴随格式的 Python 参考实现，以 MIT 许可证发布，包含 **cbxy-detect**、**cbxy-reader** 和 **cbxy-editor**。

# SEE ALSO

[cbxy-reader](/man/cbxy-reader)(1), [cbxy-editor](/man/cbxy-editor)(1), [pip](/man/pip)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/ngafar/cbxy)```

```[Documentation](https://github.com/ngafar/cbxy/blob/main/spec/v0.1.0.md)```

<!-- verified: 2026-07-21 -->
