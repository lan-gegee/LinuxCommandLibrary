# TAGLINE

终端中的逐步式 diff 查看器

# TLDR

**查看 diff**

```oyo [path/to/file]```

**用作 git difftool**

```git difftool -t oyo```

# SYNOPSIS

**oyo** [_options_] [_file_]

# DESCRIPTION

**oyo** 是一款逐步式 diff 查看器，在传统 diff 的基础上增加了演进模式。你可以像普通 diff 查看器一样滚动浏览和跳转 hunk，也可以逐个步进查看变更，观察代码从旧版本演变到新版本的过程。

查看模式包括 unified、split、evolution 和 blame。它支持剪贴板集成，并可配置为 git difftool。

# CONFIGURATION

**~/.config/oyo/config.toml**
> UI 设置的配置文件，包括查看模式、自动居中、自动换行和滚动条显示等。

# CAVEATS

最好配合 Git 集成使用。独立查看 diff 时需要格式正确的 diff 输入。

# HISTORY

**oyo** 由 **ahkohd** 创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S oyo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [delta](/man/delta)(1), [difftastic](/man/difftastic)(1)
