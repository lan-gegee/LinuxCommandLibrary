# TAGLINE

Web 应用负载测试工具

# TLDR

**启动图形界面**

```jmeter```

**运行测试计划**

```jmeter -n -t [test.jmx]```

**运行并记录日志输出**

```jmeter -n -t [test.jmx] -l [results.jtl]```

**生成 HTML 报告**

```jmeter -n -t [test.jmx] -l [results.jtl] -e -o [report/]```

**带属性运行**

```jmeter -n -t [test.jmx] -J[threads=100]```

**远程分布式测试**

```jmeter -n -t [test.jmx] -R [server1,server2]```

# SYNOPSIS

**jmeter** [_options_]

# PARAMETERS

**-n**
> 非 GUI 模式。

**-t** _FILE_
> 测试计划文件（.jmx）。

**-l** _FILE_
> 日志结果文件（.jtl）。

**-e**
> 测试结束后生成报告。

**-o** _DIR_
> 报告输出目录。

**-J**_PROP=VALUE_
> 设置属性。

**-R** _SERVERS_
> 远程服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**JMeter** 是一款 Web 应用负载测试工具。它通过向服务器施加高负载来测试其性能。

该工具支持 HTTP、JDBC、FTP 等多种协议，并提供图形化的测试设计与结果分析功能。

# CAVEATS

基于 Java。大型测试会消耗大量资源。GUI 用于设计测试，CLI 用于执行测试。

# HISTORY

Apache JMeter 由 **Stefano Mazzocchi** 开发，作为负载测试工具问世，后来成为 Web 性能测试的事实标准。

# INSTALL

```brew: brew install jmeter```

```nix: nix profile install nixpkgs#jmeter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ab](/man/ab)(1), [siege](/man/siege)(1), [wrk](/man/wrk)(1), [k6](/man/k6)(1)
