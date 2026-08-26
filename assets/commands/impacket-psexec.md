# TAGLINE

通过 SMB 在远程 Windows 系统上执行命令

# TLDR

**在远程主机上执行命令**

```impacket-psexec [domain]/[user]:[password]@[target] [command]```

**获取交互式 shell**

```impacket-psexec [domain]/[user]:[password]@[target]```

**使用 NTLM 哈希代替密码**

```impacket-psexec -hashes :[hash] [domain]/[user]@[target]```

**指定服务名**

```impacket-psexec -service-name [name] [domain]/[user]:[password]@[target]```

# SYNOPSIS

**impacket-psexec** [_options_] _target_ [_command_]

# PARAMETERS

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希进行身份验证（LM 哈希可以为空）。

**-k**
> 使用 Kerberos 身份验证。从 ccache 文件（KRB5CCNAME）获取凭据。

**-no-pass**
> 不询问密码（与 -k 搭配时有用）。

**-aesKey** _HEX_
> 用于 Kerberos 身份验证的 AES 密钥（128 或 256 位）。

**-dc-ip** _IP_
> 域控制器的 IP。

**-target-ip** _IP_
> 目标 IP（覆盖目标主机名的解析结果）。

**-service-name** _NAME_
> SMB 服务器共享的名称。

**-remote-binary-name** _NAME_
> 目标上的自定义远程二进制文件名（默认：随机）。

**-codec** _CODEC_
> 用于解码远程 stdout 的输出编码（默认：随区域设置）。

**-debug**
> 启用详细的调试输出。

# DESCRIPTION

**impacket-psexec** 通过 SMB 在远程 Windows 系统上执行命令。属于 Impacket 工具集。其工作原理是向 ADMIN$ 共享上传一个服务可执行文件，然后通过服务控制管理器启动它。需要管理员凭据。用于经授权的渗透测试和系统管理。

# CAVEATS

需要对目标的管理员访问权限。会在目标系统上留下痕迹。仅限用于经授权的安全测试。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-smbclient](/man/impacket-smbclient)(1)
