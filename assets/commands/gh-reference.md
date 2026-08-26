# TAGLINE

显示所有 GitHub CLI 命令的 Markdown 参考

# TLDR

**显示完整的命令参考**

```gh reference```

**将参考内容管道传给分页器**以便阅读

```gh reference | less```

# SYNOPSIS

**gh reference**

# DESCRIPTION

**gh reference** 输出一份涵盖所有 GitHub CLI 命令的完整 Markdown 格式参考。它在单个文档中完整列出每一条命令、子命令及其标志。

这份参考有助于发现可用命令，并概览 gh 的整体能力。与逐个查看帮助页面（`gh <command> --help`）不同，它将所有命令集中在一起，更便于探索。

# CAVEATS

输出内容较长；建议通过管道传给 `less` 等分页器查看。本地生成的参考对应已安装的 gh 版本。

# HISTORY

gh reference 被加入 **GitHub CLI**，用于提供全面的命令参考，补充逐命令的帮助系统。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-help](/man/gh-help)(1)
