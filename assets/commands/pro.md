# TAGLINE

管理 Ubuntu Pro 服务与订阅

# TLDR

将系统**附加**到 Ubuntu Pro

```sudo pro attach```

显示**状态**

```pro status```

**修复**特定漏洞

```pro fix [CVE-2023-1234]```

显示**安全状态**

```pro security-status```

列出**不可用的**软件包

```pro security-status --unavailable```

列出**第三方**软件包

```pro security-status --thirdparty```

# SYNOPSIS

**pro** [**attach**|**status**|**fix**|**security-status**] [_options_]

# COMMANDS

**attach**
> 将系统连接到 Ubuntu Pro 订阅

**detach**
> 断开与 Ubuntu Pro 的连接

**status**
> 显示 Ubuntu Pro 服务状态

**fix**
> 为特定的 CVE 或 USN 应用修复

**security-status**
> 显示安全支持状态

**enable**
> 启用特定的 Pro 服务

**disable**
> 禁用特定的 Pro 服务

# PARAMETERS

**--unavailable**
> 显示不再可用的软件包

**--thirdparty**
> 显示第三方软件包

**--format _format_**
> 输出格式（json、yaml）

# DESCRIPTION

**pro** 管理 Ubuntu Pro（原 Ubuntu Advantage）的服务和订阅。它为 Ubuntu 系统提供扩展安全维护、内核实时补丁以及合规工具。

该工具可以自动应用安全修复，并提供已安装软件包安全状态的可见性。

# CAVEATS

大多数功能需要 Ubuntu Pro 订阅。个人使用可享受免费层级。某些服务需要重启才能生效。

# HISTORY

**pro** 取代了 **ubuntu-advantage-tools** 命令，为 Ubuntu 商业支持服务提供了更简单的接口。更名是为了与 Ubuntu Pro 品牌保持一致。

# SEE ALSO

[apt](/man/apt)(8), [unattended-upgrades](/man/unattended-upgrades)(8)
