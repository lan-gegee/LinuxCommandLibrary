# TAGLINE

通过网络在主机之间复制文件

# TLDR

将**文件**复制到远程主机

```rcp path/to/local_file username@remote_host:/path/to/destination/```

递归复制**目录**

```rcp -r path/to/local_directory username@remote_host:/path/to/destination/```

**保留**文件属性

```rcp -p path/to/local_file username@remote_host:/path/to/destination/```

**强制**复制且不询问确认

```rcp -f path/to/local_file username@remote_host:/path/to/destination/```

# SYNOPSIS

**rcp** [_options_] _source_ _destination_

# PARAMETERS

**-r**, **--recursive**
> 递归复制目录

**-p**, **--preserve**
> 保留文件属性（模式、所有者、时间戳）

**-f**, **--from**
> 强制复制且不询问确认

# DESCRIPTION

**rcp** 在本地与远程系统之间复制文件。它的行为模仿 cp 命令，但通过 RSH 协议跨机器操作。

源或目标可以写成 user@host:path 的形式来指定远程位置。

# CAVEATS

rcp 以未加密方式传输数据，被认为不安全。请改用基于 SSH 的 scp 或 rsync 进行安全文件传输。

# HISTORY

属于 **GNU inetutils** 的一部分，提供经典 Unix 网络工具。如今大多已被 scp 和 rsync 等安全替代品取代。

# INSTALL

```nix: nix profile install nixpkgs#rcp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [rsync](/man/rsync)(1), [cp](/man/cp)(1), [rsh](/man/rsh)(1)
