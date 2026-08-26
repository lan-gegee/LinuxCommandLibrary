# TAGLINE

已废弃的 APT 密钥管理工具，用于软件包认证

# TLDR

**列出**受信任的密钥

```apt-key list```

向受信任的密钥库**添加**密钥

```apt-key add [public_key_file.asc]```

从受信任的密钥库**删除**密钥

```apt-key del [key_id]```

将**远程密钥**添加到受信任的密钥库

```wget -qO - [https://host.tld/filename.key] | apt-key add -```

仅凭密钥 ID 从 **keyserver** 添加密钥

```apt-key adv --keyserver pgp.mit.edu --recv [KEYID]```

**导出**所有受信任的密钥

```apt-key exportall```

**现代替代方案**：直接将密钥下载到 trusted.gpg.d（无需 apt-key）

```curl -fsSL [https://example.com/key.gpg] | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/[example].gpg```

**现代替代方案**：在 sources.list 中使用 signed-by

```echo "deb [signed-by=/usr/share/keyrings/[example].gpg] [https://repo.example.com] [stable] main" | sudo tee /etc/apt/sources.list.d/[example].list```

# SYNOPSIS

**apt-key** [_command_] [_arguments_]

# DESCRIPTION

**apt-key** 是 Debian 和 Ubuntu 上 APT 软件包管理器的一个已废弃的密钥管理工具。它管理 apt 用于认证软件包的密钥列表。

**注意：** apt-key 自 Debian 11（Bullseye）和 Ubuntu 22.04（Jammy）起已被废弃。推荐的做法是将密钥环文件直接放在 /etc/apt/trusted.gpg.d/（使用 .gpg 或 .asc 扩展名），或放在 /usr/share/keyrings/ 中，并通过 sources.list 条目中的 `signed-by` 选项引用它们。只有 `apt-key del` 仍受支持，可用于维护者脚本。

# PARAMETERS

**list**
> 列出所有受信任的密钥及其指纹

**add file**
> 向受信任密钥列表添加新密钥

**del keyid**
> 从受信任密钥列表移除密钥

**adv**
> 向 gpg 传递高级选项

**update**
> 使用归档密钥环更新本地密钥环

**net-update**
> 更新本地密钥环，从 keyserver 获取缺失的密钥

**export keyid**
> 将密钥输出到标准输出

**exportall**
> 将所有受信任的密钥输出到标准输出

**finger**
> 列出受信任密钥的指纹（已废弃）

**--keyring** _filename_
> 操作特定的密钥环文件（已废弃）

# CONFIGURATION

**/etc/apt/trusted.gpg.d/**
> 存放 GPG 格式受信任密钥环文件的目录。

**/usr/share/keyrings/**
> 系统级密钥环，通过 sources.list 中的 signed-by 引用。

# CAVEATS

**已废弃**：应改为将密钥环文件直接放入 /etc/apt/trusted.gpg.d/ 或在 apt 源中使用 signed-by。维护者脚本中只应使用 apt-key del。

# HISTORY

属于 **APT**（Advanced Package Tool）工具套件。自 Debian 11 和 Ubuntu 22.04 起被废弃，由 trusted.gpg.d 目录取代。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [gpg](/man/gpg)(1), [apt-secure](/man/apt-secure)(8)
