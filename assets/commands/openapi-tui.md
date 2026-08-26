# TAGLINE

用于浏览和运行 OpenAPI 定义 API 的 TUI

# TLDR

**打开本地规范文件**

```openapi-tui -i [path/to/spec.yaml]```

**从 URL 打开规范**

```openapi-tui -i [https://example.com/openapi.json]```

# SYNOPSIS

**openapi-tui** [_options_]

# PARAMETERS

**-i**, **--input** _PATH_OR_URL_
> OpenAPI 规范文件的路径或 URL（JSON 或 YAML）。

# DESCRIPTION

**openapi-tui** 是一个终端 UI，用于列出、浏览和运行以 OpenAPI v3.0 和 v3.1 规范定义的 API。它支持从本地文件或 URL 加载 JSON 和 YAML 格式的规范，添加查询字符串和请求头，并直接在终端中发起 API 调用。

# CAVEATS

仅支持 OpenAPI v3.0 和 v3.1 规范。Swagger v2 规范必须先进行转换。

# HISTORY

**openapi-tui** 由 **zaghaghi** 创建，使用 **Rust** 语言和 ratatui 库编写。

# INSTALL

```pacman: sudo pacman -S openapi-tui```

```brew: brew install openapi-tui```

```nix: nix profile install nixpkgs#openapi-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1)
