# TAGLINE

扫描字体文件和目录

# TLDR

在目录中**扫描**字体

```fc-scan [/usr/share/fonts]```

**扫描单个字体**

```fc-scan [font.ttf]```

**以指定格式输出**

```fc-scan --format '%{family}: %{file}\n' [directory]```

# SYNOPSIS

**fc-scan** [_options_] _files_...

# PARAMETERS

_FILES_
> 要扫描的字体文件或目录。目录会被递归扫描。

**-f**, **--format** _FORMAT_
> 输出格式字符串。

**-V**, **--version**
> 显示程序版本并退出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**fc-scan** 扫描字体文件和目录，以 fontconfig 格式显示字体信息。与检查单个文件的 fc-query 不同，fc-scan 可以处理目录和多个文件。

该工具输出 fontconfig 用于字体匹配的字体模式。自定义格式字符串可提取特定属性。给定目录时，它会递归扫描整个目录树。

fc-scan 可用于清点字体、查找重复字体，或为文档生成字体列表。

# CAVEATS

不会更新系统字体缓存。大型目录可能耗时。格式字符串语法可能较复杂。

# HISTORY

fc-scan 是 **fontconfig** 的一部分，提供批量字体扫描能力。它与 fc-query 互补，可在不影响系统字体配置的情况下检查字体。

# INSTALL

```apt: sudo apt install fontconfig```

```dnf: sudo dnf install fontconfig```

```pacman: sudo pacman -S fontconfig```

```apk: sudo apk add fontconfig```

```zypper: sudo zypper install fontconfig```

```brew: brew install fontconfig```

```nix: nix profile install nixpkgs#fontconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-query](/man/fc-query)(1), [fc-list](/man/fc-list)(1), [fc-cache](/man/fc-cache)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/fontconfig/fontconfig)```

```[Homepage](https://www.freedesktop.org/wiki/Software/fontconfig/)```

<!-- verified: 2026-07-15 -->
