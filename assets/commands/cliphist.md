# TAGLINE

Wayland 剪贴板历史管理器

# TLDR

**列出**剪贴板历史条目

```cliphist list```

使用 fzf**选择**并复制以前的条目

```cliphist list | fzf | cliphist decode | wl-copy```

**删除所有**存储的剪贴板条目

```cliphist wipe```

按 ID **删除**特定剪贴板条目

```cliphist delete [id]```

手动**保存**当前剪贴板内容

```wl-paste | cliphist store```

# SYNOPSIS

**cliphist** _command_ [_arguments_]

# DESCRIPTION

**cliphist** 是一款面向 Wayland 合成器的剪贴板历史管理器。它存储剪贴板条目并允许取回之前的项目，同时支持文本和图像内容。它与 wl-clipboard 软件包中的 **wl-copy** 和 **wl-paste** 配合工作。

要在复制时自动捕获剪贴板条目，请将 `wl-paste --watch cliphist store` 作为后台进程运行，通常写在合成器的启动配置中。之后可以使用 **fzf**、**dmenu** 或 **wofi** 等工具浏览和选择条目，快速找回之前复制的内容。

# PARAMETERS

**list**
> 列出所有存储的剪贴板条目

**store**
> 存储 stdin 传入的内容

**decode**
> 解码某个条目以便粘贴

**delete** _id_
> 删除特定条目

**wipe**
> 删除所有条目

# CAVEATS

仅支持 Wayland，不适用于 X11。需要 wl-clipboard（wl-copy、wl-paste）。历史记录默认存储在内存中。支持图像，但可能消耗大量内存。

# INSTALL

```apt: sudo apt install cliphist```

```dnf: sudo dnf install cliphist```

```pacman: sudo pacman -S cliphist```

```zypper: sudo zypper install cliphist```

```nix: nix profile install nixpkgs#cliphist```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wl-copy](/man/wl-copy)(1), [wl-paste](/man/wl-paste)(1), [xclip](/man/xclip)(1)

# RESOURCES

```[Source code](https://github.com/sentriz/cliphist)```

<!-- verified: 2026-06-22 -->
