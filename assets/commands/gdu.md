# TAGLINE

带交互式 TUI 的快速磁盘用量分析工具

# TLDR

**交互式分析磁盘用量**（当前目录）

```gdu```

**分析特定目录**

```gdu [/path/to/directory]```

**以非交互模式分析**（打印结果）

```gdu -n [/path/to/directory]```

**显示表观大小**而非磁盘占用

```gdu -a [/path/to/directory]```

**分析时忽略特定目录**

```gdu -i "[.git,node_modules]" [/path]```

**将结果导出为 JSON**

```gdu -o json [/path] > [output.json]```

**仅分析特定文件系统**（不跨越挂载点）

```gdu -x [/]```

**显示版本信息**

```gdu -v```

# SYNOPSIS

**gdu** [_options_] [_directory_]

# PARAMETERS

**-n**, **--non-interactive**
> 以非交互模式运行（只打印结果）。

**-a**, **--apparent-size**
> 显示文件的表观大小而非磁盘占用。

**-x**, **--no-cross**
> 不跨越文件系统边界。

**-i**, **--ignore-dirs** _paths_
> 要忽略的逗号分隔路径。

**-I**, **--ignore-dirs-pattern** _regex_
> 忽略匹配给定正则表达式的路径。

**-m**, **--max-cores** _n_
> 设置使用的最大 CPU 核心数。

**-o**, **--output-file** _file_
> 将结果导出到文件（配合格式标志使用）。

**-f**, **--input-file** _file_
> 从导出的 JSON 文件读取而非重新扫描。

**-c**, **--no-color**
> 禁用彩色输出。

**-d**, **--show-disks**
> 显示所有已挂载的磁盘。

**-p**, **--no-progress**
> 扫描期间不显示进度。

**-s**, **--summarize**
> 对每个参数只显示总计。

**-L**, **--follow-symlinks**
> 跟随文件符号链接。

**--top** _n_
> 只显示最大的前 N 个文件。

**--si**
> 使用 SI 单位（1000 的幂）而非二进制单位。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**gdu**（go disk usage）是一款带交互式 ncurses 界面的快速磁盘用量分析工具。它用 Go 编写，在分析大型目录结构时的性能显著优于 **du** 和 **ncdu** 等传统工具。

交互式界面按大小排序显示目录，并带有用量条和文件计数。导航使用方向键或 vim 风格的 hjkl。按 **d** 删除选中项，按 **Enter** 进入目录，按 **?** 查看帮助。

颜色编码指示目录类型：蓝色表示目录，红色表示大文件，符号链接、套接字等有特殊颜色。进度指示器显示扫描状态和预计完成情况。

非交互模式（-n）输出的结果适合脚本处理。JSON 导出便于与其他工具集成或保存分析结果以便日后比较。该工具还可以读取已导出的 JSON 文件进行查看，无需重新扫描。

性能来自并行扫描和高效的内存使用。它在 I/O 不构成瓶颈的 SSD 和 NVMe 驱动器上尤为有效。

# CAVEATS

交互式删除是永久的（无回收站）。某些终端可能无法正确渲染界面。对无法访问的目录会显示权限拒绝错误，但不会停止扫描。内存使用随文件/目录数量增加。

# HISTORY

**gdu** 由 Daniel Milde 于 **2020 年**前后创建，作为 ncdu 的更快替代品。它用 Go 编写以保证性能并便于跨平台编译，迅速受到系统管理员欢迎。该工具已进入大多数 Linux 发行版的软件包管理器和 macOS 的 Homebrew。

# INSTALL

```apt: sudo apt install gdu```

```dnf: sudo dnf install gdu```

```pacman: sudo pacman -S gdu```

```apk: sudo apk add gdu```

```zypper: sudo zypper install gdu```

```brew: brew install gdu```

```nix: nix profile install nixpkgs#gdu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [ncdu](/man/ncdu)(1), [dust](/man/dust)(1), [df](/man/df)(1), [duf](/man/duf)(1)
