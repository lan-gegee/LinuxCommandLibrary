# TAGLINE

Nix 助手工具

# TLDR

**构建 NixOS 配置**

```nh os switch```

**构建 home-manager 配置**

```nh home switch```

**使用 flake 构建**

```nh os switch --flake [.]```

**试运行构建**

```nh os switch --dry```

**清理旧世代**

```nh clean all```

**搜索软件包**

```nh search [package]```

# SYNOPSIS

**nh** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> nh 子命令。

**os** _ACTION_
> NixOS 相关操作。

**home** _ACTION_
> home-manager 相关操作。

**clean** _TARGET_
> 清理世代。

**search** _QUERY_
> 搜索软件包。

**--flake** _PATH_
> 使用指定路径处的 flake。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nh** 是一款 Nix 助手工具，用于简化 NixOS 和 home-manager 的操作。

该工具封装了常用的 Nix 命令，提供更好的输出与交互体验。

# CAVEATS

需要 Nix/NixOS 环境。基于 Rust 编写。是对 nixos-rebuild 的封装。

# HISTORY

nh 的诞生是为了给常见的 NixOS 和 home-manager 操作提供一个**更好的界面**。

# INSTALL

```nix: nix profile install nixpkgs#nh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nixos-rebuild](/man/nixos-rebuild)(1), [home-manager](/man/home-manager)(1)
