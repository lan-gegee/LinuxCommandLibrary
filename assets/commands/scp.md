# TAGLINE

通过 SSH 安全地复制文件

# TLDR

**将本地文件复制到远程主机**

```scp [path/to/file] [user]@[host]:[path/to/destination]```

**将远程主机上的文件复制**到本地

```scp [user]@[host]:[path/to/file] [path/to/destination]```

**递归复制目录**

```scp -r [path/to/directory] [user]@[host]:[path/to/destination]```

**使用指定的 SSH 端口**

```scp -P [2222] [path/to/file] [user]@[host]:[path/to/destination]```

**使用指定的身份文件**（SSH 密钥）

```scp -i [~/.ssh/id_rsa] [path/to/file] [user]@[host]:[path/to/destination]```

**启用压缩进行复制**

```scp -C [path/to/file] [user]@[host]:[path/to/destination]```

**保留文件属性**

```scp -p [path/to/file] [user]@[host]:[path/to/destination]```

经由本地在**两台远程主机之间复制**

```scp -3 [user1]@[host1]:[file] [user2]@[host2]:[destination]```

# SYNOPSIS

**scp** [_options_] _source_ _destination_

**scp** [_options_] [[_user_@]_host_:]_file_ [[_user_@]_host_:]_file_

# PARAMETERS

**-r**
> 递归复制目录

**-P** _PORT_
> 连接到远程主机的指定端口

**-p**
> 保留修改时间、访问时间和权限模式

**-C**
> 启用压缩

**-c** _CIPHER_
> 选择加密算法

**-i** _FILE_
> 用于身份验证的身份文件（私钥）

**-l** _KBITS_
> 限制带宽（Kbit/s）

**-o** _OPTION_
> 向 ssh 传递选项（ssh_config 格式）

**-F** _FILE_
> 使用指定的 ssh 配置文件

**-q**
> 安静模式；隐藏进度条和警告

**-v**
> 详细模式；显示调试消息

**-B**
> 批处理模式；禁用密码提示

**-3**
> 通过本地主机在两台远程主机之间复制

**-4**
> 仅使用 IPv4

**-6**
> 仅使用 IPv6

**-S** _PROGRAM_
> 使用指定程序建立加密连接

# DESCRIPTION

**scp**（secure copy，安全复制）通过 SSH 在主机之间传输文件。它使用 SSH 进行身份验证和加密，提供与 SSH 会话相同的安全性。冒号（**:**）用于区分远程路径和本地路径。

文件可以从本地复制到远程、从远程复制到本地，或在两台远程主机之间复制。复制目录时使用 **-r** 进行递归传输。远程路径语法为 **[user@]host:path**，其中 user 默认为当前用户名。

身份验证使用 SSH 密钥或密码，可通过 ssh_config 或命令行选项配置。除非指定 **-q**，否则会显示传输进度。命令成功时退出码为 0，出错时大于 0。

# CAVEATS

scp 使用较旧的协议（SCP/RCP），存在安全限制。OpenSSH 项目建议新脚本改用 **sftp** 或基于 SSH 的 **rsync**。远程路径中的通配符必须加引号，以防止本地 shell 展开。在不使用 **-3** 的情况下在两台远程主机之间复制时，两台主机将直接连接；如果它们无法互相访问则会失败。

# HISTORY

scp 源于 **Tatu Ylönen** 于 **1995 年**在赫尔辛基理工大学开发的 **SSH** 协议套件。它被设计为不安全的 **rcp**（remote copy）命令的安全替代品。始于 **1999 年**的 OpenSSH 项目提供了使用最广泛的实现。虽然 scp 仍然可用，但其底层协议存在已知问题，因此官方建议新的部署改用 sftp。

# INSTALL

```apt: sudo apt install openssh-client```

```pacman: sudo pacman -S dropbear-scp```

```apk: sudo apk add dropbear-scp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sftp](/man/sftp)(1), [rsync](/man/rsync)(1), [ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1)
