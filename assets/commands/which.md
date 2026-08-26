# TAGLINE

在 PATH 中定位可执行文件

# TLDR

**查找命令的路径**

```which [command]```

**查找多个命令的路径**

```which [command1] [command2]```

**显示所有匹配的可执行文件**（不只是第一个）

```which -a [command]```

# SYNOPSIS

**which** [**-a**] _command_...

# PARAMETERS

**-a**, **--all**
> 打印 PATH 中所有匹配的可执行文件，而不只是第一个

# DESCRIPTION

**which** 在 PATH 环境变量列出的目录中搜索可执行文件，并打印找到的第一个匹配项的路径。

当存在多个版本时，可以用它确定实际会执行哪个版本的命令，或者确认某个命令已安装并在你的 PATH 中。

使用 **-a** 会显示所有匹配项，从而揭示在不同 PATH 目录中是否存在多个版本。列在最前面的是实际会被执行的版本。

# CAVEATS

Which 只搜索 PATH；它不会显示 shell 内建命令、别名或函数。要全面查询命令，请在 bash 中使用 **type**，或在 zsh 中使用 **whence**。

有些系统使用不同的 which 实现，选项各异。**-a** 标志常见但并非普遍可用。

如果找不到命令，which 通常以状态码 1 退出且不产生输出（或视实现而定给出错误消息）。

# INSTALL

```dnf: sudo dnf install which```

```pacman: sudo pacman -S which```

```apk: sudo apk add which```

```zypper: sudo zypper install which```

```nix: nix profile install nixpkgs#which```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[type](/man/type)(1), [whence](/man/whence)(1), [whereis](/man/whereis)(1), [command](/man/command)(1), [hash](/man/hash)(1)
