# TAGLINE

系统性能统计信息收集守护进程

# TLDR

**测试**配置文件后退出

```collectd -t```

**测试插件**的数据收集功能

```collectd -T```

**启动** collectd 守护进程

```collectd```

指定**自定义配置**文件

```collectd -C [path/to/file]```

指定**自定义 PID 文件**

```collectd -P [path/to/file]```

在**前台**运行（不 fork）

```collectd -f```

# SYNOPSIS

**collectd** [_options_]

# DESCRIPTION

**collectd** 是一个收集、传输和存储系统性能统计信息的守护进程。它支持众多用于收集指标的输入插件，以及用于存储或转发数据的输出插件。

常见用例包括监控系统资源、网络统计信息和应用指标。

# PARAMETERS

**-t**
> 测试配置文件语法

**-T**
> 测试插件数据收集

**-C** _file_
> 使用指定的配置文件

**-P** _file_
> 将 PID 写入指定文件

**-f**
> 不 fork 到后台

**-h**
> 显示帮助和版本信息

# CONFIGURATION

**/etc/collectd.conf**
> 主配置文件，控制插件、采集间隔和输出目的地。

**~/.collectdrc**
> 用户级配置文件。

# CAVEATS

配置时需要仔细设置输入和输出插件。某些插件可能需要额外的库。若未正确配置输出插件，程序会收集数据但不予存储。

# INSTALL

```apt: sudo apt install collectd-core```

```dnf: sudo dnf install collectd```

```apk: sudo apk add collectd```

```zypper: sudo zypper install collectd```

```brew: brew install collectd```

```nix: nix profile install nixpkgs#collectd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[collectdmon](/man/collectdmon)(1)
