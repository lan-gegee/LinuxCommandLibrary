# TAGLINE

Jujutsu 版本控制系统的 TUI

# TLDR

在当前仓库中**启动 TUI**

```lazyjj```

**打开指定的仓库**

```lazyjj -p [path/to/repo]```

# SYNOPSIS

**lazyjj** [_options_]

# DESCRIPTION

**lazyjj** 是 Jujutsu（jj）版本控制系统的 TUI。它通过 Log、Files 和 Bookmarks 三个主要面板，交互式地展示仓库历史、工作区文件和书签。

该界面支持创建、编辑、压缩（squash）、放弃、拉取、推送、描述以及为变更添加书签等操作。Log 标签页在显示 revset 列表的同时，还提供一个用于查看 color-word 格式和 git 格式差异的面板。它作为一个前端运作：调用 **jj** CLI 并渲染仓库状态。

# CAVEATS

需要 **jj** 0.33.0 或更高版本，以兼容输出解析所用到的模板语言特性。

# HISTORY

**lazyjj** 由 **Cretezy** 创建，使用 **Rust** 编写，基于 ratatui 库。

# INSTALL

```pacman: sudo pacman -S lazyjj```

```brew: brew install lazyjj```

```nix: nix profile install nixpkgs#lazyjj```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [lazygit](/man/lazygit)(1)
