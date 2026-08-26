# TAGLINE

管理 alternatives 机制所用的默认命令符号链接

# TLDR

**添加**符号链接

```sudo update-alternatives --install [path/to/symlink] [command_name] [path/to/binary] [priority]```

**交互式配置**符号链接

```sudo update-alternatives --config [java]```

**移除**符号链接

```sudo update-alternatives --remove [java] [/opt/java/jdk1.8.0_102/bin/java]```

**显示**指定命令的信息

```update-alternatives --display [java]```

**显示**所有命令及其当前选择

```update-alternatives --get-selections```

# SYNOPSIS

**update-alternatives** [_option_] _command_

# PARAMETERS

**--install _link_ _name_ _path_ _priority_**
> 以指定优先级为 name 添加一个候选项

**--config _name_**
> 交互式配置 name 的候选项

**--remove _name_ _path_**
> 移除某个特定候选项

**--display _name_**
> 显示 name 的候选项信息

**--get-selections**
> 列出所有已配置的候选项

**--set _name_ _path_**
> 以非交互方式设置候选项

**--auto _name_**
> 切换到自动模式（优先级最高者胜出）

**--list _name_**
> 列出某个 name 的全部候选项

# DESCRIPTION

**update-alternatives** 通过维护一组符号链接来确定默认命令，适用于同一程序安装了多个版本的情况。它管理位于 **/etc/alternatives/** 的链接目录，这些链接指向实际的程序二进制文件。

常见用途包括管理多个 Java 版本、编辑器或编译器。在自动模式下，优先级数值越高越被优先选用。

# CAVEATS

修改操作需要 root 权限。优先级数值决定自动模式的选择结果。手动模式会一直保持，直到被显式更改。这是 Debian/Ubuntu 特有的工具；Red Hat 使用 **alternatives** 命令。

# INSTALL

```apt: sudo apt install dpkg```

```dnf: sudo dnf install dpkg```

```pacman: sudo pacman -S dpkg```

```apk: sudo apk add dpkg```

```zypper: sudo zypper install dpkg```

```brew: brew install dpkg```

```nix: nix profile install nixpkgs#dpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alternatives](/man/alternatives)(8), [ln](/man/ln)(1)
