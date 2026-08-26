# TAGLINE

远程执行与配置管理系统

# TLDR

**Ping 所有 minion**

```salt '*' test.ping```

**在 minion 上运行命令**

```salt '*' cmd.run '[command]'```

**指定目标 minion**

```salt '[minion-id]' test.ping```

**应用状态**

```salt '*' state.apply```

**应用指定状态**

```salt '*' state.apply [webserver]```

**安装软件包**

```salt '*' pkg.install [nginx]```

**显示 grains**

```salt '[minion]' grains.items```

**复制文件**

```salt '*' cp.get_file [salt://file.txt] [/tmp/file.txt]```

# SYNOPSIS

**salt** [_target_] _function_ [_args_]

# PARAMETERS

_TARGET_
> Minion 匹配模式。

_FUNCTION_
> 要执行的 模块.函数。

**-G** _GRAIN_
> 按 grain 定位目标。

**-E**
> 正则表达式定位。

**-L**
> 列表定位。

**-C**
> 复合定位。

**--async**
> 异步执行。

**--timeout** _SECS_
> 命令超时时间。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**salt** 是 SaltStack 的主要命令行界面，SaltStack 是一套远程执行与配置管理系统。它将命令从 Salt master 发送到各 minion（受管节点），在可能多达数千台系统上并行执行并返回结果。

定位机制决定哪些 minion 接收命令，可使用 glob 模式（默认）、正则表达式（**-E**）、基于 grain 的匹配（**-G**，按操作系统或硬件属性定位），或组合多个条件的复合表达式（**-C**）。执行模块提供数百个函数，涵盖软件包管理、文件操作、服务控制和系统管理。

状态（state）使用 YAML 文件以声明式方式定义系统的期望配置。**state.apply** 函数确保 minion 收敛到定义的状态，使 Salt 既适合临时命令执行，也适合系统化的基础设施管理。

# CAVEATS

需要搭建 Salt master/minion 环境。大型基础设施需要调优。状态的复杂度会不断增长。

# HISTORY

**Salt** 由 **Thomas Hatch** 创建并于 **2011 年**发布。它发展为 **SaltStack**，后于 2020 年被 **VMware** 收购。

# INSTALL

```dnf: sudo dnf install salt```

```apk: sudo apk add salt-lts-master```

```zypper: sudo zypper install salt```

```nix: nix profile install nixpkgs#salt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt-master](/man/salt-master)(1), [salt-minion](/man/salt-minion)(1), [salt-key](/man/salt-key)(1)
