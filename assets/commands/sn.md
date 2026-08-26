# TAGLINE

.NET 强名称密钥管理工具

# TLDR

**创建密钥对**

```sn -k [keypair.snk]```

**提取公钥**

```sn -p [keypair.snk] [public.snk]```

**显示令牌**

```sn -t [assembly.dll]```

**显示公钥**

```sn -tp [keypair.snk]```

**验证签名**

```sn -v [assembly.dll]```

# SYNOPSIS

**sn** [_-k file_] [_-p input output_] [_-t file_] [_options_]

# PARAMETERS

**-k** _FILE_
> 生成密钥对。

**-p** _IN OUT_
> 提取公钥。

**-t** _FILE_
> 显示令牌。

**-tp** _FILE_
> 显示公钥。

**-v** _FILE_
> 验证程序集。

**-R** _FILE KEY_
> 重新签署程序集。

# DESCRIPTION

**sn**（强名称工具）用于创建和管理用于签署 .NET 程序集的加密密钥对。强名称通过组合程序集的名称、版本号、区域性信息和公钥为其赋予唯一标识，避免同名简单名的程序集之间发生冲突。

该工具可以生成用于签名的 RSA 密钥对，提取公钥以便分发而不暴露私钥，并显示公钥令牌（用作紧凑标识符的短哈希）。它还可以验证程序集的强名称签名是否有效，并使用不同的密钥对重新签署程序集。

强名称是 .NET Framework 和 Mono 运行时的一部分。虽然仍受支持，但 Microsoft 现在建议在大多数场景中使用 NuGet 包签名；强名称主要用于遗留兼容性和全局程序集缓存（GAC）注册。

# CAVEATS

.NET 专属。Windows 工具，经 Mono 提供。强名称已被弃用。

# HISTORY

**sn**（强名称工具）是 **.NET SDK** 的一部分，用于创建和管理用于程序集签名的加密密钥。

# INSTALL

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mono](/man/mono)(1), [gacutil](/man/gacutil)(1), [mcs](/man/mcs)(1)
