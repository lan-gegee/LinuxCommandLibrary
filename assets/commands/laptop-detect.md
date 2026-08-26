# TAGLINE

尝试判断当前系统是笔记本电脑还是台式机

# TLDR

**检测**运行在笔记本上（退出码 0）还是台式机上（退出码 1）

```laptop-detect```

打印检测到的**设备类型**

```laptop-detect --verbose```

显示**版本**

```laptop-detect --version```

# SYNOPSIS

**laptop-detect** [_options_]

# PARAMETERS

**--verbose**
> 打印检测到的设备类型

**--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**laptop-detect** 会尝试判断系统是笔记本电脑还是台式机。它检查电池是否存在、机箱类型以及硬件标识符等系统特征。

如果系统被判定为笔记本电脑，该命令返回退出码 0；如果看起来是台式机或检测失败，则返回 1。这适用于需要根据系统类型做出不同行为的脚本。

# CAVEATS

检测采用启发式方法，并非对所有系统都准确。某些虚拟机或特殊的硬件配置可能被误判。

# HISTORY

laptop-detect 是为基于 Debian 的系统开发的，让软件配置能够根据系统属于移动设备还是固定设备自动调整。

# INSTALL

```pacman: sudo pacman -S laptop-detect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmidecode](/man/dmidecode)(8), [upower](/man/upower)(1), [hostnamectl](/man/hostnamectl)(1)
