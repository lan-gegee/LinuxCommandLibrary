# TAGLINE

用于约束应用程序的强制访问控制框架。

# TLDR

**显示 AppArmor 状态**和已加载的配置

```sudo aa-status```

将**某个配置**设为 enforce 模式

```sudo aa-enforce [/etc/apparmor.d/usr.bin.firefox]```

将**某个配置**设为 complain 模式（仅记录日志）

```sudo aa-complain [/etc/apparmor.d/usr.bin.firefox]```

**禁用某个配置**

```sudo aa-disable [/etc/apparmor.d/usr.bin.firefox]```

**重新加载所有 AppArmor 配置**

```sudo systemctl reload apparmor```

以交互方式**生成新配置**

```sudo aa-genprof [/usr/bin/application]```

根据日志事件**更新配置**

```sudo aa-logprof```

# SYNOPSIS

**aa-status** [_options_]

**aa-enforce** _profile_

**aa-complain** _profile_

**aa-disable** _profile_

**aa-genprof** _executable_

**aa-logprof**

# PARAMETERS

**aa-status**
> 显示 AppArmor 的当前状态，包括已加载的配置及其模式

**aa-enforce** _profile_
> 将配置设为 enforce 模式（阻止违反策略的行为）

**aa-complain** _profile_
> 将配置设为 complain 模式（记录违规但不阻止）

**aa-disable** _profile_
> 完全禁用某个配置

**aa-genprof** _executable_
> 以交互方式为应用程序生成新配置

**aa-logprof**
> 根据 complain 模式下记录的事件更新配置

**aa-unconfined**
> 列出未受 AppArmor 约束的进程

**--verbose**
> 显示详细信息（aa-status）

**--enforced**
> 仅显示处于 enforce 模式的配置数量（aa-status）

**--complaining**
> 仅显示处于 complain 模式的配置数量（aa-status）

# DESCRIPTION

**AppArmor**（Application Armor）是一个 Linux 安全模块，为程序提供强制访问控制（MAC）。它使用针对每个程序的安全配置来限制文件访问、网络能力和其他系统资源，从而约束应用行为。

配置有两种运行模式：**enforce** 模式阻止并记录违规行为；**complain** 模式只记录而不阻止，便于开发和测试新配置。

**aa-status** 命令显示已加载的配置及其模式。用 **aa-enforce** 和 **aa-complain** 切换配置模式。**aa-genprof** 工具通过运行应用程序并学习其行为来生成新配置；**aa-logprof** 则根据日志事件完善现有配置。

配置存放在 **/etc/apparmor.d/** 中并在启动时加载。在现代发行版上，AppArmor 服务通过 systemd 管理配置加载。

# EXIT CODES

**aa-status** 返回值：**0** = AppArmor 已启用且策略已加载，**1** = AppArmor 未启用，**2** = AppArmor 已启用但没有加载策略，**3** = AppArmor 控制文件不可用，**4** = 权限不足。

# CONFIGURATION

**/etc/apparmor.d/**
> 存放 AppArmor 安全配置的目录，由 apparmor 服务在启动时加载。

**/etc/apparmor.d/tunables/**
> 配置引用的共享变量定义。

**/etc/apparmor.d/abstractions/**
> 可被各配置包含的可复用规则片段。

# CAVEATS

大多数 AppArmor 命令需要 root 权限。如果策略过于严格，enforce 模式的配置可能破坏应用功能。请先在 complain 模式下测试新配置。必须安装 **apparmor-utils** 软件包才能使用配置管理工具。

# HISTORY

AppArmor 由 **Immunix Inc.** 于 **20 世纪 90 年代**末开发，并于 **2005 年**被 **Novell** 收购。它在 Linux 内核 **2.6.36** 版（2010 年）中进入主线内核。Ubuntu 自 **7.10** 版（2007 年）起默认附带 AppArmor，它也可在 Debian、SUSE 及其他发行版上作为 SELinux 的替代方案使用。

# INSTALL

```pacman: sudo pacman -S apparmor```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aa-status](/man/aa-status)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-notify](/man/aa-notify)(8)
