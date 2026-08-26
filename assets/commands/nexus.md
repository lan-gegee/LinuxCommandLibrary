# TAGLINE

基于终端的 API 测试 HTTP 客户端

# TLDR

**启动 HTTP 客户端 TUI**

```nexus```

# SYNOPSIS

**nexus** [_options_]

# DESCRIPTION

**nexus** 是一款基于终端的 API 测试 HTTP 客户端，它在 TUI 中复刻了 Postman 的组织化管理方式。它支持所有 HTTP 方法，并可将请求归入集合。

功能包括：编辑包含 URL、请求头、请求体和参数的请求、格式化的响应展示、跨会话保存请求、导入 Postman 集合，以及导出 curl 命令。导航和管理全程使用键盘快捷键。

# CAVEATS

不支持脚本或环境变量替换等全部 Postman 功能。

# HISTORY

**nexus** 由 **Pranav CS**（pranav-cs-1）创建，使用 **Rust** 编写。

# INSTALL

```dnf: sudo dnf install nexus```

```brew: brew install nexus```

```nix: nix profile install nixpkgs#nexus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1)
