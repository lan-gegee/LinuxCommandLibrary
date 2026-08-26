# TAGLINE

初始化新的 yadm dotfiles 仓库

# TLDR

**初始化**一个新的 yadm 仓库

```yadm init```

**强制重新初始化**已有仓库

```yadm init -f```

**以自定义工作树路径初始化**

```yadm init -w [path/to/worktree]```

# SYNOPSIS

**yadm** **init** [**-f**] [**-w** _dir_]

# PARAMETERS

**-f**
> 强制重新初始化已有仓库。

**-w** _dir_
> 用指定目录覆盖默认工作树（$HOME）。

# DESCRIPTION

**yadm init** 创建一个用于跟踪 dotfiles 的全新空仓库。该仓库初始化于 **$HOME/.local/share/yadm/repo.git**，并以 **$HOME** 作为默认工作树。这是使用 yadm 开始管理 dotfiles 的第一步。

如果仓库已经存在，则需要 **-f** 标志来强制重新初始化。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-clone](/man/yadm-clone)(1), [yadm-config](/man/yadm-config)(1), [yadm-encrypt](/man/yadm-encrypt)(1)
