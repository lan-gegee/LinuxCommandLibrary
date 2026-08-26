# TAGLINE

用于从文件执行 HTTP、gRPC、WebSocket 和 MQTT 请求的命令行工具

# TLDR

**执行 HTTP 文件中的所有请求**

```httpyac send [path/to/requests.http]```

**执行目录中的所有请求**

```httpyac send [path/to/directory]```

**以指定环境执行**

```httpyac send --env [production] [path/to/requests.http]```

**执行文件中的所有请求**

```httpyac send --all [path/to/requests.http]```

**以交互模式运行**

```httpyac send -i [path/to/requests.http]```

# SYNOPSIS

**httpyac** **send** [**--all**] [**--env** _name_] [**-i**] [_options_] _file_

# DESCRIPTION

**httpyac** 是一个命令行界面，用于执行定义在 **.http** 和 **.rest** 文件中的请求。它支持 **HTTP**、**REST**、**GraphQL**、**WebSocket**、**gRPC** 和 **MQTT** 协议。该工具内置对多种认证方法的支持，包括 **OAuth2**、**AWS**、**Basic**、**Digest** 和 **SSL 客户端证书**。

httpyac 支持变量、环境配置（包括 dotenv 文件）以及脚本功能，可应对复杂的测试场景。它既可以用于快速的临时请求，也可以用于 CI/CD 流水线中的自动化 API 测试。

# CAVEATS

需要 Node.js 运行时。请求文件格式遵循 IntelliJ HTTP 客户端规范及其扩展。编写复杂脚本可能需要熟悉 JavaScript。

# HISTORY

**httpyac** 由 **Andreas Weber**（AnWeber）创建，使用 **TypeScript/JavaScript** 编写。它还提供 **VS Code 扩展**版本，可在编辑器内集成执行 HTTP 请求。

# INSTALL

```brew: brew install httpyac```

```nix: nix profile install nixpkgs#httpyac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [hurl](/man/hurl)(1), [httpie](/man/httpie)(1)
