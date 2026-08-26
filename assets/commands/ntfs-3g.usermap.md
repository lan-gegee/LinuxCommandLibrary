# TAGLINE

创建 Windows-Linux 用户映射

# TLDR

**创建用户映射**

```ntfs-3g.usermap [/dev/sda1]```

**映射到指定文件**

```ntfs-3g.usermap [/dev/sda1] > [UserMapping]```

**交互模式**

```ntfs-3g.usermap -i [/dev/sda1]```

# SYNOPSIS

**ntfs-3g.usermap** [_options_] _device_

# PARAMETERS

_DEVICE_
> NTFS 分区。

**-i**
> 交互模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfs-3g.usermap** 创建 Windows-Linux 用户映射，将 SID 映射到 UID。

该工具生成 UserMapping 文件，用于权限映射。

# CAVEATS

属于 ntfs-3g 的一部分。会创建 .NTFS-3G/UserMapping。可以手动编辑。

# HISTORY

ntfs-3g.usermap 提供 Windows 和 Linux 之间的**用户身份映射**功能。

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(1), [ntfs-3g.secaudit](/man/ntfs-3g.secaudit)(1)
