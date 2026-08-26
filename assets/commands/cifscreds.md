# TAGLINE

管理内核密钥环中的 CIFS 挂载凭据

# TLDR

**为 CIFS 服务器添加凭据**

```cifscreds add [server_hostname]```

**以指定用户名添加凭据**

```cifscreds add -u [username] [server_hostname]```

**为域添加凭据**

```cifscreds add -d [domain_name]```

**更新已有凭据**

```cifscreds update [server_hostname]```

**清除指定主机的凭据**

```cifscreds clear [server_hostname]```

**清除内核中的所有 CIFS 凭据**

```cifscreds clearall```

# SYNOPSIS

**cifscreds** _command_ [**-u** _username_] [**-d**] _host_|_domain_

# DESCRIPTION

**cifscreds** 在内核密钥环中为 CIFS 多用户挂载管理 NTLM 凭据。当 CIFS 文件系统在不使用 Kerberos 身份验证的情况下以 **multiuser** 选项挂载时，该工具向内核提供每用户的凭据。

凭据安全地存储在会话密钥环中，而非明文文件中，为敏感的身份验证信息提供更好的安全性。

# PARAMETERS

**Commands:**

**add**
> 添加用于连接服务器或域的凭据

**clear**
> 移除特定主机或域的凭据

**clearall**
> 移除内核中的所有 CIFS 凭据

**update**
> 用新的用户名/密码更新已存储的凭据

**Options:**

**-d, --domain**
> 将参数视为 NT 域名而非主机名

**-u, --username** _user_
> 使用指定的用户名而非当前 Unix 用户名

# CAVEATS

需要支持 **login** 密钥类型的内核（Linux 3.3+）。请使用 **pam_keyinit** 确保在登录时建立会话密钥环。

该工具会交互式提示输入密码；出于安全考虑，无法在命令行上提供密码。

# HISTORY

**cifscreds** 是 **cifs-utils** 软件包的一部分，该软件包提供与 Linux 上 CIFS/SMB 网络共享交互的工具。此工具为支持多用户挂载功能而开发，允许不同用户使用各自的凭据访问同一挂载点。

# INSTALL

```apt: sudo apt install cifs-utils```

```dnf: sudo dnf install cifs-utils```

```pacman: sudo pacman -S cifs-utils```

```zypper: sudo zypper install cifs-utils```

```nix: nix profile install nixpkgs#cifs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount.cifs](/man/mount.cifs)(8), [cifs.idmap](/man/cifs.idmap)(8), [keyctl](/man/keyctl)(1)

# RESOURCES

```[Source code](https://git.samba.org/?p=cifs-utils.git;a=summary)```

```[Documentation](https://man7.org/linux/man-pages/man1/cifscreds.1.html)```

<!-- verified: 2026-06-22 -->
