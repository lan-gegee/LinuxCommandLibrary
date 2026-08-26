# TAGLINE

在终端中阅读 Learn X in Y Minutes 教程的 CLI

# TLDR

阅读某门编程语言的**教程**

```lexy [language]```

**列出所有可用语言**

```lexy list```

**强制更新**本地文档缓存

```lexy update```

# SYNOPSIS

**lexy** [_options_] [_language_]

# PARAMETERS

_LANGUAGE_
> 要显示其教程的编程语言名称。

**list**
> 列出所有可用语言，并用 fzf 提供模糊选择。

**update**
> 强制更新本地文档缓存。

# DESCRIPTION

**lexy** 是一个轻量级 CLI 工具，可以把 "Learn X in Y Minutes" 上的编程教程直接取回到终端中阅读。它让你无需离开当前工作流就能快速搜索、学习和查阅代码示例。

教程会缓存在本地的 **$HOME/.config/lexy** 目录中，并每 60 天自动更新一次。输出借助 bat 实现语法高亮，默认采用 Catppuccin Mocha 配色方案，可通过 config.toml 自定义。

# CAVEATS

首次下载和定期更新需要联网。语法高亮依赖 **bat**，模糊搜索依赖 **fzf**。教程每 60 天自动更新一次。

# HISTORY

**lexy** 由 **antoniorodr** 创建，采用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#lexy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [cheat](/man/cheat)(1), [bat](/man/bat)(1)
