# TAGLINE

面向 Puppet 的系统信息采集工具

# TLDR

**显示所有 fact**

```facter```

**显示特定 fact**

```facter [os.family]```

**以 JSON 输出 fact**

```facter --json```

**以 YAML 输出 fact**

```facter --yaml```

**列出所有 fact 名称**

```facter --list```

**显示耗时信息**

```facter --timing```

调试输出

```facter --debug```

# SYNOPSIS

**facter** [_options_] [_fact_...]

# PARAMETERS

**--json**
> 以 JSON 格式输出。

**--yaml**
> 以 YAML 格式输出。

**--list**
> 列出所有 fact 名称。

**--timing**
> 显示每个 fact 的采集耗时。

**--debug**
> 调试输出。

**--no-custom-facts**
> 禁用自定义 fact。

**--external-dir** _dir_
> 外部 fact 所在目录。

**--puppet**
> 加载 Puppet 的设置。

**-p**
> 包含 Puppet 的 fact。

# CONFIGURATION

**/etc/facter/facts.d/**
> 自定义外部 fact 目录，存放系统级 fact。

**/opt/puppetlabs/facter/facts.d/**
> Puppet 专用的自定义 fact 目录。

**~/.facter/facts.d/**
> 用户级自定义 fact 目录。

# DESCRIPTION

**facter** 收集并显示系统 fact——有关操作系统、硬件、网络和其他系统属性的信息。它是 Puppet 的核心组件，为配置管理提供数据。

fact 包括操作系统详情、IP 地址、内存、处理器、磁盘空间等。自定义 fact 可以用 Ruby 编写，也可以作为可执行的外部 fact 提供。

# COMMON FACTS

```
facter os.name           # Operating system
facter os.release.full   # OS version
facter networking.ip     # IP address
facter memory.total      # Total memory
facter processors.count  # CPU count
facter virtual           # Virtualization
```

# CAVEATS

部分 fact 需要 root 权限。自定义 fact 可能拖慢采集速度。不同 facter 版本的 fact 可能不同。Puppet 相关的 fact 需要 --puppet 标志。

# HISTORY

Facter 由 **Luke Kanies** 于 **2000 年代中期**作为 **Puppet Labs**（现 Puppet）Puppet 项目的一部分创建。Facter 3 是一次 C++ 重写（后来又改回 Ruby），于 **2015 年**发布，性能有所提升。

# INSTALL

```dnf: sudo dnf install facter```

```pacman: sudo pacman -S facter```

```nix: nix profile install nixpkgs#facter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[puppet](/man/puppet)(8), [ansible](/man/ansible)(1)
