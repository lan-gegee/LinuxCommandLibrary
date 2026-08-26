# TAGLINE

具备丰富 IDE 功能的 Scala 语言服务器

# TLDR

**使用 Coursier 安装 Metals**

```cs bootstrap org.scalameta:metals_2.13:[version] -o metals -f```

**将 Metals 作为 MCP 服务器为工作区启动**

```metals-mcp --workspace [/path/to/project]```

**在指定端口上启动 Metals MCP 服务器**

```metals-mcp --workspace [/path/to/project] --port [8080]```

**为特定客户端生成编辑器配置**

```metals-mcp --workspace [/path/to/project] --client [vscode]```

# SYNOPSIS

**metals** [_options_]

**metals-mcp** **--workspace** _path_ [_options_]

# PARAMETERS

**--workspace** _path_
> Scala 项目的路径（MCP 服务器必需）。

**--port** _number_
> 监听的 HTTP 端口。默认自动分配。

**--transport** _type_
> 传输类型：http（默认）或 stdio。

**--client** _name_
> 要为其生成配置的客户端（例如 vscode、cursor）。

**-v**, **--version**
> 打印版本信息。

**-h**, **--help**
> 打印用法消息。

# DESCRIPTION

**Metals** 是一个实现了语言服务器协议（LSP）的 Scala 语言服务器。它为 Scala 项目提供代码补全、导航、重构和错误检查等 IDE 功能。

Metals 可与多种编辑器配合使用，包括 VS Code、Vim/Neovim、Emacs 和 Sublime Text。

# SUPPORTED BUILD TOOLS

```
- sbt
- Mill
- Gradle
- Maven
- Bloop
```

# FEATURES

```
- Code completion
- Go to definition
- Find references
- Rename refactoring
- Code actions
- Diagnostics
```

# CAVEATS

需要 JDK 11 及以上版本。初始索引需要时间。构建工具必须受支持。性能取决于项目规模。

# HISTORY

Metals 由 **Ólafur Páll Geirsson** 于 **2018 年**在 **Scala Center** 创建，是官方的 Scala 语言服务器。

# INSTALL

```brew: brew install metals```

```nix: nix profile install nixpkgs#metals```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scala](/man/scala)(1), [sbt](/man/sbt)(1), [javac](/man/javac)(1)
