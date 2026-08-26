# TAGLINE

加密云存储与键值数据库

# TLDR

**存储一个键值对**

```charm kv set [key] [value]```

**取回一个值**

```charm kv get [key]```

**列出所有键**

```charm kv list```

**删除一个键**

```charm kv delete [key]```

使用 Charm 密钥**加密**文件

```charm crypt encrypt [path/to/file]```

**解密**用 Charm 密钥加密的文件

```charm crypt decrypt [path/to/file.enc]```

将本地数据**同步**到 Charm Cloud

```charm sync```

**显示**账户身份和已关联的设备

```charm id```

将加密密钥**备份**到文件

```charm backup-keys```

# SYNOPSIS

**charm** _command_ [_options_] [_arguments_]

# PARAMETERS

**kv set** _key_ _value_
> 存储一个键值对。

**kv get** _key_
> 取回键对应的值。

**kv list**
> 列出所有已存储的键。

**kv delete** _key_
> 删除一个键值对。

**crypt encrypt** _file_
> 加密文件。

**crypt decrypt** _file_
> 解密文件。

**sync**
> 与 Charm Cloud 同步。

**id**
> 显示或管理账户身份。

**link**
> 将新设备关联到账户。

**backup-keys**
> 导出加密密钥。

**fs**
> 访问 Charm 文件系统。

**-o**, **--output** _file_
> 操作的输出文件。

# DESCRIPTION

**charm** 是来自 Charmbracelet 的命令行工具，提供端到端加密的云存储、键值数据库和文件加密。它让你无需自建服务器即可在设备间安全地同步数据。

**kv** 命令提供简单的键值存储，适合保存配置、密钥和应用状态。所有数据在同步到 Charm Cloud 之前都会在客户端加密，确保隐私。

通过 **charm crypt** 进行文件加密时，会使用你的 Charm 密钥加密任意文件。**fs** 命令提供存储在云端的一个虚拟文件系统。设备关联让你可以从多台机器访问相同的数据。

# CAVEATS

数据是加密的，但仍需信任 Charm Cloud 基础设施。免费层有存储限制。务必备份密钥——丢失密钥就意味着无法访问数据。可以自托管，但需要更多配置。

# HISTORY

Charm 由 **Charmbracelet** 开发，这是一家成立于 **2020 年**、致力于让命令行更愉悦的公司。他们以 Bubble Tea 和 Lip Gloss 等 TUI 库闻名，并开发了 Charm Cloud 作为需要云同步功能的 CLI 工具的基础设施。该服务的目标是让开发者无需复杂配置即可获得易用的加密云存储。

# INSTALL

```pacman: sudo pacman -S charm```

```brew: brew install charm```

```nix: nix profile install nixpkgs#charm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [age](/man/age)(1), [glow](/man/glow)(1), [gpg](/man/gpg)(1)
