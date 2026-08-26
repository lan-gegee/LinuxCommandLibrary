# TAGLINE

用 Python 自动化基础设施部署

# TLDR

**部署到服务器**

```pyinfra [inventory] [deploy.py]```

**在服务器上执行命令**

```pyinfra [inventory] exec -- [command]```

**预览将发生的变更**

```pyinfra --dry [inventory] [deploy.py]```

**采集 facts 部署**

```pyinfra [inventory] fact [server.Hostname]```

# SYNOPSIS

**pyinfra** [_options_] _inventory_ _operations_

# PARAMETERS

_INVENTORY_
> 目标主机文件。

_OPERATIONS_
> 部署脚本或命令。

**--dry**
> 试运行模式；只打印操作而不执行。

**--limit** _HOSTS_
> 按名称或 glob 模式过滤，只在特定主机上执行。

**--retry** _N_
> 失败的操作最多重试 N 次。

**--debug-inventory**
> 输出 inventory 中的主机、组和数据。

**--debug-facts**
> 在生成操作后显示 facts 并退出。

**--debug-operations**
> 在生成后显示操作并退出。

**exec**
> 在主机上执行任意 shell 命令。

**fact**
> 从目标主机采集 facts。

**-v**, **-vv**, **-vvv**
> 提高详细程度（facts、shell 输入、shell 输出）。

# DESCRIPTION

**pyinfra** 使用 Python 自动化基础设施供给和配置管理。部署脚本就是普通的 Python 文件，通过安装软件包、管理文件、配置服务以及在成组服务器上执行命令等操作来描述期望的系统状态。

该工具通过 SSH 连接目标，无需在远程机器上安装代理，因此采用成本很低。inventory 文件定义目标主机和分组，部署脚本指定要运行的操作。**--dry** 标志可在应用前预览变更；**fact** 命令从目标采集系统信息，用于部署中的条件逻辑。

# CONFIGURATION

**inventory.py**
> 默认 inventory 文件，定义部署的目标主机、分组和连接信息。

**deploy.py**
> 默认部署脚本，包含要在目标主机上执行的操作。

**group_data/*.py**
> 组级数据文件，为 inventory 中定义的主机组提供变量。

**config.py**
> 项目级配置，涵盖 SSH 设置、sudo 行为和操作默认值。

# CAVEATS

需要 Python。基于 SSH 的部署方式。

# HISTORY

pyinfra 为实现基于 **Python 的**基础设施自动化而创建。

# INSTALL

```nix: nix profile install nixpkgs#pyinfra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ansible](/man/ansible)(1), [fabric](/man/fabric)(1), [salt](/man/salt)(1)
