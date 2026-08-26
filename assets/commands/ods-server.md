# TAGLINE

openDNSSEC 签名守护进程

# TLDR

**启动 ODS 服务**

```ods-server```

**在特定端口启动**

```ods-server -p [port]```

**使用指定配置启动**

```ods-server -c [config.conf]```

**在前台运行**

```ods-server -f```

# SYNOPSIS

**ods-server** [_options_]

# PARAMETERS

**-p** _PORT_
> 监听端口。

**-c** _FILE_
> 配置文件。

**-f**
> 在前台运行。

**-d**
> 调试模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ods-server** 是 OpenDNSSEC 的签名守护进程，使用 DNSSEC 对 DNS 区域进行签名。

该守护进程负责区域签名操作，属于 OpenDNSSEC 套件的一部分。

# CAVEATS

属于 OpenDNSSEC 的一部分。需要正确的配置。与 KASP 策略配合使用。

# HISTORY

ods-server 作为 **OpenDNSSEC** 的一部分开发，用于自动化 DNSSEC 签名。

# SEE ALSO

[ods-control](/man/ods-control)(1), [ods-enforcer](/man/ods-enforcer)(1), [named](/man/named)(1)
