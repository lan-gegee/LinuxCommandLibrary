# TAGLINE

在 Debian 系统上配置 PPPoE

# TLDR

**配置 PPPoE 连接**

```pppoeconf```

**使用指定接口运行**

```pppoeconf [eth0]```

# SYNOPSIS

**pppoeconf** [_interface_]

# PARAMETERS

_INTERFACE_
> 网络接口。

# DESCRIPTION

**pppoeconf** 是一个 Debian 特有的交互式工具，可自动检测并配置 PPPoE DSL 连接。它扫描网络接口以查找 PPPoE 接入集中器，提示输入身份验证凭据，并创建所需的系统配置文件。

该向导处理完整的设置流程，包括接口选择、凭据存储、DNS 配置，以及与系统网络脚本的集成，使连接在启动时自动建立。

# CAVEATS

Debian 专用。需要 root 权限。

# HISTORY

pppoeconf 是为 **Debian** 的 PPPoE 配置而创建的。

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-setup](/man/pppoe-setup)(8), [pppd](/man/pppd)(8)
