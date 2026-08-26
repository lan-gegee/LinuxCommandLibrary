# TAGLINE

启动一个提供指定软件包的 Shell

# TLDR

**进入一个可用某软件包的 Shell**

```nix shell nixpkgs#[hello]```

**进入一个可用多个软件包的 Shell**

```nix shell nixpkgs#[git] nixpkgs#[curl]```

**使用某个软件包运行单条命令后退出**

```nix shell nixpkgs#[jq] --command jq --version```

**进入一个可用来自特定 flake 的软件包的 Shell**

```nix shell github:[owner/repo]#[package]```

**进入一个可用来自特定 nixpkgs 版本的软件包的 Shell**

```nix shell github:NixOS/nixpkgs/[nixos-24.05]#[hello]```

# SYNOPSIS

**nix** **shell** [_options_] _installables_

# PARAMETERS

_INSTALLABLES_
> 指定要提供的软件包的 flake 引用（例如 nixpkgs#hello）。

**--command**, **-c** _CMD_ [_ARGS_]
> 在该 Shell 环境中运行命令，而不是启动交互式 Shell。

**--ignore-environment**, **-i**
> 清空整个环境（使用 --keep 指定的除外）。

**--keep** _NAME_
> 使用 --ignore-environment 时保留指定的环境变量。

**--keep-going**
> 若某个构建失败，继续构建其他 derivation。

**--impure**
> 允许访问可变路径和环境变量。

**--override-input** _INPUT_ _FLAKEREF_
> 覆盖特定的 flake 输入。隐含 --no-write-lock-file。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix shell** 启动一个 Shell 环境，使指定的软件包在 `$PATH` 中可用。它是基于 flake 的 `nix-shell -p` 替代品，不需要 shell.nix 或 default.nix 文件。

软件包以 flake 引用的形式指定（例如 `nixpkgs#jq`）。这些软件包会按需构建或拉取，并且仅在生成的 Shell 会话中可用。不会进行任何永久性安装。

# CAVEATS

需要启用实验性的 `nix-command` 和 `flakes` 特性。软件包不会被永久安装；它们仅在生成的 Shell 会话中可用。

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [nix3-develop](/man/nix3-develop)(1), [nix3-run](/man/nix3-run)(1), [nix3-build](/man/nix3-build)(1)
