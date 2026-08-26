# TAGLINE

基于 TUI 列表的 SSH、SCP 与 SFTP 客户端

# TLDR

**启动 SSH 连接列表**

```lssh```

**启动 SCP 客户端**

```lscp```

**启动 SFTP 客户端**

```lsftp```

# SYNOPSIS

**lssh** [_options_]

# DESCRIPTION

**lssh** 是一个基于 TUI 列表选择的 SSH、SCP 和 SFTP 连接客户端。它读取你的 OpenSSH 配置（~/.ssh/config），将服务器呈现在可选择的列表中，方便快速连接。

功能包括支持密码、公钥、证书以及 PKCS11（Yubikey）认证、在 SSH 目的地使用本地机器的 bashrc，以及 NFS 正向/反向转发支持。

# CAVEATS

需要 OpenSSH 配置文件。认证方式取决于服务器端的配置。

# HISTORY

**lssh** 由 **blacknon** 创建，使用 **Go** 编写。可在 Linux、macOS 和 Windows 上运行。

# SEE ALSO

[ssh](/man/ssh)(1), [scp](/man/scp)(1), [sftp](/man/sftp)(1), [lazyssh](/man/lazyssh)(1)
