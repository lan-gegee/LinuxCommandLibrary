# TAGLINE

将 RTF 转换为其他格式的转换器

# TLDR

将 RTF 文件转换为 **HTML**

```unrtf --html [document.rtf] > [document.html]```

将 RTF 文件转换为**纯文本**

```unrtf --text [document.rtf] > [document.txt]```

将 RTF 文件转换为 **LaTeX**

```unrtf --latex [document.rtf] > [document.tex]```

不提取**内嵌图片**进行转换

```unrtf --nopict --html [document.rtf] > [document.html]```

以**详细输出**模式转换

```unrtf --verbose --html [document.rtf]```

从 **stdin** 转换

```cat [document.rtf] | unrtf --text```

# SYNOPSIS

**unrtf** [_--html_|_--text_|_--vt_|_--latex_|_--rtf_] [_options_] [_file..._]

# PARAMETERS

**--html**
> 选择 HTML 输出（默认）

**--text**
> 选择纯 ASCII 文本输出

**--vt**
> 选择带 VT100 终端转义码的文本输出

**--latex**
> 选择 LaTeX 文档输出

**--rtf**
> 选择 RTF 输出（通常比输入更紧凑）

**--nopict**
> 禁用将内嵌图片提取到当前目录

**--noremap**
> 禁用字符集转换（仅适用于 8 位字符集）

**--verbose**
> 打印额外的处理信息

**--quiet**
> 抑制输出中的前导注释

**-t** _tags_file_
> 指定要使用的输出配置文件

**-P** _config_search_path_
> 指定搜索配置文件的目录（冒号分隔）。默认为 /usr/share/unrtf/

**--version**
> 打印程序版本

**--help**
> 显示帮助信息

# DESCRIPTION

**unrtf** 是一个 GNU 命令行转换器，可将 **富文本格式（RTF）**文档转换为 HTML、纯文本、LaTeX 和 VT100 转义文本等其他格式。它支持表格、字体、超链接、段落对齐以及前景色和背景色。除非用 **--nopict** 禁用，内嵌图片会被提取为单独的文件。未指定文件时，unrtf 从标准输入读取，输出写入标准输出。

自 0.21.0 版起，所有代码页转换都通过 **iconv** 库完成，输出控制由运行时配置文件管理，因此具有高度可定制性。

# CONFIGURATION

输出由位于 **/usr/share/unrtf/** 的运行时配置文件控制。可用 **-t** 指定自定义标签文件，用 **-P** 指定备用搜索路径。SYMBOL 字体映射存储在 **/usr/share/unrtf/SYMBOL.charmap** 中。

# CAVEATS

较旧版本曾发现多个安全漏洞（CVE），包括处理恶意构造的 RTF 文件时的越界内存访问。请始终使用最新版本。**--noremap** 选项仅适用于 8 位字符集。PostScript 输出因缺陷在 0.19.5 版中被移除。并非所有 RTF 特性都得到完全支持；含有高级格式或不常见编码的复杂文档可能无法完美转换。

# HISTORY

最初由 **Zachary T. Smith** 在 **2000 年**前后编写，当时名为 **rtf2htm**，后更名为 **UnRTF**，并被自由软件基金会采纳为官方 **GNU 项目**。其他贡献者包括 David F. Davey 和 Jean-Francois Dockes。最新发布版本为 **0.21.11**。基于 **GNU 通用公共许可证** 授权。

# INSTALL

```apt: sudo apt install unrtf```

```dnf: sudo dnf install unrtf```

```pacman: sudo pacman -S unrtf```

```apk: sudo apk add unrtf```

```brew: brew install unrtf```

```nix: nix profile install nixpkgs#unrtf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [iconv](/man/iconv)(1), [enscript](/man/enscript)(1)
