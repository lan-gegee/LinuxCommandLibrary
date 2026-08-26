# TAGLINE

用于 SSH 密钥管理的 Krypton CLI

# TLDR

**与手机配对**

```kr pair```

**显示已配对的设备**

```kr devices```

**生成 SSH 密钥**

```kr generate --email [email@example.com]```

**将公钥添加到服务器**

```kr add [user@host]```

**解除配对**

```kr unpair```

# SYNOPSIS

**kr** _command_ [_options_]

# PARAMETERS

**pair**
> 与 Krypton 手机应用配对。

**devices**
> 列出已配对的设备。

**generate**
> 在手机上生成 SSH 密钥。

**add** _HOST_
> 向主机添加密钥。

**unpair**
> 移除设备配对。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kr** 是 Krypton 的命令行界面。Krypton 是一套将 SSH 和 GPG 私钥存储在配对手机上而非电脑上的系统。通过把私钥保存在单独的设备上，Krypton 为 SSH 连接提供了一种双因素认证：每次登录尝试都会在手机上触发推送通知，必须批准后连接才能继续。

该 CLI 负责与 Krypton 移动应用配对、在手机上生成密钥，以及将对应的公钥复制到远程服务器。配置完成后，kr 会透明地集成本地 SSH agent，标准的 ssh 命令无需修改即可使用。Krypton 项目已被弃用，但该 CLI 及其架构影响了后来基于硬件的 SSH 密钥管理方案。

# CAVEATS

需要 Krypton 应用。认证时需要手机。项目已弃用。

# HISTORY

kr 是 **Krypton**（现已弃用）的 CLI，该工具将 SSH 和 GPG 密钥存储在智能手机上以实现双因素认证。

# INSTALL

```aur: yay -S kr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1), [gpg](/man/gpg)(1)
