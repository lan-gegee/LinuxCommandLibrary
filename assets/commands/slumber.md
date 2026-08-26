# TAGLINE

基于终端、使用 YAML 配方的 HTTP/REST 客户端

# TLDR

**使用默认集合启动 TUI**

```slumber```

**通过 CLI 发送请求**

```slumber request --recipe [my_recipe]```

**从 Insomnia 导入请求**

```slumber import insomnia [export.json]```

# SYNOPSIS

**slumber** [_subcommand_] [_options_]

# DESCRIPTION

**slumber** 是一个用于定义、执行和分享 HTTP 请求的 TUI 与 CLI 工具。请求以"配方"（recipe）的形式配置在 YAML 文件中，便于版本控制和团队共享。它支持从 Insomnia 导入、通过模板动态构建请求，并将请求历史存储在本地 SQLite 数据库中。所有数据都保留在本地。

# HISTORY

**slumber** 由 **Lucas Pickering**（LucasPickering）创建，采用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S slumber```

```brew: brew install slumber```

```nix: nix profile install nixpkgs#slumber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [posting](/man/posting)(1)
