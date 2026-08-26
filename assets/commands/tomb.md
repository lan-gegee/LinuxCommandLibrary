# TAGLINE

加密存储卷管理器

# TLDR

**创建**新的 tomb（100 MB）

```tomb dig -s 100 secret.tomb```

**锻造**新密钥文件

```tomb forge secret.tomb.key```

**用密钥锁定** tomb

```tomb lock secret.tomb -k secret.tomb.key```

**打开**并挂载 tomb

```tomb open secret.tomb -k secret.tomb.key```

**关闭** tomb

```tomb close secret.tomb```

**强制**关闭所有 tomb

```tomb slam all```

**列出**所有已打开的 tomb

```tomb list```

**调整** tomb 大小

```tomb resize secret.tomb -s 200```

# SYNOPSIS

**tomb** [_options_] _command_ [_arguments_]

# DESCRIPTION

**tomb** 管理可安全传输并隐藏在文件系统中的加密存储目录。它创建 LUKS 加密容器，可以像普通目录一样挂载。Tomb 适合安全存储敏感数据。

# PARAMETERS

**dig**
> 创建新的 tomb 容器

**forge**
> 创建用于锁定 tomb 的新密钥文件

**lock**
> 用密钥初始化并锁定空的 tomb

**open**
> 使用密钥文件挂载 tomb

**close**
> 卸载 tomb

**slam**
> 强制关闭 tomb，终止占用它们的进程

**list**
> 列出所有已打开的 tomb

**resize**
> 更改 tomb 的大小

**passwd**
> 更改保护密钥文件的口令

**setkey**
> 将现有 tomb 的密钥替换为另一个

**bury**
> 将密钥文件隐藏在 JPEG 图像中（隐写术）

**exhume**
> 恢复先前埋入图像中的密钥文件

**engrave**
> 将密钥打印为二维码以便纸质备份

**index**, **search**, **recompose**
> 维护和查询 tomb 的 recoll 全文索引

**-s SIZE**
> 以 MB 为单位指定大小

**-k KEYFILE**
> 指定要使用的密钥文件

**-f, --force**
> 强制执行操作（例如无视 swap 存在而锻造密钥）

**-o MOUNT_OPTIONS**
> 指定挂载选项

**--kdf** _N_
> 使用带 _N_ 轮密钥派生的强 KDF（增强抗暴力破解能力）。

**--tomb-pwd** _FD_
> 从文件描述符 _FD_ 读取口令（用于自动化）。

**-g, --gpg-key** _KEYID_
> 使用 GPG 公钥而不是口令加密 tomb 密钥。

# CAVEATS

如果启用了 swap，tomb 会拒绝锻造密钥（防止密钥材料被写入 swap）。使用 -f 可绕过此检查。Tomb 基于 LUKS 实现，需要 cryptsetup。

# HISTORY

**tomb** 由 Dyne.org 基金会创建，是一个以可移植方式创建和管理 LUKS 加密卷的易用包装器。

# INSTALL

```apt: sudo apt install tomb```

```nix: nix profile install nixpkgs#tomb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [gpg](/man/gpg)(1), [dm-crypt](/man/dm-crypt)(8)
