# TAGLINE

Unix 系统中的隐藏配置文件

# TLDR

**显示当前目录的隐藏文件**

```ls -a```

**只列出 dotfiles**

```ls -d .[!.]*```

**递归查找所有 dotfiles**

```find . -name ".*" -type f```

**复制 dotfiles 进行备份**

```cp ~/.[!.]* [backup_dir/]```

**用 rsync 同步 dotfiles**

```rsync -av ~/.[!.]* [remote:~/]```

# DESCRIPTION

**Dotfiles** 是类 Unix 系统中以点号（.）开头、默认隐藏的配置文件。它们存储各种应用程序和 shell 的用户偏好与设置。

常见的 dotfiles 包括 **.bashrc**（Bash 配置）、**.vimrc**（Vim 设置）、**.gitconfig**（Git 设置）和 **.ssh/**（SSH 密钥与配置）。管理 dotfiles 通常涉及版本控制和符号链接策略。

# COMMON DOTFILES

```
~/.bashrc          # Bash configuration
~/.bash_profile    # Bash login shell
~/.zshrc           # Zsh configuration
~/.vimrc           # Vim settings
~/.gitconfig       # Git configuration
~/.ssh/config      # SSH settings
~/.tmux.conf       # Tmux configuration
~/.config/         # XDG config directory
```

# MANAGEMENT STRATEGIES

**Git bare 仓库**：通过 bare 仓库和 work tree 别名用 git 跟踪 dotfiles。

**符号链接管理器**：stow、dotbot 或 chezmoi 等工具从中央仓库创建符号链接。

**版本控制**：把 dotfiles 保存在 git 仓库中，以获得历史记录并跨机器同步。

# CAVEATS

Dotfiles 常常包含机密信息：`~/.netrc` 或 `~/.aws/credentials` 里的 API 令牌、`~/.ssh/` 里的私钥，以及 `~/.bash_history` 里的 shell 历史。在把 dotfiles 仓库推送到公共托管平台前务必仔细检查；最好从一开始就把机密完全放在仓库之外，而不是指望事后清理，因为 git 历史会保留你删掉的东西。

"隐藏"只是 `ls` 和文件管理器遵循的显示约定，并非一种权限：任何能读取你主目录的程序都能读取它们。许多程序还会自动生成 dotfiles 和点目录，其中包括绝不应纳入版本控制的缓存和状态数据。**XDG Base Directory** 规范正是为了遏制这种混乱而生：把配置移到 `~/.config/`、缓存移到 `~/.cache/`、状态移到 `~/.local/state/`，但各程序的落实程度参差不齐，典型的主目录仍然是两种约定并存。

# HISTORY

隐藏的 dotfiles 是一个著名的意外产物。早期 Unix 的目录中包含 `.` 和 `..` 两个条目，为了让它们不出现在列表里，有人给 `ls` 加了一个测试：跳过任何以点开头的名字——而不是本可以精确跳过那两个条目的两行判断。由此产生的副作用，即*任何*以 `.` 开头的文件都从列表中消失，从来不是有意设计；只是有人注意到了这个现象，然后加以利用。**Rob Pike** 曾把这个故事当作警世寓言讲述：某个程序里走捷径的做法，最终演变成一个所有后续程序都必须知晓的约定，而如今它让主目录里散落着数百个条目。

把 dotfiles 当作受版本控制的可迁移资产来对待则要晚得多，它与 Git 的普及以及工程师跨多台机器工作的趋势相伴而来。让 `~` 本身充当工作树的 **bare 仓库**技巧，以及 **GNU Stow**、**dotbot**、**chezmoi** 和 **yadm** 等符号链接管理器，都是对同一个问题的回应：配置需要多年积累，却只需几分钟就会丢失。

# INSTALL

```nix: nix profile install nixpkgs#dotfiles```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stow](/man/stow)(1), [dotbot](/man/dotbot)(1), [chezmoi](/man/chezmoi)(1), [yadm](/man/yadm)(1), [ls](/man/ls)(1), [git](/man/git)(1)
