# TAGLINE

通过 SMB 直接解析 NTFS 结构，从远程 Windows 系统读取文件

# TLDR

**从远程 NTFS 共享读取文件**

```impacket-ntfs-read '[domain]/[user]:[password]@[192.168.1.100]' '[C$\Windows\System32\config\SAM]'```

使用 **NTLM 哈希**身份验证**读取文件**

```impacket-ntfs-read -hashes ':[nthash]' '[domain]/[user]@[192.168.1.100]' '[share\path\to\file]'```

使用 **Kerberos** 身份验证**读取文件**

```impacket-ntfs-read -k -no-pass '[domain]/[user]@[target]' '[C$\path\to\file]'```

# SYNOPSIS

**impacket-ntfs-read** [_-h_] [_-hashes LMHASH:NTHASH_] [_-no-pass_] [_-k_] [_-aesKey KEY_] [_-dc-ip IP_] _target_ _path_

# PARAMETERS

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-no-pass**
> 不询问密码（与 -k 搭配时有用）

**-k**
> 使用 ccache 文件中的 Kerberos 身份验证

**-aesKey** _KEY_
> 用于 Kerberos 身份验证的 AES 密钥

**-dc-ip** _IP_
> 域控制器的 IP 地址（用于 Kerberos）

# DESCRIPTION

**impacket-ntfs-read** 通过 SMB 直接解析 NTFS 文件系统结构，从远程 Windows 系统读取文件。这样可以读取可能被操作系统锁定的文件，例如注册表配置单元（registry hive）或其他系统文件。

该工具连接管理共享（C$、ADMIN$），在原始 NTFS 层级读取文件，绕过 Windows 的文件锁定机制。这在渗透测试期间提取敏感文件时尤其有用。

# CAVEATS

需要对目标系统的管理员访问权限（能访问 C$ 或 ADMIN$ 共享）。某些文件仍可能因 NTFS 权限而无法访问。路径应使用反斜杠并引用共享名。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。该工具实现了基于 SMB 的 NTFS 解析以读取被锁定的文件，这是凭据提取工作流中常用的技术。

# SEE ALSO

[impacket-secretsdump](/man/impacket-secretsdump)(1), [smbclient](/man/smbclient)(1), [impacket-smbclient](/man/impacket-smbclient)(1)
