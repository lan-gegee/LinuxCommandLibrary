# TAGLINE

显示文件与文件系统的元数据

# TLDR

**显示文件状态**

```stat [file]```

**以简洁格式显示**

```stat -t [file]```

**显示文件系统状态**

```stat -f [file]```

**自定义格式输出**

```stat -c "%n: %s bytes" [file]```

**显示访问时间**

```stat -c "%x" [file]```

**显示修改时间**

```stat -c "%y" [file]```

**以八进制显示权限**

```stat -c "%a" [file]```

**显示多个文件的全部信息**

```stat [file1] [file2] [file3]```

**跟随符号链接**

```stat -L [symlink]```

# SYNOPSIS

**stat** [_options_] _file_...

# DESCRIPTION

**stat** 显示关于文件或文件系统的详细信息。它展示的元数据包括大小、权限、所有者关系、时间戳、inode 号和设备信息。

默认输出包括文件名、大小、块数、设备、inode、链接数、访问权限、所有者关系以及访问/修改/变更时间。自定义格式字符串可以选择特定字段。

当脚本需要特定文件属性，或需要调查 ls 未显示的文件属性时，stat 非常有用。

# PARAMETERS

**-f**, **--file-system**
> 显示文件系统状态而非文件状态。

**-L**, **--dereference**
> 跟随符号链接。

**-t**, **--terse**
> 打印简洁输出。

**-c** _format_, **--format=** _format_
> 使用自定义格式字符串。

**--printf=** _format_
> 类似 --format，但会解释反斜杠转义且不输出末尾换行符。

# FORMAT SEQUENCES (FILE)

**%a**: 八进制访问权限
**%A**: 人类可读形式的访问权限
**%F**: 文件类型
**%g**: 组 ID
**%G**: 组名
**%h**: 硬链接数量
**%i**: inode 号
**%n**: 文件名
**%s**: 大小（字节）
**%u**: 用户 ID
**%U**: 用户名
**%x**: 访问时间
**%y**: 修改时间
**%z**: 变更时间

# FORMAT SEQUENCES (FILESYSTEM)

**%a**: 空闲块数
**%b**: 总块数
**%f**: 空闲块数（非 root）
**%n**: 文件名
**%s**: 块大小
**%T**: 文件系统类型

# CAVEATS

GNU stat（Linux）与 BSD stat（macOS）的输出格式不同。某些文件系统不支持全部属性。出于性能考虑，部分系统可能禁用了访问时间记录。

# HISTORY

**stat** 在不同系统上有不同的起源。GNU 版本（**coreutils** 的一部分）由 **Michael Meskes** 于 **2001 年**编写。BSD 系统有自己的实现，语法略有差异。该命令为 stat() 系统调用提供了标准接口。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [file](/man/file)(1), [touch](/man/touch)(1), [chmod](/man/chmod)(1)
