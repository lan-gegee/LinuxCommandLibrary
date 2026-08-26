# TAGLINE

报告 AppArmor 配置文件与约束状态

# TLDR

检查 **AppArmor 状态**

```sudo aa-status```

以 **JSON 格式**显示状态

```sudo aa-status --json```

以**格式化 JSON 格式**显示状态

```sudo aa-status --pretty-json```

显示**已加载策略**的数量

```sudo aa-status --profiled```

显示**强制模式策略**的数量

```sudo aa-status --enforced```

显示**投诉模式策略**的数量

```sudo aa-status --complaining```

显示处于 **kill 模式**的策略数量

```sudo aa-status --kill```

# SYNOPSIS

**aa-status** [_option_]

# DESCRIPTION

**aa-status** 报告系统上 AppArmor 约束的当前状态。默认情况下，它会按执行模式（enforce、complain、kill、unconfined）分组展示已加载配置文件的摘要、受约束进程的数量，以及各进程适用的配置文件。各个标志可用于在脚本中查询特定计数器。**--json** 和 **--pretty-json** 标志提供机器可解析的输出，适合监控和自动化流水线使用。

# PARAMETERS

**--enabled**
> 若 AppArmor 未启用则返回错误码

**--profiled**
> 显示已加载的 AppArmor 策略数量

**--enforced**
> 显示强制模式的策略数量

**--complaining**
> 显示非强制（投诉模式）策略的数量

**--kill**
> 显示违规时终止任务的强制模式策略数量

**--prompt**
> 显示回退到用户态裁决的强制模式策略数量

**--special-unconfined**
> 显示 unconfined 模式策略的数量

**--process-mixed**
> 显示被包含不同模式配置文件的配置文件栈所约束的进程数量

**--verbose**
> 显示全面的 AppArmor 策略数据（默认行为）

**--json**
> 以 JSON 格式输出策略数据，便于机器处理

**--pretty-json**
> 提供人类和机器都可读的 JSON 输出

**--count**
> 只显示所选信息的计数

**--show** _TYPE_
> 指定要显示的内容：processes、profiles 或 all（默认：all）

**--filter.mode** _REGEX_
> 使用 POSIX 正则表达式按配置文件模式过滤输出

**--filter.profiles** _REGEX_
> 使用 POSIX 正则表达式按约束配置文件的名称过滤输出

**--filter.pid** _REGEX_
> 使用 POSIX 正则表达式按进程 PID 过滤输出

**--filter.exe** _REGEX_
> 使用 POSIX 正则表达式按可执行文件名过滤输出

**--help**
> 显示用法信息

# CAVEATS

退出码代表不同状态：**0** = 已启用且有策略，**1** = 未启用，**2** = 已启用但无策略，**3** = 控制文件不可用，**4** = 权限不足。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apt: sudo apt install apparmor```

```pacman: sudo pacman -S apparmor```

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-disable](/man/aa-disable)(8), [apparmor](/man/apparmor)(7)
