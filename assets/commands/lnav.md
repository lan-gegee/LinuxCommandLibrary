# TAGLINE

利用日志文件语义信息的高级日志查看器

# TLDR

查看**日志文件**

```lnav path/to/log```

查看**目录**中的日志

```lnav /var/log/```

通过 SSH 查看**远程**日志文件

```lnav ssh user@host:/var/log/syslog```

**校验**日志格式配置

```lnav -C path/to/log```

包含**已轮转/归档**的日志

```lnav -R /var/log/syslog```

以**无界面**模式运行命令

```lnav -n -c ":filter-in error" path/to/log```

# SYNOPSIS

**lnav** [**-hHVCnqirRt**] [**-c** _CMD_] [**-f** _PATH_] [**-I** _PATH_] [**-d** _FILE_] [**-w** _FILE_] [_logfile1_ _logfile2_ ...]

# DESCRIPTION

**lnav** 是一个利用日志文件语义信息的高级日志查看器。它可以交错显示来自多个文件的消息，生成基于时间的直方图，并提供基于热键的高效日志导航。

# PARAMETERS

**-h**
> 显示帮助信息

**-H**
> 显示内部帮助文本

**-V**
> 打印版本信息

**-n**
> 以无界面模式运行，不显示 UI

**-c CMD**
> 加载文件后执行命令

**-f PATH**
> 从配置文件中读取命令执行

**-I PATH**
> 向配置搜索路径添加目录

**-q**
> 静默模式；抑制消息输出

**-i**
> 将格式文件安装到用户目录。传入 'extra' 可安装默认的第三方格式集合。

**-u**
> 从软件仓库更新已安装的格式文件

**-a**
> 加载所有最近使用的日志文件类型

**-C**
> 校验配置和日志格式文件

**-d FILE**
> 将调试消息输出到文件

**-r**
> 递归加载目录中的文件

**-R**
> 包含已轮转和归档的日志文件

**-t**
> 为 stdin 数据添加时间戳

**-w FILE**
> 将 stdin 内容写入文件

# CONFIGURATION

**~/.lnav/formats/**
> 存放用户自定义日志格式文件的目录（JSON 格式定义）。

**~/.lnav/configs/**
> 存放用户配置文件的目录。

# CAVEATS

运行时按 "?" 获取在线帮助，按 "q" 退出。lnav 会自动检测并解析许多常见的日志格式（syslog、Apache、strace 等）。自定义格式可在 JSON 配置文件中定义。使用 ":filter-in" 和 ":filter-out" 命令交互式地过滤日志行。

# HISTORY

**lnav** 的创建目的是为系统管理员和开发者提供一款高级日志导航器，具备自动格式检测、语法高亮和高效导航能力。

# INSTALL

```apt: sudo apt install lnav```

```dnf: sudo dnf install lnav```

```pacman: sudo pacman -S lnav```

```apk: sudo apk add lnav```

```zypper: sudo zypper install lnav```

```brew: brew install lnav```

```nix: nix profile install nixpkgs#lnav```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [tail](/man/tail)(1), [journalctl](/man/journalctl)(1), [multitail](/man/multitail)(1)
