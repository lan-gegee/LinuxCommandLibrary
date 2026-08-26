# TAGLINE

将 Graphviz DOT 格式转换为 GXL

# TLDR

**将 DOT 转换为 GXL**

```gv2gxl [input.gv] -o [output.gxl]```

**输出到标准输出**

```gv2gxl [input.dot]```

**处理多个文件**

```gv2gxl [file1.gv] [file2.gv] -o [output.gxl]```

# SYNOPSIS

**gv2gxl** [**-gd?**] [**-o** _outfile_] [_files_]

# PARAMETERS

**-g**
> 强制将输入视为 GV 格式并生成 GXL 输出，忽略文件扩展名

**-d**
> 强制将输入视为 GXL 格式并生成 GV 输出，忽略文件扩展名

**-o** _outfile_
> 将输出写入指定文件而非标准输出

**-?**
> 显示用法信息并退出

# DESCRIPTION

**gv2gxl** 在以 GXL（Graph eXchange Language）表示的图与 Graphviz GV/DOT 格式之间进行转换。GXL 是一种基于 XML 的图交换格式。

除非用 **-g** 或 **-d** 指定转换类型，否则该工具会根据输入文件的扩展名推断转换方向：".gv" 后缀表示从 GV 转换为 GXL，".gxl" 后缀表示从 GXL 转换为 GV。当通过管道输入且未加任何标志时，转换方向由可执行文件名决定：**gv2gxl** 从 GV 转换为 GXL。

命令 **dot2gxl**、**gv2gxl** 和 **gxl2dot** 都是 **gxl2gv** 的别名。

# CAVEATS

转换只能处理每个 GXL 文件中的一个图。先执行 gxl2gv 再执行 gv2gxl 在语义上等价于恒等操作。

# HISTORY

gv2gxl 是 **Graphviz** 项目的一部分，由 **AT&T 实验室**创建，用于基于 XML 的图交换。

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

[gxl2gv](/man/gxl2gv)(1), [gv2gml](/man/gv2gml)(1), [dot](/man/dot)(1)
