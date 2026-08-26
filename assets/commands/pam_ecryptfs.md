# TAGLINE

处理 eCryptfs 加密的家目录

# TLDR

**自动挂载加密家目录**

```auth optional pam_ecryptfs.so unwrap```

**会话建立**

```session optional pam_ecryptfs.so unwrap```

**密码同步**

```password optional pam_ecryptfs.so```

# SYNOPSIS

**pam_ecryptfs.so** [_options_]

# PARAMETERS

**unwrap**
> 使用用户的登录密码解密存储在 `~/.ecryptfs/wrapped-passphrase` 中的已封装挂载密码（mount passphrase），并将其加入内核密钥环。

# DESCRIPTION

**pam_ecryptfs** 是让基于用户的 eCryptfs 加密家目录在登录时透明化的 PAM 胶水模块：当它被放入 `auth` 和 `session` 栈时，会将用户的挂载密码插入内核密钥环（通常是用登录密码解封 `~/.ecryptfs/wrapped-passphrase`），然后调用辅助程序把 `~/.Private`（或整个家目录）挂载到 `~` 上。注销时，session 步骤会卸载并清除密钥。

它是 **ecryptfs-utils** 套件（`ecryptfs-setup-private`、`ecryptfs-mount-private`）在内核侧的对应组件。

# CAVEATS

需要事先用 **ecryptfs-setup-private** 设置好 eCryptfs。只有当 `password` PAM 栈同样调用 `pam_ecryptfs.so` 时，登录密码更改才会同步重新加密 wrapped-passphrase 文件——否则密码更改会悄悄失去同步，用户将无法再挂载家目录。自 Ubuntu 18.04 起，eCryptfs 已不再是默认选项，取而代之的是全盘加密（LUKS）。

# HISTORY

pam_ecryptfs 实现了登录时**自动挂载加密家目录**。

# SEE ALSO

[ecryptfs](/man/ecryptfs)(7), [ecryptfs-setup-private](/man/ecryptfs-setup-private)(1), [pam](/man/pam)(8)
