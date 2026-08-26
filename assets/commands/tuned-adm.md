# TAGLINE

管理系统性能调优配置

# TLDR

显示当前**激活的** tuned 配置

```tuned-adm active```

**列出**本系统可用的配置

```tuned-adm list```

**切换**到指定配置

```tuned-adm profile [profile_name]```

让 tuned **推荐**一个配置

```tuned-adm recommend```

**关闭**动态调优

```tuned-adm off```

# SYNOPSIS

**tuned-adm** [_command_] [_arguments_]

# PARAMETERS

**list**
> 列出可用的调优配置

**active**
> 显示当前激活的配置

**profile _name_**
> 切换到指定配置

**recommend**
> 为本系统推荐最优配置

**off**
> 禁用 tuned 并重置为默认值

**verify**
> 校验当前设置是否与配置一致

**auto_profile**
> 启用/禁用自动选择配置

# DESCRIPTION

**tuned-adm** 管理 **tuned** 守护进程提供的系统性能调优配置。这些配置针对特定工作负载（如吞吐量、延迟、节能或虚拟化）优化各种内核和系统参数。

常见配置包括：**balanced**、**throughput-performance**、**latency-performance**、**powersave**、**virtual-guest** 和 **virtual-host**。**recommend** 命令会分析系统并建议最佳配置。

# CAVEATS

需要 tuned 服务正在运行。配置更改立即生效。某些设置可能需要重启才能完全应用。可用配置因发行版而异。

# INSTALL

```dnf: sudo dnf install tuned```

```pacman: sudo pacman -S tuned```

```apk: sudo apk add tuned```

```zypper: sudo zypper install tuned```

```nix: nix profile install nixpkgs#tuned```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tuned](/man/tuned)(8), [cpupower](/man/cpupower)(1)
