# TAGLINE

管理 Nix channel 订阅

# TLDR

**列出已订阅的 channel**

```nix-channel --list```

**添加 channel**

```nix-channel --add [https://nixos.org/channels/nixpkgs-unstable] [nixpkgs]```

**更新所有 channel**

```nix-channel --update```

**更新指定 channel**

```nix-channel --update [nixpkgs]```

**移除 channel**

```nix-channel --remove [nixpkgs]```

**回滚到上一个 channel 世代**

```nix-channel --rollback```

**列出 channel 世代**

```nix-channel --list-generations```

# SYNOPSIS

**nix-channel** [_options_]

# PARAMETERS

**--list**
> 打印所有已订阅 channel 的名称和 URL。

**--add** _URL_ [_NAME_]
> 订阅一个 channel。如果省略 _NAME_，则默认取 URL 的最后一个组成部分，并去掉 -stable 或 -unstable 后缀。

**--update** [_NAMES..._]
> 下载已订阅 channel 的 Nix 表达式，并把它们设为 nix-env 操作的默认来源。也可以只更新指定名称的 channel。

**--remove** _NAME_
> 取消订阅某个 channel。

**--rollback** [_GENERATION_]
> 撤销上一次 `--update` 调用。可选地指定世代编号。

**--list-generations**
> 显示 channel 世代列表。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**nix-channel** 管理 Nix channel 的订阅。channel 是指向某个 Nix 表达式 tarball 的 URL，其中提供了一组软件包和 NixOS 模块。

已订阅 channel 的列表存储在 `~/.nix-channels` 中。更新之后，channel 表达式会以符号链接的形式出现在 `~/.nix-defexpr/` 下，从而可供 `nix-env` 和其他 Nix 工具使用。Nix flake 是 channel 的现代化替代方案。

# CAVEATS

Channel 属于旧有机制；新项目建议使用 Nix flake。除非在 NixOS 上进行了系统级配置，channel 都是按用户独立维护的。运行 `--update` 需要网络连接来下载 channel 表达式。

# HISTORY

自 Eelco Dolstra 发布早期版本以来，nix-channel 就一直是 **Nix** 软件包管理器的一部分。它是订阅软件仓库的传统机制，早于 Nix 2.4 中以实验形式引入的 flakes 系统。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-env](/man/nix-env)(1), [nix-build](/man/nix-build)(1), [nix-shell](/man/nix-shell)(1), [nixos-rebuild](/man/nixos-rebuild)(1)
