# TAGLINE

Exoscale 计算实例与基础设施管理

# TLDR

**列出实例**

```exo compute instance list```

**创建实例**

```exo compute instance create [name] --template [Linux Ubuntu] --zone [ch-gva-2]```

**启动实例**

```exo compute instance start [name]```

**停止实例**

```exo compute instance stop [name]```

**删除实例**

```exo compute instance delete [name]```

**SSH 登录实例**

```exo compute instance ssh [name]```

**显示实例详情**

```exo compute instance show [name]```

# SYNOPSIS

**exo compute** _resource_ _action_ [_options_]

# PARAMETERS

_RESOURCE_
> 资源类型：instance、template、security-group 等。

_ACTION_
> 操作：list、create、delete、start、stop、show。

**--template** _NAME_
> 实例模板。

**--zone** _ZONE_
> 可用区。

**--type** _TYPE_
> 实例类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**exo compute** 用于管理 Exoscale 计算实例（虚拟机）。它处理从创建到删除的完整生命周期，包括电源管理。

命令支持所有实例配置，包括模板、安全组、SSH 密钥和网络设置。可用区即 Exoscale 数据中心的位置。

该子命令为 Exoscale 的计算平台提供 IaaS 管理。

# CAVEATS

实例运行期间会产生费用。可用区资源可能有限。部分模板需要特定配置。删除操作立即生效。

# HISTORY

exo compute 是 **Exoscale CLI** 的一部分，为自动化云管理提供对 Exoscale 计算基础设施的编程访问。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [exo-compute-sks](/man/exo-compute-sks)(1)

# RESOURCES

```[Source code](https://github.com/exoscale/cli)```

```[Homepage](https://www.exoscale.com/)```

<!-- verified: 2026-07-15 -->
