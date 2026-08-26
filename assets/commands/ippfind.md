# TAGLINE

使用 DNS-SD 在本地网络中发现 IPP 打印机和服务

# TLDR

**查找网络上所有 IPP 打印机**

```ippfind```

**查找匹配名称模式的打印机**

```ippfind --name '[*HP*]'```

**查找打印机并输出其 URI**

```ippfind --print```

**查找打印机并对每台执行命令**

```ippfind --exec [ipptool] -t '{}' [get-printer-attributes.test] \;```

**搜索指定时间**后退出

```ippfind -T [5]```

**查找具有特定能力的打印机**

```ippfind --txt-key '[pdl]' --txt-value '[*pdf*]'```

# SYNOPSIS

**ippfind** [_options_] [_regtype_[,_subtype_]] [_expressions_]

# PARAMETERS

**--name** _PATTERN_
> 将打印机名称与模式匹配（支持通配符）

**--txt-key** _KEY_
> 匹配 DNS-SD TXT 记录键

**--txt-value** _VALUE_
> 匹配 DNS-SD TXT 记录值

**--print**
> 输出每台找到的打印机的 URI

**--exec** _command_ \;
> 对每台打印机执行命令（{} 会被替换为 URI）

**-T** _seconds_
> 搜索指定的秒数后退出

**-P** _number_
> 找到指定数量的打印机后停止

**--quiet**
> 除匹配到的 URI 外不输出任何内容

**--version**
> 显示版本信息

# DESCRIPTION

**ippfind** 使用 DNS-SD（Bonjour/mDNS）在本地网络中发现 IPP（Internet Printing Protocol，互联网打印协议）打印机和服务。它可以查找打印机、按各种条件过滤结果，并对每台发现的打印机执行命令。

在无驱动打印环境中，打印机是自动发现而非手动配置的，该工具在其中不可或缺。它支持按名称、能力和 DNS-SD TXT 记录属性进行搜索。

# CAVEATS

需要网络支持 mDNS/DNS-SD（Linux 上通常由 Avahi 提供，macOS 上为 mDNSResponder）。若未配置 mDNS 反射，可能发现不了不同子网上的打印机。结果取决于打印机是否正确广告了自身的能力。

# HISTORY

**CUPS** 及 IPP 工具套件的一部分，由 Michael Sweet 开发。为支持无驱动打印的 IPP Everywhere 计划而创建，利用 PWG 标准化的 DNS-SD 实现打印机自动发现。

# INSTALL

```apt: sudo apt install cups-ipp-utils```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipptool](/man/ipptool)(1), [ippeveprinter](/man/ippeveprinter)(1), [lpstat](/man/lpstat)(1), [avahi-browse](/man/avahi-browse)(1)
