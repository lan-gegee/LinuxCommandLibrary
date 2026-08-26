# TAGLINE

基于 Shell 命令、用 YAML 配置的终端仪表盘

# TLDR

**使用配置文件启动仪表盘**

```sampler -c [config.yml]```

**带环境变量启动**

```sampler -c [config.yml] -e "[VAR=value]"```

**带多个环境变量启动**

```sampler -c [config.yml] -e "[VAR1=value1]" -e "[VAR2=value2]"```

# SYNOPSIS

**sampler** **-c** _config.yml_ [_options_]

# PARAMETERS

**-c** _FILE_
> YAML 配置文件的路径。

**-e** _VAR=VALUE_
> 为仪表盘设置环境变量。

# DESCRIPTION

**sampler** 按可配置的间隔执行 shell 命令，并将其输出可视化为终端中的折线图、迷你图（sparkline）、柱状图、仪表盘和文本框。它支持基于触发器的告警（视觉、声音、终端响铃或任意 shell 命令），并且开箱即用地支持数据库、消息队列、SSH 和 JMX。

# CAVEATS

Windows 支持尚属实验性。Linux 上若要使用声音告警需要 **libasound2-dev**。

# HISTORY

**sampler** 由 **Alexander Lukyanchikov**（sqshq）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install sampler```

```nix: nix profile install nixpkgs#sampler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glances](/man/glances)(1), [htop](/man/htop)(1)
