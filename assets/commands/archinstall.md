# TAGLINE

带交互式菜单的 Arch Linux 引导式安装器

# TLDR

启动**交互式安装器**

```archinstall```

运行指定的**安装配置文件**

```archinstall --script [minimal]```

使用**配置文件**运行

```archinstall --config [/path/to/config.json]```

以预定义配置在**静默模式**下运行

```archinstall --config [/path/to/config.json] --silent```

# SYNOPSIS

**archinstall** [_options_]

# DESCRIPTION

**archinstall** 是一个引导式的 Arch Linux 安装器，提供交互式菜单驱动的安装体验。它简化了 Arch Linux 的安装过程，同时保留了灵活性和自定义选项。

# PARAMETERS

**--config** _path_
> 从 JSON 文件加载配置。

**--creds** _path_
> 从文件加载凭据（密码、密钥）。

**--disk-layout** _path_
> 从文件加载磁盘布局配置。

**--script** _name_
> 运行指定的安装配置文件（如 minimal、desktop）。

**--silent**
> 无用户提示运行（需要 --config）。

**--dry-run**
> 测试安装过程而不做任何更改。

# CAVEATS

需要网络连接。只应在 Arch Linux live 安装环境中运行。会创建分区并格式化磁盘；可能造成数据丢失。

# HISTORY

由 **Arch Linux** 社区开发，自 **2021** 年起正式纳入安装 ISO，作为传统手动安装流程的替代方案。

# INSTALL

```pacman: sudo pacman -S archinstall```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pacman](/man/pacman)(8), [arch-chroot](/man/arch-chroot)(8), [pacstrap](/man/pacstrap)(8), [genfstab](/man/genfstab)(8)
