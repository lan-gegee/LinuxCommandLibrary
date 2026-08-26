# TAGLINE

将 GXL 转换为 Graphviz DOT 格式

# TLDR

**将 GXL 转换为 DOT**

```gxl2gv [input.gxl] -o [output.gv]```

**输出到标准输出**

```gxl2gv [input.gxl]```

**处理多个文件**

```gxl2gv [file1.gxl] [file2.gxl] -o [output.gv]```

# SYNOPSIS

**gxl2gv** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入的 GXL 文件。

**-o** _FILE_
> 输出的 DOT 文件。

**-d**
> 输出有向图。

**-?**
> 显示帮助信息。

# DESCRIPTION

**gxl2gv** 在以 GXL（Graph eXchange Language）表示的图与以 GV 语言表示的图之间进行转换。它可以将基于 XML 的图数据导入 Graphviz 生态。

除非通过标志指定转换类型，否则 gxl2gv 会根据输入文件的后缀推断转换类型：".gv" 后缀表示从 GV 转换为 GXL，".gxl" 后缀表示从 GXL 转换为 GV。当通过管道输入时，转换类型由可执行文件名推断。

GXL 支持比 GV 更丰富的图模型。gxl2gv 会尽可能将 GXL 构件映射到对应的 GV 构件；无法映射时，GXL 信息会作为属性存储。

# CAVEATS

属于 Graphviz 软件包的一部分。需要有效的 GXL 输入。部分属性可能无法转换。

# HISTORY

gxl2gv 是 **Graphviz** 项目的一部分，由 **AT&T 实验室**创建，用于基于 XML 的图交换。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```apk: sudo apk add graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gv2gxl](/man/gv2gxl)(1), [graphml2gv](/man/graphml2gv)(1), [dot](/man/dot)(1)
