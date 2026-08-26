# TAGLINE

Midnight Commander，一个可视化文件管理器

# TLDR

**启动 Midnight Commander**

```mc```

**在两个面板中打开指定目录启动**

```mc [dir1] [dir2]```

**黑白模式**

```mc -b```

**使用内置查看器查看文件**

```mc -v [file]```

**使用内置编辑器编辑文件**

```mc -e [file]```

**禁用鼠标支持**

```mc -d```

# SYNOPSIS

**mc** [_options_] [_path1_] [_path2_]

# PARAMETERS

_PATH1_ _PATH2_
> 左右面板显示的目录。

**-a**, **--stickchars**
> 禁用用于绘制线条的图形字符。

**-b**, **--nocolor**
> 强制黑白显示。

**-c**, **--color**
> 强制彩色模式。

**-C** _arg_, **--colors=**_arg_
> 指定不同的配色方案。

**-d**, **--nomouse**
> 禁用鼠标支持。

**-e** _FILE_
> 对指定文件启动内置编辑器。

**-v** _FILE_
> 对指定文件启动内置查看器。

**-s**, **--slow**
> 慢速终端模式。

**-u**, **--nosubshell**
> 禁用并发 subshell。

**-S** _arg_, **--skin=**_arg_
> 指定皮肤名称。

**-P** _FILE_, **--printwd=**_FILE_
> 退出时将面板的最后工作目录写入 _FILE_（由 **mc** 包装脚本使用，这样按 **F10** 退出时外层 shell 会 cd 到该目录）。

**-F**, **--datadir-info**
> 打印编译时的数据目录路径并退出。

**-g**, **--oldmouse**
> 使用"普通跟踪"鼠标模式（适用于不支持现代协议的终端）。

**-X**, **--no-x11**
> 不使用 X11 查询修饰键状态。

**--help**
> 显示帮助信息。

# KEYBOARD COMMANDS

**F1**
> 帮助。

**F3**
> 查看文件。

**F4**
> 编辑文件。

**F5**
> 复制文件或目录。

**F6**
> 移动/重命名文件或目录。

**F7**
> 创建目录。

**F8**
> 删除文件或目录。

**F9**
> 打开顶部菜单栏。

**F10**
> 退出。

**Tab**
> 在面板之间切换。

**Ctrl+O**
> 在面板和 shell 之间切换。

**Alt+Enter**
> 将选中的文件名复制到命令行。

# DESCRIPTION

**mc**（Midnight Commander）是一个具有双面板界面的可视化文件管理器。它通过功能键和菜单提供复制、移动、重命名和删除等文件操作。

支持将归档（tar、zip、rpm 等）作为虚拟文件系统浏览、通过 FTP/SFTP/SMB 进行远程连接，还带有内置文本编辑器和文件查看器。

subshell 集成（Ctrl+O）允许在文件管理器和完整命令行之间切换而无需退出 mc。

# CAVEATS

功能键被大量使用，可能与终端模拟器的快捷键冲突。某些终端可能需要重新映射按键。subshell 需要兼容的 shell（bash、zsh 或 fish）。

# HISTORY

Midnight Commander 由 **Miguel de Icaza** 于 **1994 年**创建，是 Norton Commander 的 Unix 克隆版。

# INSTALL

```apt: sudo apt install mc```

```dnf: sudo dnf install mc```

```pacman: sudo pacman -S mc```

```apk: sudo apk add mc```

```zypper: sudo zypper install mc```

```brew: brew install mc```

```nix: nix profile install nixpkgs#mc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [lf](/man/lf)(1)
