# TAGLINE

找出安全支持受限的已安装软件包

# TLDR

显示支持**受限或已终止**的软件包

```check-support-status```

仅显示支持**已终止**的软件包

```check-support-status --type ended```

显示安全支持**受限**的软件包

```check-support-status --type limited```

跳过输出**标题**

```check-support-status --no-heading```

将特定软件包**排除**在警报之外

```check-support-status --except [package1,package2]```

# SYNOPSIS

**check-support-status** [_options_]

# DESCRIPTION

**check-support-status** 找出安全支持已被限制或提前终止的已安装 Debian 软件包。这有助于用户了解哪些软件包可能不会再收到安全更新。它是 **debian-security-support** 软件包的一部分。

该工具报告那些早于发行版支持期就到达生命周期的软件包，以及因各种原因安全支持受限的软件包。

# PARAMETERS

**--type** _type_
> 按支持状态类型过滤：**ended**（支持已终止）、**limited**（支持受限）或 **earlyend**（支持比发行版的更早结束）。

**--no-heading**
> 跳过标题输出。

**--except** _PACKAGES_
> 对给定的逗号分隔二进制软件包不发出警报。

**--list** _FILE_
> 使用给定文件作为软件包及其支持状态的数据库。

**--status-db** _FILE_
> 使用给定文件记录警报，使每个受影响的软件包只被报告一次。

**--version**, **-V**
> 显示版本号并退出。

# CAVEATS

仅适用于基于 Debian 的发行版。软件包支持状态取决于 Debian 安全团队的决定，可能会变化。默认根据运行所在的 Debian 版本评估状态；可通过 **DEBIAN_VERSION** 环境变量覆盖。

# SEE ALSO

[apt](/man/apt)(8), [apt-cache](/man/apt-cache)(8), [debsecan](/man/debsecan)(1)
