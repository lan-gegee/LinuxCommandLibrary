# TAGLINE

Base16 配色方案管理器

# TLDR

**应用主题**

```flavours apply [theme-name]```

**列出可用主题**

```flavours list```

**生成 Shell 补全**

```flavours generate [bash|zsh|fish]```

**构建模板**

```flavours build [template-path]```

**更新配色方案**

```flavours update schemes```

# SYNOPSIS

**flavours** [_options_] _command_ [_args_]

# PARAMETERS

**apply** _theme_
> 将 Base16 主题应用到已配置的应用程序。

**list**
> 列出可用主题。

**info** _theme_
> 显示主题信息。

**build** _template_
> 从模板构建配置文件。

**update** _target_
> 更新配色方案、模板或全部内容。

**generate** _shell_
> 生成 Shell 补全脚本。

**current**
> 显示当前已应用的主题。

# DESCRIPTION

**flavours** 是一个用 Rust 编写的 Base16 主题管理器。它通过从模板生成配置文件，将统一的配色方案应用到多个应用程序。

Base16 提供 16 色 scheme，设计上可跨终端、编辑器和其他应用程序工作。flavours 自动将这些方案同时应用到所有已配置的应用程序。

# CONFIGURATION

**~/.config/flavours/config.toml**
> 定义哪些应用程序接收主题更新及其模板映射。每个条目指定目标文件、模板名称以及可选的子模板。

配置示例：
```toml
[[items]]
file = "~/.config/alacritty/alacritty.yml"
template = "alacritty"
subtemplate = "default-256"

[[items]]
file = "~/.config/nvim/colors/base16.vim"
template = "vim"
```

# CAVEATS

每个应用程序都需要对应的模板。并非所有应用都支持 Base16。主题更改后可能需要重启应用。模板语法必须正确。

# HISTORY

flavours 作为现有 Base16 管理器的 Rust 替代品而创建。Base16 本身由 **Chris Kempson** 创建，旨在为不同应用程序提供一致的主题架构。

# INSTALL

```brew: brew install flavours```

```nix: nix profile install nixpkgs#flavours```

<!-- packages: 2026-07-22 -->

# SEE ALSO
