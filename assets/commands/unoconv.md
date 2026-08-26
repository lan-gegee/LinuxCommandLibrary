# TAGLINE

借助 LibreOffice 在不同格式之间转换文档

# TLDR

**将文档转换为 PDF**

```unoconv -f pdf [document.docx]```

**转换为指定格式**

```unoconv -f [odt] [document.docx]```

**转换多个文件**

```unoconv -f pdf [*.docx]```

**输出到指定目录**

```unoconv -o [/output/dir] -f pdf [document.docx]```

**启动监听守护进程**

```unoconv --listener &```

**列出可用的输出格式**

```unoconv --show```

**使用导出选项转换**

```unoconv -f pdf -e PageRange=[1-5] [document.docx]```

**从 stdin 读取，写入 stdout**

```cat [doc.docx] | unoconv --stdin --stdout -f pdf > [output.pdf]```

# SYNOPSIS

**unoconv** [_options_] _file_...

**unoconv** **--listener** [_options_]

# PARAMETERS

**-f**, **--format** _format_
> 输出格式（默认：pdf）。

**-o**, **--output** _path_
> 输出目录或文件名。

**-e**, **--export** _option_
> 导出过滤器选项（例如 PageRange=1-5）。

**-i**, **--import** _option_
> 导入过滤器选项。

**-t**, **--template** _file_
> 用于导入样式的模板。

**-l**, **--listener**
> 以监听守护进程方式启动。

**-p**, **--port** _port_
> 监听端口（默认：2002）。

**--server** _address_
> 监听的服务器地址。

**-n**, **--no-launch**
> 找不到监听器时也不启动自己的。

**--stdin**
> 从 stdin 读取输入。

**--stdout**
> 将输出写入 stdout。

**--show**
> 列出可用的输出格式。

**-T**, **--timeout** _seconds_
> 连接超时时间。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**unoconv** 是一个基于 LibreOffice/OpenOffice 的命令行文档转换器。它可以在 LibreOffice 支持的任意格式之间转换，包括 DOC、DOCX、ODT、PDF、HTML、TXT 等众多格式。

该工具通过 UNO 绑定与 LibreOffice 实例通信。如果没有正在运行的监听器，unoconv 会自动启动一个临时实例。对于批处理，请用 --listener 启动持久监听器。

导出选项允许对输出进行微调，例如 PDF 的页码范围或图像质量设置。模板可以在多次转换中应用一致的样式。

注意：新实现建议改用 unoserver，unoconv 已被弃用。

# CAVEATS

需要安装 LibreOffice。首次转换时 LibreOffice 启动可能较慢。某些格式组合的保真度可能有限。新项目请考虑使用 unoserver。

# HISTORY

**unoconv** 由 Dag Wieers 创建，旨在通过命令行使用 LibreOffice 的转换能力。它曾被广泛用于自动化文档处理。该项目目前处于维护模式，由 unoserver 接替。

# INSTALL

```dnf: sudo dnf install unoconv```

```pacman: sudo pacman -S unoconv```

```zypper: sudo zypper install unoconv```

```brew: brew install unoconv```

```nix: nix profile install nixpkgs#unoconv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libreoffice](/man/libreoffice)(1), [pandoc](/man/pandoc)(1), [soffice](/man/soffice)(1)
