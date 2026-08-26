# TAGLINE

功能全面的 IPP 打印机和服务器测试工具

# TLDR

从 IPP 打印机**获取打印机属性**

```ipptool -tv [ipp://printer.local/ipp/print] get-printer-attributes.test```

对打印机**运行测试文件**

```ipptool [ipp://printer.local/ipp/print] [test.ipp]```

**提交一个打印作业**进行测试

```ipptool -f [document.pdf] [ipp://printer.local/ipp/print] print-job.test```

**以详细输出进行测试**

```ipptool -tv [ipp://printer.local/ipp/print] [test.ipp]```

**运行一致性测试**

```ipptool -tIv [ipp://printer.local/ipp/print] ipp-everywhere.test```

# SYNOPSIS

**ipptool** [_-tv_] [_-f filename_] [_-d name=value_] _printer-uri_ _testfile_ [_... testfile_]

# PARAMETERS

**-t**
> 生成 CUPS 风格的测试报告输出。

**-v**
> 详细模式；显示每个请求和响应属性。

**-q**
> 安静模式；抑制常规摘要输出。

**-l**
> 生成纯文本（列表）输出而非默认报告。

**-c**
> 生成逗号分隔（CSV）输出。

**-X**
> 生成 Apple plist XML 输出。

**-P** _FILE_
> 在生成常规报告之外，将机器可读的 plist XML 结果写入 _FILE_。

**-f** _FILENAME_
> 用作 print-job 测试文档数据的文件。

**-d** _name=value_
> 定义测试文件中可用的变量（可重复使用）。

**-I**
> 忽略错误并继续下一个测试，而不是中止。

**-S**
> 连接打印机时使用加密（TLS/SSL）。

**-T** _SECONDS_
> 请求超时时间（秒）。

**-V** _VERSION_
> 要声明的 IPP 版本（**1.0**、**1.1**、**2.0**、**2.1**、**2.2**）。

**-4**, **-6**
> 分别强制使用 IPv4 或 IPv6 连接。

**-C**
> 对请求使用 HTTP/1.1 分块传输编码。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ipptool** 是一款功能全面的 IPP（Internet Printing Protocol，互联网打印协议）打印机和服务器测试工具。它根据测试文件发送 IPP 请求并验证响应，是打印机一致性测试与调试的必备工具。

测试文件以简单的文本格式定义 IPP 操作和预期响应。该工具附带标准测试文件，涵盖获取打印机属性、提交作业以及 IPP Everywhere 一致性测试等常见操作。

# CAVEATS

创建自定义测试文件需要了解 IPP 协议。某些测试可能会修改打印机状态或产生实际的打印输出。打印机 URI 格式因打印机型号和制造商而异。

# HISTORY

**ipptool** 是 **CUPS** 的一部分，由 Michael Sweet 开发。它由更早期的 IPP 测试工具演化而来，成为 IPP 一致性测试的参考实现，被打印机制造商用于验证 IPP Everywhere 合规性。

# INSTALL

```apt: sudo apt install cups-ipp-utils```

```apk: sudo apk add ipptool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ippfind](/man/ippfind)(1), [ippeveprinter](/man/ippeveprinter)(1), [lpstat](/man/lpstat)(1), [lp](/man/lp)(1)
