# TAGLINE

Exoscale 虚拟机生命周期管理

# TLDR

**列出实例**

```exo compute instance list```

**创建实例**

```exo compute instance create [name] --zone [ch-gva-2] --template [Linux Ubuntu]```

**显示实例详情**

```exo compute instance show [name]```

**启动实例**

```exo compute instance start [name]```

**停止实例**

```exo compute instance stop [name]```

**删除实例**

```exo compute instance delete [name]```

**SSH 登录实例**

```exo compute instance ssh [name]```

# SYNOPSIS

**exo** **compute** **instance** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出实例。

**create**
> 创建实例。

**show**
> 显示实例详情。

**start**
> 启动实例。

**stop**
> 停止实例。

**reboot**
> 重启实例。

**delete**
> 删除实例。

**ssh**
> SSH 登录实例。

**resize**
> 调整实例规格。

# DESCRIPTION

**exo compute instance** 用于管理 Exoscale 计算实例（虚拟机）。它处理从创建到删除的完整生命周期，包括电源管理和配置。

实例运行在指定的可用区中，可配置模板、实例类型、安全组和 SSH 密钥。该工具提供便捷的 SSH 访问和管理能力，无需使用 Web 控制台。

命令支持所有实例操作，包括调整规格、重启以及连接网络和存储。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [exo-compute](/man/exo-compute)(1), [exo-compute-block-storage](/man/exo-compute-block-storage)(1)

# RESOURCES

```[Source code](https://github.com/exoscale/cli)```

```[Homepage](https://www.exoscale.com/)```

<!-- verified: 2026-07-15 -->
