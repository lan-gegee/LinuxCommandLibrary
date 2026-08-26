# TAGLINE

在 Linux 上管理 BetterDiscord 安装

# TLDR

在 **Discord Stable** 上**安装** BetterDiscord

```sudo betterdiscordctl install```

在 **Discord Canary** 上安装 BetterDiscord

```sudo betterdiscordctl -f canary install```

在 **Discord PTB** 上安装 BetterDiscord

```sudo betterdiscordctl -f ptb install```

在以 **Flatpak** 方式安装的 Discord 上安装 BetterDiscord

```sudo betterdiscordctl -i flatpak install```

在以 **Snap** 方式安装的 Discord 上安装 BetterDiscord

```sudo betterdiscordctl -i snap install```

# SYNOPSIS

**betterdiscordctl** [_options_] _command_

# DESCRIPTION

**betterdiscordctl** 在 Linux 系统上管理 BetterDiscord 的安装。BetterDiscord 是 Discord 的客户端修改工具，可启用主题、插件和额外的自定义功能。

该工具可在不同 Discord 变体（Stable、Canary、PTB）和不同安装方式（原生、Flatpak、Snap）之间处理 BetterDiscord 的安装、更新与卸载。

# SUBCOMMANDS

**install**
> 安装 BetterDiscord。

**reinstall**
> 重新安装 BetterDiscord，并移除旧文件。

**uninstall**
> 卸载 BetterDiscord。

**update**
> 更新 BetterDiscord，如本地仓库存在则一并更新。

**status**
> 显示当前 Discord 补丁状态。

**self-upgrade**
> 升级 betterdiscordctl 自身。

# PARAMETERS

**-f**, **--d-flavors** _flavor_
> 指定 Discord 版本：stable、canary 或 ptb。

**-i**, **--d-install** _method_
> 指定安装方式：system、flatpak 或 snap。

**-p**, **--d-appdir** _path_
> 指定自定义的 Discord 应用目录。

**-v**, **--verbose**
> 提高输出详细程度。

**-q**, **--quiet**
> 降低输出详细程度。

**-V**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助信息并退出。

# CAVEATS

需要 root 权限。Discord 更新后 BetterDiscord 可能失效；通常需要重新安装。使用客户端修改可能违反 Discord 的服务条款。

# INSTALL

```aur: yay -S betterdiscordctl```

```nix: nix profile install nixpkgs#betterdiscordctl```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[discord](/man/discord)(1), [flatpak](/man/flatpak)(1), [snap](/man/snap)(1)
