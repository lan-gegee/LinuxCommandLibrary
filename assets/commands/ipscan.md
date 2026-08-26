# TAGLINE

快速、跨平台的网络扫描器，可扫描 IP 地址和端口

# TLDR

**启动 Angry IP Scanner** 图形界面

```ipscan```

从命令行**扫描单个 IP 地址**

```ipscan -s -f:txt -o [output.txt] [192.168.1.1]```

**扫描一段 IP 范围**并保存结果

```ipscan -s -f:txt -o [output.txt] [192.168.1.1] [192.168.1.254]```

**使用包含 IP 地址的文件**进行扫描

```ipscan -s -f:csv -o [output.csv] -ff:[iplist.txt]```

**扫描并以 XML 格式导出**

```ipscan -s -f:xml -o [output.xml] [192.168.1.0/24]```

**扫描指定端口并在完成后退出**

```ipscan -s -q -f:txt -o [output.txt] -p [80,443,8080] [192.168.1.1] [192.168.1.254]```

# SYNOPSIS

**ipscan** [_-s_] [_-f:format_] [_-o filename_] [_-ff:filename_] [_start-ip_] [_end-ip_]

# PARAMETERS

**-s**
> 以静默（命令行）模式运行，不显示图形界面

**-f:format**
> 输出格式：txt、csv、xml、ip-port

**-o** _filename_
> 扫描结果的输出文件名

**-ff:** _filename_
> 从文件读取 IP 地址

**-q**
> 扫描完成后退出（配合 -s 使用）。

**-a**
> 追加到输出文件而不是覆盖。

**-p** _ports_
> 指定要扫描的端口。

**-d** _ms_
> 每次请求之间的延迟（毫秒）。

# DESCRIPTION

**ipscan**（Angry IP Scanner）是一款快速、跨平台的网络扫描器，可扫描 IP 地址和端口。它使用多线程提升速度，能够检测存活主机、解析主机名、扫描端口并获取 NetBIOS 信息。

该工具既可以作为 GUI 应用交互式使用，也可以在命令行模式下运行，便于脚本化和自动化。它支持多种输出格式，方便与其他工具集成。

# CAVEATS

过高的扫描速率可能触发 IDS/IPS 告警或违反网络策略。某些功能需要管理员权限。未经授权进行端口扫描在部分司法辖区可能违法。图形界面需要安装 Java。

# HISTORY

**Angry IP Scanner** 由 Anton Keks 创建，于 **2001 年**首次发布。最初为 Windows 编写，约在 **2007 年**用 Java 重写以实现跨平台。它至今仍是最受欢迎的开源网络扫描器之一，下载量达数百万次。

# INSTALL

```nix: nix profile install nixpkgs#ipscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [ping](/man/ping)(1), [netcat](/man/netcat)(1)
