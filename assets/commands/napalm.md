# TAGLINE

支持多厂商的网络自动化库

# TLDR

**获取设备信息**

```napalm --user [admin] --password [pass] --vendor [ios] [192.168.1.1] call get_facts```

**获取接口**

```napalm --user [admin] --password [pass] --vendor [junos] [device] call get_interfaces```

**配置设备**

```napalm --user [admin] --password [pass] --vendor [eos] [device] configure [config.txt]```

**校验配置**

```napalm --user [admin] --password [pass] --vendor [nxos] [device] validate [validation.yml]```

# SYNOPSIS

**napalm** [_options_] _hostname_ _command_ [_args_]

# PARAMETERS

**--user** _username_
> 设备用户名。

**--password** _password_
> 设备密码。

**--vendor** _vendor_
> 设备厂商（ios、junos、eos、nxos）。

**--optional_args** _args_
> 可选的连接参数。

**call** _method_
> 调用 NAPALM 方法。

**configure** _file_
> 应用配置。

**validate** _file_
> 校验配置。

# DESCRIPTION

**NAPALM**（Network Automation and Programmability Abstraction Layer with Multivendor support）是一个用于网络自动化的 Python 库。它提供统一的 API 来与不同网络厂商的设备交互。

CLI 工具提供对 NAPALM 功能的快速访问。

# SUPPORTED VENDORS

```
ios, iosxr, nxos, eos
junos, fortios, panos
```

# CAVEATS

需要厂商专用库。必须配置 SSH/API 访问。Python 库比 CLI 更强大。

# HISTORY

NAPALM 由 **David Barroso** 等人于 **2015 年**在 Spotify 创建，旨在简化多厂商网络自动化。

# INSTALL

```nix: nix profile install nixpkgs#napalm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netmiko](/man/netmiko)(1), [ansible](/man/ansible)(1)
