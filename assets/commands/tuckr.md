# TAGLINE

基于符号链接的 dotfile 管理器

# TLDR

**将所有 dotfile 以符号链接部署到位**

```tuckr add \*```

**部署指定分组**

```tuckr add [neovim] [zsh]```

**部署除某些分组外的全部内容**

```tuckr add \* -e [neovim]```

**设置分组并运行其钩子**

```tuckr set [group]```

**移除已部署的 dotfile**

```tuckr rm [group]```

**显示符号链接状态**

```tuckr status```

**将现有文件复制进某个分组**

```tuckr push [group] [file]```

# SYNOPSIS

**tuckr** _command_ [_group_...] [_options_]

# PARAMETERS

**add**（别名 **a**）
> 通过创建符号链接为给定分组部署 dotfile。

**rm**
> 从系统中移除已部署的 dotfile。

**set**
> 设置分组并运行它们的钩子。

**unset**
> 移除分组并运行其清理钩子。

**status**（别名 **s**）
> 显示 dotfile 的符号链接状态。

**push**
> 将现有文件复制进一个分组。

**pop**
> 从 dotfiles 目录中移除分组。

**encrypt**（别名 **e**）
> 加密文件并将其存放在 Secrets 下。

**decrypt**（别名 **d**）
> 解密文件。

**groupis**
> 报告文件属于哪个分组。

**init**
> 初始化 dotfile 目录。

**-e** _GROUP_
> 与 add 一起使用时排除给定分组。

# DESCRIPTION

**tuckr** 是一个 dotfile 管理器，它将配置文件组织成逻辑分组并以符号链接方式部署。每个分组代表一组相关的 dotfile（如 vim、zsh 或 git），可以在不同机器上选择性地部署配置。

add 命令从 dotfile 仓库创建指向家目录中预期位置的符号链接。分组可以单独链接，也可以用 `\*` 通配符一次性全部链接；status 命令显示当前已链接的分组。rm 命令干净地解除已部署的符号链接，而 set 还会运行各分组的设置钩子。

该工具使用简单的目录结构，包含 Configs、Hooks 和 Secrets 目录，Configs 下的每个子目录代表一个分组，并在其中镜像家目录布局。它受 GNU Stow 启发，增加了钩子和加密密钥管理功能，且不要求具备符号链接感知能力的工具。

# CAVEATS

使用 Rust 实现。目录结构有特定要求。基于符号链接。

# HISTORY

**Tuckr** 的创建目标是提供一个使用符号链接、按分组组织的简单 dotfile 管理器。

# INSTALL

```apk: sudo apk add tuckr```

```brew: brew install tuckr```

```nix: nix profile install nixpkgs#tuckr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stow](/man/stow)(1), [chezmoi](/man/chezmoi)(1), [yadm](/man/yadm)(1)
