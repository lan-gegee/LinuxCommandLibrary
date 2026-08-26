# TAGLINE

为 Dropbear 生成 SSH 密钥

# TLDR

生成 **ed25519** 密钥

```dropbearkey -t ed25519 -f [path/to/key_file]```

生成 **ECDSA** 密钥

```dropbearkey -t ecdsa -f [path/to/key_file]```

生成 4096 位的 **RSA** 密钥

```dropbearkey -t rsa -s 4096 -f [path/to/key_file]```

打印**指纹和公钥**

```dropbearkey -y -f [path/to/key_file]```

# SYNOPSIS

**dropbearkey** [_options_]

# DESCRIPTION

**dropbearkey** 以 Dropbear 原生格式生成 SSH 主机密钥和用户密钥。Dropbear 是一款轻量级 SSH 实现，常用于嵌入式系统、路由器和资源受限设备——这些场合 OpenSSH 会显得过于庞大。

该工具支持现代密钥类型，包括 Ed25519、ECDSA 以及可配置密钥长度的 RSA。生成的密钥以 Dropbear 自有格式存储，与 OpenSSH 的格式不同。如果需要让密钥在 OpenSSH 中使用（或反过来），请使用 dropbearconvert 在两种格式间转换。

主机密钥通常存放在 /etc/dropbear/ 下，用户密钥则可放在标准 SSH 位置。

# PARAMETERS

**-t** _type_
> 密钥类型：**rsa**、**ecdsa**、**ed25519** 或 **dss**。

**-f** _file_
> 写入私钥的目标文件。

**-s** _bits_
> 密钥长度（位），应为 8 的倍数。适用于 RSA 和 ECDSA；Ed25519 长度固定，会忽略此选项。

**-y**
> 打印已有私钥对应的公钥和指纹，而不是生成新密钥。

# CAVEATS

生成的文件采用 **Dropbear 自有的私钥格式**而非 OpenSSH 格式，因此不能直接交给 `ssh -i` 使用：必须先用 `dropbearconvert` 转换。而 **-y** 打印出的*公*钥是常见的 OpenSSH 单行形式，可直接粘贴进 `authorized_keys` 文件。

与 `ssh-keygen` 不同，dropbearkey **不会**用口令加密私钥，也没有提供这样做的选项。任何能读到该文件的人就拿到了密钥。对于重要的用户密钥，应先用 `ssh-keygen` 生成再转换，而不是反过来。

优先选择 **ed25519**：它体积小、速度快且支持良好。**dss** 已经过时，会被现代 SSH 实现拒绝，新密钥绝不应选用。

在缓慢的嵌入式设备上生成 RSA 密钥可能耗时惊人；而且刚启动的系统熵池可能尚未播种，首次开机时的主机密钥生成正是既拖慢启动又产生弱密钥的经典来源。

# INSTALL

```apt: sudo apt install dropbear-bin```

```dnf: sudo dnf install dropbear```

```pacman: sudo pacman -S dropbear```

```apk: sudo apk add dropbear```

```brew: brew install dropbear```

```nix: nix profile install nixpkgs#dropbear```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dropbearconvert](/man/dropbearconvert)(1), [dropbear](/man/dropbear)(8), [dbclient](/man/dbclient)(1), [ssh-keygen](/man/ssh-keygen)(1)

# RESOURCES

```[Source code](https://github.com/mkj/dropbear)```

```[Homepage](https://matt.ucc.asn.au/dropbear/dropbear.html)```

<!-- verified: 2026-07-14 -->
