# TLDR

**将默认公钥复制**到远程主机

```ssh-copy-id [user@host]```

**复制特定的公钥**

```ssh-copy-id -i [~/.ssh/id_ed25519.pub] [user@host]```

**复制到非标准端口上的主机**

```ssh-copy-id -p [2222] [user@host]```

**试运行（dry run）**以查看会安装哪些密钥

```ssh-copy-id -n [user@host]```

不检查已有密钥而**强制复制**

```ssh-copy-id -f -i [~/.ssh/id_rsa.pub] [user@host]```

# SYNOPSIS

**ssh-copy-id** [_-f_] [_-n_] [_-s_] [_-i identity_file_] [_-p port_] [_-o ssh_option_] [_user@_]_hostname_

# PARAMETERS

**-i** _identity_file_
> 使用指定的身份文件（公钥）

**-p** _port_
> 连接远程主机的指定端口

**-f**
> 强制模式；不检查远程是否已存在该密钥

**-n**
> 试运行；打印将被安装的密钥但不实际安装

**-s**
> 复制时用 sftp 代替 cat（适用于受限 Shell）

**-o** _ssh_option_
> 向底层 ssh 命令传递选项

# DESCRIPTION

**ssh-copy-id** 将 SSH 公钥安装到远程服务器的 authorized_keys 文件中，从而启用免密认证。它通过 SSH 连接（通常使用密码认证），在需要时创建 ~/.ssh 目录和 authorized_keys 文件，然后追加你的公钥。

该脚本确保设置正确的权限：~/.ssh 目录为 700，authorized_keys 为 600——这是 SSH 出于安全考虑的要求。权限不正确会导致认证失败。

默认情况下，ssh-copy-id 使用 ssh-add -L 输出的密钥或最新的 ~/.ssh/id*.pub 文件。可用 **-i** 指定其他密钥。

# CAVEATS

初次复制时远程主机必须启用密码认证。安装完成后，你可能需要在 sshd_config 中禁用密码认证。该脚本只是围绕 ssh 的 shell 封装，因此所有 ssh 选项都适用。

# HISTORY

ssh-copy-id 是 **OpenSSH** 附带的便利脚本，用于简化公钥安装过程。它把原本需要手动复制密钥并正确设置权限的流程自动化了。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-client-common```

```brew: brew install ssh-copy-id```

```nix: nix profile install nixpkgs#ssh-copy-id```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1), [ssh-add](/man/ssh-add)(1), [sshd](/man/sshd)(8)

# RESOURCES

```[Source code](https://github.com/openssh/openssh-portable)```

```[Homepage](https://www.openssh.com/)```

<!-- verified: 2026-06-10 -->
