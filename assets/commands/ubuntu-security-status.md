# TAGLINE

显示软件包的安全支持状态

# TLDR

显示**不受支持**的软件包数量

```ubuntu-security-status```

列出**不可用**的软件包

```ubuntu-security-status --unavailable```

列出**第三方**软件包

```ubuntu-security-status --thirdparty```

# SYNOPSIS

**ubuntu-security-status** [_OPTIONS_]

# PARAMETERS

**--unavailable**
> 列出已无法下载的软件包

**--thirdparty**
> 列出来自第三方来源的软件包

# DESCRIPTION

**ubuntu-security-status** 显示已安装 Ubuntu 软件包的安全支持状态信息。它会识别可能不再接收安全更新的软件包。

该工具通过识别超出官方支持期的软件包或来自非官方来源的软件包，帮助管理员了解系统的安全状况。

# CAVEATS

Ubuntu 专用。结果取决于当前 Ubuntu 发行版及其支持状态。第三方软件包可能有各自的安全策略。

# SEE ALSO

[apt](/man/apt)(8), [pro](/man/pro)(1)
