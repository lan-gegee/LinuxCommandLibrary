# TAGLINE

通过 SAM、LSA 机密、缓存凭据等从 Windows 系统提取凭据

# TLDR

**从域控制器导出机密**

```impacket-secretsdump [domain]/[user]:[password]@[target]```

**使用 NTLM 哈希导出**

```impacket-secretsdump -hashes :[hash] [domain]/[user]@[target]```

**从本地 SAM 文件导出**

```impacket-secretsdump -sam [SAM] -system [SYSTEM] LOCAL```

**导出 NTDS.dit**

```impacket-secretsdump -ntds [ntds.dit] -system [SYSTEM] LOCAL```

**仅 DCSync（不读注册表）**

```impacket-secretsdump -just-dc [domain]/[user]:[password]@[dc]```

# SYNOPSIS

**impacket-secretsdump** [_options_] _target_

# PARAMETERS

**-hashes** _lm:nt_
> 使用 NTLM 哈希。

**-sam** _file_
> 本地 SAM 文件。

**-system** _file_
> 本地 SYSTEM 配置单元。

**-ntds** _file_
> NTDS.dit 文件。

**-just-dc**
> 仅通过 DCSync 提取 NTDS.dit 数据。

**-just-dc-ntlm**
> 仅提取 NTLM 哈希。

**-k**
> 使用 Kerberos 身份验证。

# DESCRIPTION

**impacket-secretsdump** 通过 SAM、LSA 机密、缓存凭据和 NTDS.dit 从 Windows 系统提取凭据。属于 Impacket 工具集。支持针对域控制器的 DCSync。仅限用于经授权的渗透测试和安全评估。

# CAVEATS

高度敏感的操作。需要管理员/域管理员权限。仅限用于经授权的安全测试。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-psexec](/man/impacket-psexec)(1)
