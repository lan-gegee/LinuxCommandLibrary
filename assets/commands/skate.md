# TAGLINE

个人命令行键值存储

# TLDR

**设置一个值**

```skate set [key] [value]```

**获取一个值**

```skate get [key]```

**列出所有键**

```skate list```

**删除一个键**

```skate delete [key]```

**从 stdin 设置值**

```echo "[value]" | skate set [key]```

**使用指定数据库**

```skate set [key] [value] -d [mydb]```

**同步到 GitHub**

```skate sync```

**链接到 GitHub gist**

```skate link [gist_url]```

# SYNOPSIS

**skate** _command_ [_-d database_] [_options_] [_args_]

# PARAMETERS

**set** _KEY_ _VALUE_
> 存储值。

**get** _KEY_
> 读取值。

**list**
> 列出所有键。

**delete** _KEY_
> 删除键。

**sync**
> 与远程同步。

**link** _URL_
> 链接到 gist。

**-d**, **--database** _NAME_
> 数据库名称。

**--help**
> 显示帮助。

# DESCRIPTION

**skate** 是一个个人键值存储工具，可以直接从命令行进行简单、快速的存储。它可存储任意文本数据，如 API 密钥、笔记、代码片段和配置值，并通过命名键来访问。

数据可以使用 **-d** 标志组织到多个命名数据库中。**sync** 命令将数据备份到 GitHub Gist，从而实现跨机器共享。值既可以通过命令参数设置，也可以从 stdin 管道传入，便于直接存储命令输出。

# CAVEATS

数据默认存储在本地。Gist 同步需要 GitHub 身份验证。不适合存储敏感机密。

# HISTORY

**Skate** 是 **Charm** 工具的一部分，由 Charm 创建，致力于打造精美的终端体验。它提供简单优雅的键值存储。

# INSTALL

```pacman: sudo pacman -S skate```

```apk: sudo apk add skate```

```brew: brew install skate```

```nix: nix profile install nixpkgs#skate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [secret-tool](/man/secret-tool)(1)
