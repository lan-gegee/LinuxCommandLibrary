# TAGLINE

校验并重新格式化 HTML 标记

# TLDR

**清理 HTML 文件**

```tidy [input.html]```

**写入文件**

```tidy -o [output.html] [input.html]```

**原地修改**

```tidy -m [file.html]```

**转换为 XHTML**

```tidy -asxhtml [input.html]```

**只显示错误**

```tidy -e [input.html]```

**缩进输出**

```tidy -i [input.html]```

**安静模式**

```tidy -q [input.html]```

**在指定列处换行**

```tidy -w [80] [input.html]```

# SYNOPSIS

**tidy** [_-o output_] [_-m_] [_-i_] [_options_] [_files_]

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-m**, **--modify**
> 原地修改。

**-i**, **--indent**
> 缩进内容。

**-e**, **--errors**
> 只显示错误。

**-q**, **--quiet**
> 安静模式。

**-w** _N_, **--wrap** _N_
> 在指定列处换行。

**-asxhtml**
> 以 XHTML 格式输出。

**-ashtml**
> 以 HTML 格式输出。

**--indent-spaces** _N_
> 每级缩进的空格数。

# DESCRIPTION

**tidy** 用于校验和重新格式化 HTML 文档，能检测出缺少闭合标签、嵌套不当、使用废弃元素等标记错误。它可以自动修复许多常见问题，同时以统一的缩进和换行生成格式一致的输出。

该工具可将 HTML 转换为更严格、符合 XML 规范的 XHTML（**-asxhtml**），也可用 **-m** 原地重排格式。仅报错模式（**-e**）只报告问题而不修改文档，适合快速校验。输出换行宽度可用 **-w** 标志配置。

# CAVEATS

可能改变空白字符。某些修复会影响渲染效果。复杂页面需谨慎处理。

# HISTORY

**HTML Tidy** 最初由 **W3C** 的 **Dave Raggett** 开发。现由 HTACG（HTML Tidy Advocacy Community Group）维护。

# INSTALL

```apt: sudo apt install tidy```

```dnf: sudo dnf install tidy```

```pacman: sudo pacman -S tidy```

```apk: sudo apk add tidyhtml```

```zypper: sudo zypper install tidy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmllint](/man/xmllint)(1), [prettier](/man/prettier)(1)
