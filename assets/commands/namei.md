# TAGLINE

沿路径名逐级解析直到终点，并显示每一级组件

# TLDR

**解析路径名**（跟随符号链接）

```namei [path/to/a] [path/to/b]```

以**长列表格式**显示

```namei -l [path/to/file]```

显示各文件类型的**权限位**

```namei -m [path/to/file]```

显示每个文件的**所有者和组**

```namei -o [path/to/file]```

**不跟随**符号链接

```namei -n [path/to/file]```

显示**全部信息**（长列表、权限、所有者）

```namei -lmo [path/to/file]```

# SYNOPSIS

**namei** [**-l**] [**-m**] [**-o**] [**-n**] [**-x**] [**-v**] _pathname_...

# PARAMETERS

**-l, --long**
> 使用长列表格式（等同于 -m -o -v）

**-m, --modes**
> 以 ls 风格显示各文件类型的权限位

**-o, --owners**
> 显示每个文件的所有者和组名

**-n, --nosymlinks**
> 不跟随符号链接

**-x, --mountpoints**
> 用 D 标记挂载点目录

**-v, --vertical**
> 权限和所有者垂直对齐

**-Z, --context**
> 显示每个文件的安全上下文

**-h, --help**
> 显示帮助

**-V, --version**
> 显示版本

# DESCRIPTION

**namei** 沿路径名逐级解析直到找到终点（文件、目录、设备等），并显示路径的每一级组件。它对诊断"符号链接层级过多"错误特别有用。

输出会显示每个路径组件及其类型指示符：d（目录）、l（符号链接）、-（普通文件）、c（字符设备）、b（块设备）、s（套接字）、p（FIFO/管道）。

# OUTPUT SYMBOLS

**f:** - 当前正在解析的路径名
**d** - 目录
**l** - 符号链接
**s** - 套接字
**b** - 块设备
**c** - 字符设备
**p** - FIFO/命名管道
**-** - 普通文件
**?** - 某种错误
**D** - 挂载点（配合 -x）

# CAVEATS

符号链接循环会导致错误。命令在第一个无法解析的组件处停止。如果任何路径组件不可访问，会出现权限拒绝错误。

# HISTORY

**namei** 是 **util-linux**（标准 Linux 工具集）的组成部分。它提供了一种诊断工具，用于理解复杂的路径结构并解决符号链接问题。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [stat](/man/stat)(1), [readlink](/man/readlink)(1)
