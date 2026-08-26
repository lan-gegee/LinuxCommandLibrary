# TAGLINE

通过 D-Bus 提供服务的软件包管理守护进程

# TLDR

**启动** APT 守护进程

```sudo aptd```

以**前台**模式运行并开启调试

```sudo aptd --disable-timeout --debug```

# SYNOPSIS

**aptd** [_--disable-timeout_] [_--debug_]

# DESCRIPTION

**aptd** 是提供 D-Bus 接口的 APT 守护进程，用于软件包管理。它让 Update Manager 和 Software Center 等 GUI 应用无需直接以 root 权限访问 APT 即可执行软件包操作。

该守护进程通过 PolicyKit 处理身份验证，并将软件包操作排队执行。

# PARAMETERS

**--disable-timeout**
> 空闲超时后不退出

**--debug**
> 启用调试输出

**--dummy**
> 以模拟模式运行

**-h**, **--help**
> 显示帮助

# CONFIGURATION

**/etc/apt/apt.conf.d/**
> 守护进程使用的 APT 配置片段。

**/usr/share/dbus-1/system-services/org.debian.apt.service**
> aptd 的 D-Bus 服务激活文件。

**/usr/share/polkit-1/actions/org.debian.apt.policy**
> 控制身份验证要求的 PolicyKit 策略文件。

# CAVEATS

通常由 D-Bus 自动激活启动。GUI 软件包管理器依赖此服务，很少需要手动调用。

# HISTORY

**aptd** 为 Ubuntu 开发，旨在为软件包管理提供友好的接口，让 GUI 工具能够安全地执行 root 操作。

# SEE ALSO

[aptdcon](/man/aptdcon)(1), [apt](/man/apt)(8)
