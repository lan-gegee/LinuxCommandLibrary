# TAGLINE

通过 FUSE 在 SSH 上挂载远程文件系统

# TLDR

**通过 SSH 挂载远程目录**

```sshfs [user]@[host]:[remote/path] [local/mountpoint]```

**使用指定的 SSH 端口挂载**

```sshfs [user]@[host]:[remote/path] [local/mountpoint] -p [2222]```

**使用 SSH 密钥认证挂载**

```sshfs -o IdentityFile=[~/.ssh/key] [user]@[host]:[path] [mountpoint]```

**挂载时允许其他用户**访问该挂载点

```sshfs -o allow_other [user]@[host]:[path] [mountpoint]```

**卸载远程文件系统**

```fusermount -u [mountpoint]```

**断线时自动重连**挂载

```sshfs -o reconnect [user]@[host]:[path] [mountpoint]```

# SYNOPSIS

**sshfs** [_-o options_] [_user@_]_host_:[_dir_] _mountpoint_

# PARAMETERS

**-o** _options_
> 挂载选项（以逗号分隔）

**-p** _port_
> 要连接的 SSH 端口

**-C**
> 启用压缩

**-F** _ssh_config_
> 要使用的 SSH 配置文件

**-1**
> 使用 SSH 协议版本 1

**-o IdentityFile=**_file_
> SSH 私钥路径

**-o allow_other**
> 允许其他用户访问该挂载点

**-o allow_root**
> 允许 root 访问该挂载点

**-o reconnect**
> 连接断开时重新连接到服务器

**-o ServerAliveInterval=**_seconds_
> 发送保活消息以防超时

**-o StrictHostKeyChecking=no**
> 不验证主机密钥（谨慎使用）

**-o cache=yes**
> 启用缓存（可提升性能）

**-o kernel_cache**
> 启用内核缓存

**-o idmap=user**
> 将远程用户的 UID/GID 映射到本地挂载用户

**-o transform_symlinks**
> 将绝对符号链接改写为相对于挂载点的相对链接

**-o follow_symlinks**
> 在服务器侧跟随符号链接

**-o max_conns=**_N_
> 并发 SSH 连接的最大数量

**-f**
> 在前台运行（用于调试）

**-d**
> 调试模式

# DESCRIPTION

**sshfs** 是一个基于 FUSE（用户空间文件系统）的文件系统客户端，允许你通过 SSH 连接挂载远程目录。挂载完成后，远程文件系统可以像任何本地目录一样访问，并使用标准的文件操作。

该工具使用 SSH 协议进行安全数据传输，并复用现有的 SSH 配置，包括来自 **~/.ssh/config** 的身份验证密钥、代理设置和主机配置。在已经具备 SSH 访问条件的情况下，它是替代 NFS 或 Samba 访问远程文件的绝佳选择。

SSHFS 对开发工作流特别有用，可以让本地编辑器和工具透明地处理远程文件。它能优雅地处理连接中断，并在网络恢复后自动重连。

# CAVEATS

由于 SSH 加密的开销，性能比本地文件系统或 NFS 慢。**allow_other** 选项需要在 **/etc/fuse.conf** 中设置 **user_allow_other**。在 macOS 上需要安装 macFUSE。网络延迟会直接影响文件操作速度。由于文件系统抽象层的开销，大文件传输可能比 **scp** 或 **rsync** 慢。

# HISTORY

**sshfs** 由 **Miklos Szeredi** 创建，于 **2004 年**首次发布，是最早基于 FUSE 的文件系统之一。它展示了用户空间文件系统的强大能力，并成为许多其他 FUSE 实现的典范。该项目一直得到积极维护，并在类 Unix 系统上被广泛采用。在 Linux 上，它已成为标准 FUSE 工具集的一部分；macOS 用户则依赖 macFUSE（原名 OSXFUSE）来获得兼容性。

# INSTALL

```apt: sudo apt install sshfs```

```pacman: sudo pacman -S sshfs```

```apk: sudo apk add sshfs```

```zypper: sudo zypper install sshfs```

```brew: brew install sshfs```

```nix: nix profile install nixpkgs#sshfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [fusermount](/man/fusermount)(1), [mount](/man/mount)(8), [scp](/man/scp)(1), [rsync](/man/rsync)(1)
