# TAGLINE

向运行级添加或移除服务

# TLDR

**列出已启用的服务及其运行级**

```rc-update```

**列出所有服务，包括已禁用的**

```rc-update -v```

**显示特定运行级中的服务**

```rc-update show [default]```

**将服务添加到运行级**

```sudo rc-update add [service] [default]```

**从运行级移除服务**

```sudo rc-update del [service] [default]```

**从所有运行级移除服务**

```sudo rc-update -a del [service]```

# SYNOPSIS

**rc-update** [_options_] [**add**|**del**|**show**] [_service_] [_runlevel_...]

# PARAMETERS

**add**
> 将服务添加到指定运行级；未指定时为当前运行级。

**del**, **delete**
> 从指定运行级移除服务；未指定时为当前运行级。

**show**
> 显示所有已启用的服务及其所属的运行级。

**-a**, **--all**
> 将操作应用到所有运行级。

**-s**, **--stack**
> 叠加运行级而不是服务（高级用法）。

**-u**, **--update**
> 强制更新依赖树。

**-v**, **--verbose**
> 显示所有服务，包括已禁用的。

# DESCRIPTION

**rc-update** 管理 OpenRC 中哪些服务在哪些运行级启动。运行级是会一起启动的命名服务组，例如 **boot** 用于早期引导服务，**default** 用于日常运行，**shutdown** 用于系统关机。

所有服务必须位于 **/etc/init.d** 或 **/usr/local/etc/init.d** 中并符合 OpenRC runscript 标准。该工具通过在 **/etc/runlevels/** 中创建和删除符号链接来控制每个运行级启动哪些服务。

# CAVEATS

仅适用于 OpenRC，不适用于基于 systemd 的发行版。运行级名称因发行版而异。加入 **boot** 运行级的服务必须存在于 **/etc/init.d**。更改将在下次启动或切换运行级时生效。

# HISTORY

**rc-update** 是 **OpenRC** 的一部分。OpenRC 是一个基于依赖关系的 init 系统，主要用于 Gentoo 和 Alpine Linux，作为 systemd 的替代方案。

# INSTALL

```apt: sudo apt install openrc```

```apk: sudo apk add openrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rc-service](/man/rc-service)(8), [rc-status](/man/rc-status)(8), [openrc](/man/openrc)(8)
