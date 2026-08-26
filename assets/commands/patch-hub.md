# TAGLINE

浏览并应用内核邮件列表补丁的 TUI

# TLDR

**启动补丁浏览器**

```patch-hub```

**启动时指定邮件列表**

```patch-hub --mailing-list [linux-kernel]```

# SYNOPSIS

**patch-hub** [_options_]

# PARAMETERS

**--mailing-list** _list_
> 指定启动时要浏览的邮件列表。

**--page-size** _N_
> 每页显示的补丁数量。

# DESCRIPTION

**patch-hub** 是一个终端用户界面，用于简化 Linux 相关开发中通过邮件列表提交的软件补丁处理工作。它连接 lore.kernel.org 来浏览邮件列表、查看包含作者、标题、版本和评审标签等元数据的补丁集、将补丁应用到本地内核树、收藏补丁集以及回复 Reviewed-by 标记。

# CAVEATS

应用和回复补丁需要安装 **b4** 和 **git send-email**。借助 bat、delta 或 diff-so-fancy 等可选工具可获得更好的补丁渲染效果。

# HISTORY

**patch-hub** 由 **kworkflow** 组织创建，使用 **Rust** 编写。

# INSTALL

```apt: sudo apt install patch```

```dnf: sudo dnf install patch```

```pacman: sudo pacman -S patch```

```apk: sudo apk add patch```

```zypper: sudo zypper install patch```

```nix: nix profile install nixpkgs#patch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-send-email](/man/git-send-email)(1), [mutt](/man/mutt)(1), [patch](/man/patch)(1)
