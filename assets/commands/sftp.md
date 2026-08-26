# TAGLINE

基于 SSH 的安全交互式文件传输

# TLDR

**连接到远程服务器**

```sftp [user]@[hostname]```

**使用指定端口连接**

```sftp -P [port] [user]@[hostname]```

**上传文件**

```sftp> put [local_file] [remote_path]```

**下载文件**

```sftp> get [remote_file] [local_path]```

**递归上传目录**

```sftp> put -r [local_directory]```

**递归下载目录**

```sftp> get -r [remote_directory]```

**列出远程目录**

```sftp> ls```

**切换远程目录**

```sftp> cd [remote_path]```

# SYNOPSIS

**sftp** [**-P** _port_] [**-i** _identity_file_] [_user_**@**]_host_[**:**_path_]

# PARAMETERS

**-P** _port_
> 连接到指定端口（注意：是大写 P，与 ssh 不同）

**-i** _identity_file_
> 使用指定的私钥文件

**-b** _batchfile_
> 批处理模式；从文件读取命令

**-C**
> 启用压缩

**-r**
> 递归复制目录（配合 get/put 使用）

**-v**
> 详细模式

**-o** _option_
> 向 SSH 传递选项（例如 -o "ProxyJump=jump-host"）

# INTERACTIVE COMMANDS

**ls** [_path_]: 列出远程目录
**lls** [_path_]: 列出本地目录
**cd** _path_: 切换远程目录
**lcd** _path_: 切换本地目录
**pwd**: 显示远程工作目录
**lpwd**: 显示本地工作目录
**get** [**-r**] _remote_ [_local_]: 下载文件/目录
**put** [**-r**] _local_ [_remote_]: 上传文件/目录
**mkdir** _path_: 创建远程目录
**rmdir** _path_: 删除远程目录
**rm** _file_: 删除远程文件
**rename** _old_ _new_: 重命名远程文件
**chmod** _mode_ _file_: 更改远程文件权限
**chown** _uid_ _file_: 更改远程文件所有者
**!** _command_: 执行本地 shell 命令
**exit** 或 **quit**: 关闭连接

# DESCRIPTION

**sftp** 是 SSH 文件传输协议客户端，通过 SSH 连接提供安全的交互式文件传输。它提供熟悉的类 FTP 界面，同时使用 SSH 进行身份验证和加密。

与 FTP 不同，SFTP 对包括凭据和文件内容在内的所有数据进行加密。它使用单一连接（没有独立的数据通道），因此对防火墙友好。

该界面既支持交互式使用，也支持用于脚本的批处理模式（**-b**）。在大多数实现中，本地和远程路径都支持 Tab 补全。

SFTP 无需在二进制和文本模式之间切换即可传输文件，并保留权限和时间戳等文件属性。

# CONFIGURATION

**~/.ssh/config**
> SSH 客户端配置文件；Host 别名、IdentityFile、ProxyJump 和 Port 等设置同样适用于 sftp 连接。

**~/.ssh/known_hosts**
> 已接受的服务器主机密钥数据库，由 ssh 和 scp 共享。

**/etc/ssh/ssh_config**
> 作用于所有用户的系统级 SSH 客户端配置。

# CAVEATS

端口用大写 **-P** 指定，而不是像 SSH 那样的小写 **-p**。这是常见的混淆来源。

SFTP 与 FTPS（FTP over SSL/TLS）不同。SFTP 使用 SSH；FTPS 则是在 FTP 协议上加 TLS 加密。

对于自动化传输，请使用批处理模式（**-b**），或者考虑通过 SSH 使用 **rsync** 来完成更复杂的同步。

默认情况下会跟随符号链接。使用 **get -P** 或 **put -P** 可以将符号链接保留为链接本身。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-client-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [ssh](/man/ssh)(1), [rsync](/man/rsync)(1), [ftp](/man/ftp)(1)
