# TAGLINE

用 Rust 编写的类 Ranger 终端文件管理器

# TLDR

**在当前目录启动 joshuto**

```joshuto```

**在指定目录中启动**

```joshuto [path/to/directory]```

# SYNOPSIS

**joshuto** [_options_] [_path_]

# DESCRIPTION

**joshuto** 是一款受 **ranger** 启发的终端文件管理器，用 Rust 编写。它采用三栏布局，分别显示上级目录、当前目录和文件预览栏。导航采用类 **Vim** 的按键绑定，并且像 ranger 一样支持通过可定制的预览脚本实现文件预览。

主要特性包括鼠标支持（默认启用）、剪贴板集成（通过 xsel/xclip/wl-clipboard）、**fzf** 模糊查找集成、**zoxide** 目录跳转集成、批量重命名操作，以及通过 TOML 配置文件完全自定义按键绑定和主题。

# CONFIGURATION

配置文件存放在 **$XDG_CONFIG_HOME/joshuto/** 中，包括 **joshuto.toml**（常规设置）、**keymap.toml**（按键绑定）、**mimetype.toml**（文件关联）和 **theme.toml**（颜色与样式）。

# CAVEATS

从源码构建需要 Rust 1.67+。富预览需要单独配置文件预览脚本。剪贴板支持依赖外部剪贴板工具。

# HISTORY

**joshuto** 由 **kamiyaa** 开发，使用 **Rust** 编写。它的目标是成为现代化、高性能的 ranger 替代品，既发挥 Rust 的性能优势，又保持熟悉的文件管理器操作习惯。

# INSTALL

```brew: brew install joshuto```

```nix: nix profile install nixpkgs#joshuto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1), [yazi](/man/yazi)(1)
