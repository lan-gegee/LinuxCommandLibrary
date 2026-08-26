# TAGLINE

处理 Gremlin 图形的 groff 预处理器

# TLDR

**处理 gremlin 文件**

```grn [file.grn] | groff > output.ps```

**指定宏文件目录**

```grn -M [macrodir] [file.grn]```

**兼容模式**

```grn -C [file.grn]```

# SYNOPSIS

**grn** [_options_] [_file_]

# PARAMETERS

_FILE_
> Gremlin 输入文件。

**-M** _DIR_
> 宏目录。

**-C**
> 与旧版本兼容的模式。

**-F** _FILE_
> 字体文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grn** 是一个用于 Gremlin 图形文件的 groff 预处理器。它将 Gremlin 矢量图形格式转换为 groff 命令，以便在文档中嵌入线条图和文字。

该工具最初为 SunView 开发，后来被移植到 groff。它可以处理线条图、文本标签及其他 Gremlin 图元。

# CAVEATS

属于 groff 套件。Gremlin 格式已基本过时。仅限于基本矢量图形。

# HISTORY

grn 由 **加州大学伯克利分校（UC Berkeley）** 为 Gremlin 绘图程序创建，后来为了兼容性被收入 **GNU groff**。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [pic](/man/pic)(1), [grap](/man/grap)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

<!-- verified: 2026-07-17 -->
