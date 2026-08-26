# TAGLINE

加密环境变量管理器

# TLDR

**加载 .env 运行命令**

```dotenvx run -- [command]```

**使用指定 env 文件运行**

```dotenvx run -f [.env.production] -- [command]```

**加密 env 文件**

```dotenvx encrypt```

**解密 env 文件**

```dotenvx decrypt```

**设置一个键**

```dotenvx set [KEY] [value]```

**获取一个键**

```dotenvx get [KEY]```

**转换为加密格式**

```dotenvx convert```

# SYNOPSIS

**dotenvx** _command_ [_options_]

# SUBCOMMANDS

**run**
> 加载 env 并运行命令。

**get**
> 获取环境变量。

**set**
> 设置环境变量。

**encrypt**
> 加密 .env 文件。

**decrypt**
> 解密 .env 文件。

**convert**
> 转换为加密格式。

**genexample**
> 生成 .env.example。

# PARAMETERS

**-f**, **--env-file** _file_
> env 文件路径。

**--overload**
> 覆盖已存在的环境变量。

# CONFIGURATION

**.env**
> 默认的环境变量文件，会被自动加载。

**.env.keys**
> 用于解密 .env 文件的加密密钥。

# DESCRIPTION

**dotenvx** 是增强版 dotenv 工具，可从 .env 文件加载环境变量并支持加密。它在传统 dotenv 模式的基础上增加了内置加密能力，使团队能够将加密后的环境文件安全地提交到版本控制。

该工具支持多个环境文件（.env.production、.env.staging）、运行时自动解密，以及面向团队密钥共享的密钥管理。它提供了一种无需外部密钥管理服务即可管理应用机密的现代方案。

# INSTALL

```nix: nix profile install nixpkgs#dotenvx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[env](/man/env)(1), [direnv](/man/direnv)(1), [sops](/man/sops)(1)
