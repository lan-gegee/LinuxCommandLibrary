# TAGLINE

深度递归文件比较工具

# TLDR

**比较两个文件**

```diffoscope [file1] [file2]```

**比较并输出 HTML 报告**

```diffoscope --html [report.html] [file1] [file2]```

**限制输出深度进行比较**

```diffoscope --max-diff-block-lines [100] [file1] [file2]```

**递归比较目录**

```diffoscope [dir1] [dir2]```

**输出 JSON 报告**

```diffoscope --json [report.json] [file1] [file2]```

**比较 Debian 软件包**

```diffoscope [package1.deb] [package2.deb]```

**排除特定的文件模式**

```diffoscope --exclude "[*.pyc]" [dir1] [dir2]```

# SYNOPSIS

**diffoscope** [_options_] _path1_ _path2_

# PARAMETERS

**--html** _file_
> 将 HTML 报告写入文件。

**--text** _file_
> 将文本报告写入文件。

**--json** _file_
> 将 JSON 报告写入文件。

**--max-diff-block-lines** _n_
> 每个 diff 块的最大行数。

**--max-report-size** _bytes_
> 报告的最大大小。

**--exclude** _pattern_
> 排除匹配模式的文件。

**--exclude-directory-metadata**
> 忽略目录元数据的差异。

**--fuzzy-threshold** _n_
> 模糊匹配阈值（0-400）。

**--new-file**
> 将缺失的文件视为空文件。

**--no-default-limits**
> 移除默认的大小限制。

**--diff-tool** _tool_
> 要使用的外部 diff 工具。

# DESCRIPTION

**diffoscope** 对文件执行深度比较，递归解压归档并检查其内容。与简单的 diff 不同，它能理解文件格式，并显示压缩文件、图像、二进制文件等内部有意义的差异。

该工具支持数百种文件格式：归档（tar、zip、deb、rpm）、二进制（ELF、PE）、图像（PNG、JPEG）、文档（PDF）等等。它在比较前使用专用工具解码每种格式。

diffoscope 的创建目的是调试可复现构建问题，帮助找出同一份源码的两次构建为何产生不同的二进制文件。输出可以是终端文本、用于网页查看的 HTML，或用于程序化处理的 JSON。

# CAVEATS

完整功能需要许多外部工具（binutils、unzip 等）。大文件或深层归档可能处理缓慢。部分专有格式不受支持。大型比较可能占用大量内存。

# HISTORY

diffoscope 由 **Reproducible Builds** 项目于 **2014** 年起创建，主要作者是 **Lunar** 等人。最初名为 "debbindiff"，用于比较 Debian 软件包，后更名并泛化。该工具是可复现构建工作的核心，帮助开发者理解构建差异的原因并消除不确定性来源。

# INSTALL

```dnf: sudo dnf install diffoscope```

```pacman: sudo pacman -S diffoscope```

```apk: sudo apk add diffoscope```

```zypper: sudo zypper install diffoscope```

```brew: brew install diffoscope```

```nix: nix profile install nixpkgs#diffoscope```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [cmp](/man/cmp)(1)
