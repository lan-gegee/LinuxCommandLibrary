# TAGLINE

云实例初始化与配置

# TLDR

显示最近一次 cloud-init 运行的**状态**

```cloud-init status```

**等待** cloud-init 完成并报告状态

```cloud-init status --wait```

**列出**可用的顶级元数据键

```cloud-init query --list-keys```

**查询**缓存的实例元数据

```cloud-init query [dot_delimited_variable_path]```

**清理**日志和产物，使 cloud-init 可以重新运行

```cloud-init clean```

**分析** cloud-init 的启动性能

```cloud-init analyze show```

**校验** cloud-config 文件

```cloud-init schema --config-file [path/to/config.yaml]```

# SYNOPSIS

**cloud-init** [_options_] _command_ [_arguments_]

# DESCRIPTION

**cloud-init** 是云实例初始化的行业标准，适用于所有主要云提供商和 Linux 发行版。它负责云实例的早期初始化，包括网络配置、存储设置、SSH 密钥注入、用户账户创建和软件包安装。

Cloud-init 从多种数据源读取配置，包括云提供商的元数据服务、user-data 脚本和本地配置文件。它在启动过程中分多个阶段运行，以确保系统配置任务按正确顺序执行。

该工具支持以 cloud-config YAML 进行声明式配置、用 shell 脚本进行命令式设置，并可通过自定义模块扩展。它提供查询实例元数据、校验配置和排查初始化问题的命令。

# PARAMETERS

**init**
> 初始化 cloud-init 并执行初始模块

**modules**
> 使用给定的配置键激活模块

**single**
> 运行单个模块

**status**
> 报告 cloud-init 状态

**query** _key_
> 查询实例元数据

**clean**
> 移除日志和产物，以便下次启动时重新运行

**collect-logs**
> 将调试信息收集到一个 tar 包中

**analyze**
> 分析 cloud-init 启动性能

**schema**
> 校验 cloud-config 文件

**features**
> 列出此版本支持的定义特性

# CONFIGURATION

**/etc/cloud/cloud.cfg**
> 主配置文件，控制模块、数据源和默认设置。

**/etc/cloud/cloud.cfg.d/*.cfg**
> 与主配置合并的附加配置文件。

# CAVEATS

主要用于具有元数据服务的云/虚拟环境。运行 clean 会让 cloud-init 在下次启动时再次运行，这可能重新配置系统。某些命令需要 root 权限。

# HISTORY

**cloud-init** 最初由 Canonical 为 Ubuntu 开发，如今已成为大多数 Linux 发行版和云提供商事实上的云实例初始化标准。

# INSTALL

```dnf: sudo dnf install cloud-init```

```pacman: sudo pacman -S cloud-init```

```apk: sudo apk add cloud-init```

```zypper: sudo zypper install cloud-init```

```nix: nix profile install nixpkgs#cloud-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1)
