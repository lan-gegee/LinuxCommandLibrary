# TAGLINE

卸载 opencode

# TLDR

**卸载 opencode 并删除所有相关文件**

```opencode uninstall```

**预览将被删除的内容而不做任何更改**

```opencode uninstall --dry-run```

**卸载但保留配置文件**

```opencode uninstall --keep-config```

**卸载但保留会话数据和快照**

```opencode uninstall --keep-data```

**跳过确认提示**

```opencode uninstall --force```

# SYNOPSIS

**opencode uninstall** [_options_]

# PARAMETERS

**-c**, **--keep-config**
> 保留配置文件。默认：false。

**-d**, **--keep-data**
> 保留会话数据和快照。默认：false。

**--dry-run**
> 显示将被删除的内容但不实际删除。默认：false。

**-f**, **--force**
> 跳过确认提示。默认：false。

**--print-logs**
> 将日志打印到 stderr。

**--log-level** _LEVEL_
> 日志级别：`DEBUG`、`INFO`、`WARN` 或 `ERROR`。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本号。

# DESCRIPTION

**opencode uninstall** 会删除 opencode 二进制文件，并且默认从当前系统删除其配套文件：配置、缓存数据与会话历史。`--keep-config` 和 `--keep-data` 标志可保留特定类别的文件，在重新安装或切换渠道时很有用。

先使用 `--dry-run` 审计将要删除的具体路径，再执行真正的卸载。

# CAVEATS

在不加 `--keep-config` 或 `--keep-data` 的情况下，此操作**不可逆**：本地会话数据、配置和缓存的凭据将被永久删除。如果 opencode 是通过软件包管理器（如 Homebrew）安装的，请改用该管理器卸载。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-upgrade](/man/opencode-upgrade)(1), [opencode-models](/man/opencode-models)(1)
