# TAGLINE

**setarch linux64** 的别名，以修改后的方式运行程序

# TLDR

以 **64 位**personality 运行命令

```linux64 command```

带 **uname** 模拟运行命令

```linux64 --uname-2.6 command```

带**详细**输出运行命令

```linux64 -v command```

# SYNOPSIS

**linux64** [_options_] [_program_ [_arguments_]]

# DESCRIPTION

**linux64** 是 **setarch linux64** 的别名，它以修改后的体系结构域和进程 personality 标志运行程序。主要用于设置 uname 调用所报告的体系结构，以及控制进程的执行环境。

# PARAMETERS

**-v, --verbose**
> 详细模式

**--uname-2.6**
> 将内核版本报告为 2.6.x

**-3, --3gb**
> 将地址空间限制为 3GB（针对 32 位程序）

**--addr-no-randomize**
> 禁用地址空间随机化

**--short-inode**
> 启用短 inode 模式

# CAVEATS

此命令通常在运行会检查系统体系结构的程序时用于兼容性目的。它并不会真正改变底层的体系结构。

# HISTORY

**linux64** 是 **util-linux** 软件包的一部分，提供体系结构 personality 修改工具。配套命令 **linux32** 用于设置 32 位 personality。

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

[setarch](/man/setarch)(8), [linux32](/man/linux32)(8), [uname](/man/uname)(1)
