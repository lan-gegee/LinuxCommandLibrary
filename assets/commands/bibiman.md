# TAGLINE

带 Vim 风格键位、用于管理 BibLaTeX 数据库的 TUI

# TLDR

浏览**参考文献文件**中的条目

```bibiman [path/to/references.bib]```

同时打开**多个参考文献文件**

```bibiman [file1.bib] [file2.bib]```

递归加载目录下的所有 **.bib 文件**

```bibiman [path/to/directory]```

使用**自定义配置**文件

```bibiman -c [path/to/bibiman.toml] [path/to/file.bib]```

仅加载**命令行指定的文件**，忽略配置

```bibiman -C [path/to/file.bib]```

启用针对**浅色终端**背景优化的配色

```bibiman --light-terminal [path/to/file.bib]```

**设置自定义 PDF 目录**以便将 PDF 与条目匹配

```bibiman --pdf-path [path/to/pdfs] [path/to/file.bib]```

**格式化参考文献文件中的 citekey**

```bibiman format-citekeys [path/to/file.bib]```

# SYNOPSIS

**bibiman** [**-h**|**--help**] [**-v**|**--version**] [**-c** _path_] [**-l** _path_] [**--pdf-path** _path_] [**--light-terminal**] [**-C**] [_file_|_directory_]...

**bibiman** **format-citekeys** [_options_] _file_

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出

**-v**, **--version**
> 打印已安装的版本并退出

**-c**, **--config-file** _path_
> 指定自定义配置文件位置

**-l**, **--log-file** _path_
> 指定自定义日志文件位置

**--pdf-path** _path_
> 设置本次会话中查找 PDF 文件时使用的目录路径

**--light-terminal**
> 启用针对浅色终端背景优化的配色方案

**-C**, **--cli-only**
> 仅加载命令行上指定的文件，忽略配置中定义的任何文件

**format-citekeys**
> 子命令，使用模式语法重新格式化参考文献文件中的 citekey

# DESCRIPTION

**bibiman** 是一个终端用户界面（TUI），用于管理 BibLaTeX 文献数据库，可作为基于终端的科研工作流的一部分。它以 Rust 编写，提供快速、键盘驱动的 .bib 文件交互方式。

界面采用 Vim 风格键位进行导航：**j**/**k** 或方向键在条目间移动，**Ctrl-d**/**Ctrl-u** 按五个条目跳转，**g**/**G** 跳到第一条或最后一条，**h**/**l** 选择列。按 **?** 会弹出包含完整键位参考的帮助窗口。

可以用 **/** 或 **Ctrl-f** 对所有字段进行模糊搜索，或用 **Alt-/** 搜索特定字段。模糊匹配由 nucleo-matcher 引擎提供。特殊前缀可修改匹配行为：**^** 锚定到开头，**$** 锚定到结尾，**'** 强制字面匹配。按 **TAB** 可在条目视图和关键词视图之间切换，从而按关键词过滤。

按 **e** 会在终端编辑器中打开当前条目并定位到正确的行。编辑器依次由配置文件、**VISUAL** 环境变量、**EDITOR** 决定，最后回退到 **vi**。按 **y** 将 citekey 复制到系统剪贴板，**o** 打开关联的 PDF、URL 或 DOI 链接，**n** 创建或打开与该条目关联的笔记文件。可以通过 **a** 经 DOI 查询添加条目。

排序方面：按 **s** 可在作者、标题和年份列之间循环切换排序，或按 **S** 恢复文件中的原始顺序。自定义列可以显示额外元数据，如期刊名、出版商、机构、丛书或出版物类型。

通过传入多个文件参数或一个目录路径，可在单个会话中加载多个 .bib 文件。若给定目录，bibiman 会递归搜索其中的所有 .bib 文件。PDF 文件可通过 BibTeX 的 **file** 字段匹配到条目，也可通过将 citekey 与配置的 PDF 目录中的文件名匹配来关联。

**format-citekeys** 子命令允许在不启动 TUI 的情况下，通过命令行使用可配置的模式语法批量重排 citekey。

# CONFIGURATION

配置文件位于 **$XDG_CONFIG_HOME/bibiman/bibiman.toml**（通常是 ~/.config/bibiman/bibiman.toml）。

```[general]
bibfiles = ["/path/to/references.bib"]
editor = { command = "vim", args = [] }
pdf_opener = "xdg-open"
url_opener = "xdg-open"
pdf_path = "/path/to/pdfs"
note_path = "/path/to/notes"
note_extensions = ["md", "txt"]
custom_column = "pubtype"
clipboard = "wayland"```

**editor** 字段既接受简单字符串，也接受含 **command** 和 **args** 键的表。**custom_column** 字段控制条目列表中显示哪些额外元数据，可设置为 **journaltitle**、**organization**、**institution**、**series**、**publisher** 或 **pubtype**。**clipboard** 字段选择剪贴板提供者：**wayland**、**x-clip**、**x-sel**、**pasteboard**、**tmux** 或 **win32-yank**。

颜色在一个 **[colors]** 小节中配置，可使用 ANSI 颜色名、256 色索引或十六进制码，作用于 **main_text_color**、**highlight_text_color**、**entry_color**、**keyword_color** 和 **popup_bg_color** 等元素。

citekey 格式化规则定义于 **[citekey_formatter]** 小节，选项包括 **fields**、**ascii_only** 和 **case**。

# CAVEATS

citekey 不能包含特殊字符 **/ | # * \ " ' ; !**，因为它们会干扰笔记文件的创建和其他操作。编辑器必须支持 **+line** 参数语法以跳转到指定行。Windows 上对打开 PDF 文件和 URL 的支持未经测试。为了可读性，LaTeX 宏在显示时被隐藏，但在底层 .bib 文件中保持不变。

# HISTORY

**bibiman** 由 **lukeflo** 创建，**2024 年 11 月**首次以 0.7.0 版本发布到 crates.io。首个正式 Codeberg 发布版（v0.15.0）随后于 **2025 年 10 月**推出。该项目以 Rust 编写且不含 AI 生成的代码，采用 GPL-3.0-or-later 许可证，托管在 Codeberg 上。截至 2026 年初，开发仍然活跃：2026 年 1 月发布了 0.19.3 版本，仓库已有超过 376 次提交。

# SEE ALSO

[biber](/man/biber)(1), [bibtex](/man/bibtex)(1), [papis](/man/papis)(1), [latex](/man/latex)(1)

# INSTALL

```nix: nix profile install nixpkgs#bibiman```

<!-- packages: 2026-07-22 -->
