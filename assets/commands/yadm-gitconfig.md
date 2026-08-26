# TAGLINE

管理 yadm 仓库的 git 配置

# TLDR

**查看 yadm git 配置**

```yadm gitconfig --list```

**设置 yadm git 配置**

```yadm gitconfig [setting] [value]```

# SYNOPSIS

**yadm** **gitconfig** [_options_] [_name_] [_value_]

# DESCRIPTION

**yadm gitconfig** 管理 yadm 仓库的 git 配置。它与系统的 git 配置相互独立，专门为 yadm 仓库设置用户、远程及其他 git 设置。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-config](/man/yadm-config)(1), [git-config](/man/git-config)(1)
