# TAGLINE

自动 CPU 速度与功耗优化器

# TLDR

**监控** CPU 频率和功耗

```sudo auto-cpufreq --monitor```

以 **live** 模式运行（临时优化）

```sudo auto-cpufreq --live```

显示**统计信息**

```sudo auto-cpufreq --stats```

**安装**为系统服务

```sudo auto-cpufreq --install```

**移除**系统服务

```sudo auto-cpufreq --remove```

**强制**使用指定的调速器

```sudo auto-cpufreq --force=powersave```

**重置**被强制的调速器，恢复自动行为

```sudo auto-cpufreq --force=reset```

**更新** auto-cpufreq

```sudo auto-cpufreq --update```

# SYNOPSIS

**auto-cpufreq** [_options_]

# DESCRIPTION

**auto-cpufreq** 是一款 Linux 自动 CPU 速度与功耗优化工具。它根据系统负载和供电来源（交流电/电池）动态调整 CPU 频率调节和睿频加速，兼顾性能与电池续航。

# PARAMETERS

**--monitor**
> 监控 CPU 频率、调速器和电源信息

**--live**
> 以 live 模式运行并进行临时优化

**--stats**
> 显示守护进程模式的统计信息

**--install**
> 将 auto-cpufreq 安装为系统服务

**--remove**
> 移除 auto-cpufreq 系统服务

**--update**
> 将 auto-cpufreq 更新到最新版本

**--force=GOVERNOR**
> 强制使用指定的调速器（powersave、performance），或用 reset 回到自动模式

**--turbo=MODE**
> 强制睿频加速行为（always、never、auto）

**--config=PATH**
> 使用自定义配置文件

**--debug**
> 显示调试信息

**--version**
> 显示已安装的 auto-cpufreq 版本

# CONFIGURATION

**/etc/auto-cpufreq.conf**
> 系统级配置文件。按供电来源（充电/电池）定义调速器和睿频加速偏好。

**$XDG_CONFIG_HOME/auto-cpufreq/auto-cpufreq.conf**
> 每个用户的配置文件，优先于系统级路径检查。通过 --config 指定的文件优先级最高。

# CAVEATS

使用 --install 会创建 systemd 服务以实现自动化运行。--live 与 --monitor 模式仅用于测试，重启后不会保留。对于笔记本电脑，auto-cpufreq 会根据供电来源在 performance 与 powersave 之间自动切换。

# HISTORY

**auto-cpufreq** 的诞生是为了免去手动调优即可实现 CPU 频率自动优化，对笔记本电脑尤为实用，可在延长电池续航的同时在需要时保持性能。

# INSTALL

```aur: yay -S auto-cpufreq```

```nix: nix profile install nixpkgs#auto-cpufreq```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cpupower](/man/cpupower)(1), [cpufreq-info](/man/cpufreq-info)(1), [tlp](/man/tlp)(8)

# RESOURCES

```[Source code](https://github.com/AdnanHodzic/auto-cpufreq)```

<!-- verified: 2026-06-17 -->
