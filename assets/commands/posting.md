# TAGLINE

驻留在你终端中的现代 API 客户端

# TLDR

**启动 HTTP 客户端 TUI**

```posting```

**打开特定的集合目录**

```posting --collection [path/to/collection]```

**加载环境变量文件**

```posting --env [dev.env] --env [secrets.env]```

**导入 Postman v2.1 集合**

```posting import [postman_collection.json]```

**显示帮助**

```posting --help```

# SYNOPSIS

**posting** [_options_] [_subcommand_]

# PARAMETERS

**--collection** _PATH_
> 将给定目录用作请求集合。

**--env** _FILE_
> 从 .env 文件加载环境变量（可重复使用）。

**--config** _FILE_
> 使用备用配置文件。

**import** _FILE_
> 将 Postman v2.1 集合导入 Posting 集合。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**posting** 是一款基于终端的 HTTP 客户端，类似于 Postman 和 Insomnia。请求以 YAML 文件的形式存储在本地，便于版本控制。功能包括 jump 模式导航、环境与变量、基于 tree-sitter 的语法高亮、Vim 按键、可自定义快捷键、请求前/后 Python 脚本、curl 导入/导出，以及从 Postman 和 OpenAPI 规范导入。

# CAVEATS

为以键盘为中心的工作流设计。可通过 SSH 使用。

# HISTORY

**posting** 由 **Darren Burns**（darrenburns）创建，使用 **Python** 编写。

# INSTALL

```brew: brew install posting```

```nix: nix profile install nixpkgs#posting```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [slumber](/man/slumber)(1)
