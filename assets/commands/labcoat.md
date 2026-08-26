# TAGLINE

基于 flakes 部署 NixOS 系统的 TUI

# TLDR

**启动部署 TUI**

```labcoat```

**从指定的 flake 部署**

```labcoat [path/to/flake]```

# SYNOPSIS

**labcoat** [_options_] [_flake_path_]

# DESCRIPTION

**labcoat** 是一个基于 flakes 部署 NixOS 系统的终端用户界面。它会自动从你的 flake 配置中发现主机，并提供一条命令来部署或检查这些机器。

功能包括：直接通过 SSH 访问目标机器、远程执行 Shell 命令、重启机器并结合基于 ping 的状态监控、按节点记录部署日志，以及标记过期的系统。

该工具面向爱好者和需要管理小型基础设施的 NixOS 用户——最多几十台机器的集群或家庭实验室——尤其适合在开发和测试阶段对配置进行快速迭代时使用。

# CAVEATS

需要有 NixOS flake 配置。专为小规模部署设计；对于更大规模的基础设施，建议考虑专门的部署方案。

# HISTORY

**labcoat** 由 **jhillyerd** 创建，使用 **Go** 编写。

# SEE ALSO

[nixos-rebuild](/man/nixos-rebuild)(8), [ssh](/man/ssh)(1)
