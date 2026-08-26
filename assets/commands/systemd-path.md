# TAGLINE

查询 systemd 文件层级路径

# TLDR

**显示**已知路径及其值的列表

```systemd-path```

**查询**特定路径并显示其值

```systemd-path "[path_name]"```

为打印的路径添加字符串**后缀**

```systemd-path --suffix [suffix_string]```

# SYNOPSIS

**systemd-path** [_options_] [_name_...]

# PARAMETERS

**--suffix _string_**
> 为打印的路径追加后缀

**--no-pager**
> 不将输出通过分页器显示

**-h, --help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**systemd-path** 查询并列出 systemd 文件层级规范定义的各类系统和用户路径。其中包括配置、缓存、运行时数据等系统目录的标准位置。

常见的路径名称包括：**temporary**、**temporary-large**、**system-binaries**、**system-configuration**、**user-configuration**、**user-runtime** 等。

# CAVEATS

路径的值可能随系统配置和用户上下文而变化。该工具反映的是 systemd 所理解的文件层级。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file-hierarchy](/man/file-hierarchy)(7), [systemctl](/man/systemctl)(1), [systemd-analyze](/man/systemd-analyze)(1)
