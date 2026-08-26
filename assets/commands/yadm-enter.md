# TAGLINE

在设置了 yadm Git 变量的子 Shell 中运行命令

# TLDR

**进入设置了 yadm Git 变量的子 Shell**

```yadm enter```

**在 yadm 上下文中运行特定命令**

```yadm enter [command]```

**在 yadm 工作树中运行 git log**

```yadm enter git log --oneline```

# SYNOPSIS

**yadm** **enter** [_command_]

# DESCRIPTION

**yadm enter** 会打开一个子 Shell，其中 **GIT_DIR** 和 **GIT_WORK_TREE** 环境变量已设置为 yadm 仓库。退出该子 Shell 的方式与退出普通 Shell 相同（通常是 "exit"）。这对于对 dotfiles 执行复杂的 git 操作很有用，也便于与直接使用 Git 的工具集成，例如 **tig**、**vim-fugitive** 或 **git-cola**。

也可以在 "enter" 之后提供一个命令，该命令将在其环境中带有 yadm Git 变量的情况下运行，而不是启动子 Shell。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1)
