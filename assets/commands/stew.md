# TAGLINE

用于 GitHub 编译版二进制文件的软件包管理器

# TLDR

**安装 GitHub 项目的最新发行版**

```stew install [junegunn/fzf]```

**使用 TUI 在 GitHub 上搜索项目**

```stew search [ripgrep]```

**升级所有已安装的二进制文件**

```stew upgrade --all```

# SYNOPSIS

**stew** _command_ [_arguments_]

# DESCRIPTION

**stew** 是一个零运行时依赖的单二进制软件包管理器，可从 GitHub releases 或直接 URL 安装编译好的二进制文件。它支持通过 Stewfile 进行声明式包管理、版本锁定和私有仓库，并提供 TUI 用于搜索和浏览 GitHub 发行版。

# HISTORY

**stew** 由 **Marwan Hawari** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S stew```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eget](/man/eget)(1), [cargo-binstall](/man/cargo-binstall)(1), [brew](/man/brew)(1)
