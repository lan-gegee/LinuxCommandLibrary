# TAGLINE

查询 NetBIOS 名称并将其解析为 IP 地址

# TLDR

**查找 NetBIOS 名称**

```nmblookup [hostname]```

**通过广播查找**

```nmblookup -B [192.168.1.255] [hostname]```

**查询特定 WINS 服务器**

```nmblookup -U [wins_server] [hostname]```

**按 IP 地址查找**（反向查询）

```nmblookup -A [192.168.1.100]```

**显示主浏览器**

```nmblookup -M -- -```

**列出工作组成员**

```nmblookup -S [WORKGROUP]```

**递归查询**

```nmblookup -R [hostname]```

# SYNOPSIS

**nmblookup** [_-B broadcast_] [_-U unicast_] [_-A_] [_-M_] [_options_] _name_

# PARAMETERS

**-B** _ADDR_
> 广播地址。

**-U** _ADDR_
> 单播地址（WINS 服务器）。

**-A**
> 节点状态查询（反向查找）。

**-M**
> 搜索主浏览器。

**-R**
> 通过 WINS 进行递归查询。

**-S**
> 返回完整的节点状态。

**-d** _LEVEL_
> 调试级别。

**-s** _FILE_
> smb.conf 文件的位置。

**-r**
> 使用 /etc/hosts。

**-T**
> 转换为 DNS 名称。

**--usage**
> 显示用法。

# DESCRIPTION

**nmblookup** 查询 NetBIOS 名称并将其解析为 IP 地址。它相当于 DNS 领域中 nslookup 的 NetBIOS 版本。

NetBIOS 名称解析在 Windows 网络中出现得比 DNS 更早。机器会在网络上注册名称，nmblookup 则找出它们的 IP 地址。

广播模式向本地网段发送查询。WINS（Windows Internet Name Service）则通过服务器提供全网范围的名称解析。

节点状态查询（-A）会显示一台主机注册的所有 NetBIOS 名称，包括共享资源、工作组成员身份和服务名称。

主浏览器查询可找到管理工作组浏览列表的计算机，有助于诊断网络浏览问题。

该工具与 Samba 配置集成，使用 smb.conf 设置作为默认值。

# CAVEATS

NetBIOS 是一项遗留技术。广播查询只能到达本地子网。WINS 服务器已越来越少见。现代网络更倾向于使用 DNS。

# HISTORY

**nmblookup** 是 **Samba** 套件的一部分，自 **20 世纪 90 年代**起由 **Andrew Tridgell** 和 Samba 团队开发。它提供用于与 Windows 网络互操作的 Unix/Linux 工具。

# INSTALL

```apt: sudo apt install samba-common-bin```

```dnf: sudo dnf install samba-client```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [net](/man/net)(8), [nbtscan](/man/nbtscan)(1), [nslookup](/man/nslookup)(1)
