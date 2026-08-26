# TAGLINE

将 ANSI 转义序列转换为 HTML

# TLDR

**将彩色终端输出转换为 HTML**

```ls --color=always | aha > ls.html```

**将 man page 转换为 HTML**（保留格式）

```MAN_KEEP_FORMATTING=1 man command | ul | aha > man.html```

**从文件转换**，使用黑色背景和标题

```aha -f input.txt --black --title "My Log" > output.html```

**处理光标定位序列**（如 htop）

```echo q | htop | aha --black --line-fix > htop.html```

**添加自定义 CSS** 并启用自动换行

```command | aha --css style.css --word-wrap > output.html```

**使用粉色背景**

```command | aha --pink > output.html```

# SYNOPSIS

**aha** [_options_] [_-f file_]

# DESCRIPTION

**aha**（Ansi HTML Adapter）从文件或标准输入读取包含 ANSI SGR 转义序列（颜色、粗体、下划线等）的文本，并将一个完整、符合标准的 HTML 文档写入标准输出。

它常用于在网页上发布彩色终端会话、diff、日志或交互式工具的输出（htop、git、ls --color 等），同时保留原始外观。

aha 支持多种输出定制，例如强制黑色或粉色背景、设置 HTML 文档标题、注入外部 CSS 样式表、启用自动换行，以及输出基于样式表的样式而非内联样式。

# PARAMETERS

**-f**, **--file** _file_
> 从 _file_ 读取输入而不是标准输入。

**-b**, **--black**
> 使用黑底白字背景。

**-p**, **--pink**
> 使用粉色背景。

**-t**, **--title** _title_
> 设置 HTML `<title>`（默认：标准输入或输入文件名）。

**-c**, **--css** _file_
> 链接外部 CSS 样式表（`<link rel="stylesheet" href="...">`）。

**-s**, **--stylesheet**
> 使用样式表而非内联样式。

**-w**, **--word-wrap**
> 启用自动换行以避免水平滚动条。

**-l**, **--line-fix**
> 修正使用控制序列改变光标位置的输入（htop 等工具需要）。属于临时修补；并非对所有程序都有效。

**-n**, **--no-header**
> 不将输出包裹在 `<html>`、`<head>` 和 `<body>` 标签中。

**-r**, **--ignore-cr**
> 忽略回车符（`\r`），否则可能在 HTML 中产生双重换行。

**-i**, **--iso** _X_
> 输出使用 ISO-8859-_X_（1–16）而非 UTF-8。

**-y**, **--style** _STYLE_
> 在其他样式参数之后，将 _STYLE_ 追加到 `<body>` 元素的样式中。

**-L**, **--lang** _LANG_
> 将文档语言设置为 ISO-639-1 代码 _LANG_。

**-x**, **--no-xml**
> 使用 HTML doctype 而非 XML（可能对旧浏览器有帮助）。

**-v**, **--version**
> 输出版本号并退出。

**-h**, **--help**
> 显示帮助。

# CAVEATS

对于根据 stdout 是否为 tty 来改变输出的工具（如 `ls`、`grep`），必须使用 `--color=always` 等选项强制启用颜色。

某些程序（htop、man）会发出额外的控制序列；为了获得最佳效果，可能需要通过 `ul` 管道传输或使用 `--line-fix`。在现代浏览器上，闪烁文本需要 `--stylesheet` 以及自定义的 `.blink` CSS 类。

# INSTALL

```apt: sudo apt install aha```

```dnf: sudo dnf install aha```

```pacman: sudo pacman -S aha```

```apk: sudo apk add aha```

```zypper: sudo zypper install aha```

```brew: brew install aha```

```nix: nix profile install nixpkgs#aha```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ul](/man/ul)(1)

# RESOURCES

```[Source code](https://github.com/theZiz/aha)```

<!-- verified: 2026-07-11 -->
