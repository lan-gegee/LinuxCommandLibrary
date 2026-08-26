# TAGLINE

免费开源的办公生产力套件，含文字处理器等组件

# TLDR

**打开文档**

```libreoffice [path/to/document]```

**将文档转换为 PDF**

```libreoffice --headless --convert-to pdf [document.docx]```

**转换为其他格式**

```libreoffice --headless --convert-to [xlsx] [spreadsheet.ods]```

**批量转换多个文件**

```libreoffice --headless --convert-to pdf [*.docx]```

**指定输出目录**

```libreoffice --headless --convert-to pdf --outdir [/output] [document.docx]```

**启动 Writer**（文字处理器）

```libreoffice --writer```

**启动 Calc**（电子表格）

```libreoffice --calc```

**启动 Impress**（演示文稿）

```libreoffice --impress```

# SYNOPSIS

**libreoffice** [_--headless_] [_--convert-to format_] [_--outdir path_] [_--writer|--calc|--impress|--draw_] [_options_] [_files_]

# PARAMETERS

**--headless**
> 无 GUI 运行（用于转换/脚本化）。

**--convert-to** _format[:filter]_
> 转换为指定格式后退出。

**--outdir** _path_
> 转换结果文件的输出目录。

**--writer**
> 打开 LibreOffice Writer。

**--calc**
> 打开 LibreOffice Calc。

**--impress**
> 打开 LibreOffice Impress。

**--draw**
> 打开 LibreOffice Draw。

**--math**
> 打开 LibreOffice Math。

**--base**
> 打开 LibreOffice Base。

**--print-to-file** _file_
> 打印到文件而不是打印机。

**--infilter** _filter_
> 强制指定输入过滤器。

**-n**, **--new**
> 打开一个新的空白文档。

**-o**, **--view**
> 以只读模式打开。

**--safe-mode**
> 以安全模式启动（禁用扩展）。

**--nofirststartwizard**
> 跳过首次启动向导。

**--quickstart**
> 启用快速启动器。

**--terminate_after_init**
> 加载完成后即退出（用于测试）。

**--norestore**
> 禁用自动崩溃恢复。

**--nologo**
> 启动时不显示启动画面。

**--nolockcheck**
> 禁用对远程正在运行的实例的检查。

**--invisible**
> 不带任何 UI 启动（无窗口、无托盘图标）。

**--cat** _file_
> 将文档文本内容输出到标准输出，然后退出。

**-p** _file..._
> 将给定文件打印到默认打印机后退出。

**--pt** _printer_ _file..._
> 打印到指定打印机后退出。

**--version**
> 打印版本信息后退出。

**--help**
> 显示帮助。

# CONVERSION FORMATS

**pdf**
> PDF 文档。

**html**
> HTML 网页。

**docx**
> Microsoft Word 2007+。

**doc**
> Microsoft Word 97-2003。

**xlsx**
> Microsoft Excel 2007+。

**xls**
> Microsoft Excel 97-2003。

**pptx**
> Microsoft PowerPoint 2007+。

**odt**
> OpenDocument 文本。

**ods**
> OpenDocument 电子表格。

**csv**
> 逗号分隔值。

**txt**
> 纯文本。

# DESCRIPTION

**LibreOffice** 是一个免费的开源办公生产力套件，包括文字处理器（Writer）、电子表格（Calc）、演示软件（Impress）、绘图应用（Draw）、公式编辑器（Math）和数据库管理器（Base）。

命令行为自动化提供了强大支持。**--headless** 模式可在无 GUI 下运行，这对服务器端文档转换至关重要。结合 **--convert-to** 使用时，可以批量在各种文档格式之间转换——常用于从办公文档生成 PDF。

转换支持过滤器以便精细调整输出。格式:过滤器语法（例如 csv:Text - txt - csv (StarCalc)）可用于指定精确的导出选项。可用过滤器取决于已安装的组件。

在脚本化方面，LibreOffice 支持 Basic、Python、JavaScript 和 BeanShell 宏。UNO API 提供程序化的文档操作能力。配合无头模式，可以构建文档生成流水线。

快速启动器功能会让 LibreOffice 保持部分加载状态，从而加快文档打开速度，适合频繁使用它的系统。

# CAVEATS

无头转换需要完整安装的 LibreOffice。一些复杂文档可能无法完美转换。每次转换都会派生一个独立进程——处理大量文件时请留意内存占用。过滤器语法可能相当复杂。部分功能需要 Java 运行时。

# HISTORY

**LibreOffice** 诞生于 **2010 年**，是 Oracle 收购 Sun Microsystems 之后从 OpenOffice.org 分叉而来。随后成立了 The Document Foundation 来指导开发。它已成为最主要的开源办公套件，默认包含在大多数 Linux 发行版中，也可用于 Windows 和 macOS。

# INSTALL

```dnf: sudo dnf install libreoffice```

```apk: sudo apk add libreoffice-common```

```zypper: sudo zypper install libreoffice```

```nix: nix profile install nixpkgs#libreoffice```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [wkhtmltopdf](/man/wkhtmltopdf)(1), [unoconv](/man/unoconv)(1)
