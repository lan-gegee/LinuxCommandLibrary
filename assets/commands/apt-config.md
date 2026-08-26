# TAGLINE

查询并显示 APT 配置设置。

# TLDR

**显示** APT 配置

```apt-config dump```

显示**特定选项**

```apt-config dump | grep [Dir::Cache]```

以 **shell 格式**显示配置

```apt-config shell VAR [Dir::Cache]```

# SYNOPSIS

**apt-config** [_-o option_] [_-c config_] _command_

# DESCRIPTION

**apt-config** 显示 APT 的配置值。它展示来自所有来源的有效配置，包括 /etc/apt/apt.conf、/etc/apt/apt.conf.d/ 以及命令行选项。

这对于调试 APT 行为、了解哪些设置正在生效，以及在脚本中使用 APT 配置值很有用。

# PARAMETERS

**dump**
> 显示全部配置

**shell** _var_ _option_
> 输出与 Shell 兼容的变量赋值语句

**-o** _option_
> 设置配置选项

**-c** _file_
> 读取额外的配置文件

# CONFIGURATION

**/etc/apt/apt.conf**
> APT 主配置文件。

**/etc/apt/apt.conf.d/**
> 存放即插式配置片段的目录，按字母数字顺序处理。

# CAVEATS

配置是分层的；较低层级的选项会覆盖较高层级的。命令行选项会覆盖文件中的设置。某些选项需要特定的 APT 版本。

# HISTORY

**apt-config** 从 APT 早期版本起就是其组成部分，为程序化访问 APT 的配置系统提供了途径。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8)
