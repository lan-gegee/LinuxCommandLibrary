# TAGLINE

类 Postman 的终端 API 客户端

# TLDR

在当前目录**启动 TUI**

```atac```

**指定自定义应用目录**

```atac -d [path/to/directory]```

**发送一次性 GET 请求**

```atac try [https://api.example.com/endpoint]```

**发送集合中的请求**

```atac request [collection/request_name] send```

**使用环境发送请求**

```atac request [collection/request_name] send --env [my_env]```

**导入 Postman 集合**

```atac import postman [path/to/collection.json]```

**从 cURL 命令导入**

```atac import curl "[curl -X GET https://example.com]"```

**生成 Shell 补全脚本**

```atac completions [bash|zsh|fish]```

# SYNOPSIS

**atac** [**-d** _directory_] [**--filter** _regex_] [**--dry-run**] [**--no-ansi-log**] [**-v**...] [_subcommand_]

# PARAMETERS

**-d** _directory_, **--directory** _directory_
> 主应用目录，包含集合文件、atac.toml 配置文件和 atac.log 文件

**--filter** _regex_
> 仅解析名称匹配给定正则表达式的集合文件

**--tui**
> 执行 CLI 子命令后运行 TUI

**--dry-run**
> 不将数据保存到集合和环境文件

**--no-ansi-log**
> 日志文件输出中不使用 ANSI 格式

**-v**, **--verbose**
> 提高详细程度；可重复使用以获得更多细节

**collection**
> 管理集合（列出、创建、删除、重命名）

**request**
> 管理集合并发送其中的请求

**try**
> 一次性请求发送器，无需已保存的集合即可快速调用 API

**env**
> 管理环境文件和变量

**import**
> 从 Postman v2.1.0、cURL 或 OpenAPI 格式导入集合、请求或环境

**completions**
> 为 bash、zsh 或 fish 生成 Shell 补全脚本

**man**
> 生成 ATAC 的 man page

# DESCRIPTION

**atac**（Arguably a Terminal API Client）是一款功能丰富的基于终端的 API 测试工具，用 Rust 编写。它在终端内提供类 Postman 的体验，同时支持交互式 TUI 模式和可脚本化的 CLI 模式。

TUI 提供完整界面，用于构建和组织 HTTP 请求、查看带语法高亮的响应、管理集合以及在环境之间切换。CLI 模式支持以非交互方式发送请求、管理集合和导入数据，适合脚本编写与自动化场景。

atac 支持所有标准 HTTP 方法，包括 GET、POST、PUT、PATCH、DELETE、OPTIONS、HEAD、TRACE 和 CONNECT。认证方式包括 Basic、Bearer token、Digest 和 JWT。请求体可以是 JSON、XML、HTML、纯文本、multipart 表单、URL 编码表单或文件上传。响应详情完整可见，包括状态码、头部、Cookie 和耗时信息。

除 HTTP 外，atac 还内置 WebSocket 客户端，支持 text、binary、ping、pong 和 close 消息。内置的 JavaScript 运行时支持请求前和请求后脚本，可用于动态修改请求和处理响应。

集合与环境以人类可读的 JSON 或 YAML 文件存储，便于提交到版本控制。环境变量定义在 .env 文件中，并通过 **{{variable_name}}** 语法在请求中引用。该工具可以从 Postman v2.1.0 集合、OpenAPI 规范和 cURL 命令导入，并能将请求导出为 cURL、PHP Guzzle、Node.js Axios、Rust Reqwest 及原始 HTTP 格式。

# CONFIGURATION

**atac.toml** -- 放置在应用目录中的主配置文件。所有键均为可选。

**disable_syntax_highlighting**
> 设为 true 可禁用响应语法高亮（默认：false）

**disable_cors**
> 设为 true 可禁用 CORS 处理（默认：false）

**[proxy] http_proxy**
> HTTP 代理 URL

**[proxy] https_proxy**
> HTTPS 代理 URL

按键绑定通过单独的 TOML 文件配置，该文件由 **ATAC_KEY_BINDINGS** 环境变量指定。项目提供了默认及 Vim 风格的按键绑定模板。

**ATAC_MAIN_DIR** 环境变量可作为 **-d** 标志的替代方案来指定应用目录。

# CAVEATS

从源码构建需要 Rust 1.82 或更高版本。在 macOS 上，从 GitHub releases 下载的二进制可能需要用 **xattr -rd com.apple.quarantine** 移除隔离属性。暂不支持 OAuth 和 AWS 认证。导入仅支持 Postman v2.1.0 集合格式。

# HISTORY

**atac** 由 **Julien Caposiena**（Julien-cpsn）创建，于 **2024** 年 **4 月**首次发布到 crates.io。该项目以 MIT 许可证开源，托管在 GitHub 上。其目标是提供一个免费、免账户、离线优先的替代方案，以取代 Postman 和 Insomnia 等图形化 API 客户端。

# INSTALL

```apt: sudo apt install atac```

```pacman: sudo pacman -S atac```

```brew: brew install atac```

```nix: nix profile install nixpkgs#atac```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [wget](/man/wget)(1), [websocat](/man/websocat)(1), [posting](/man/posting)(1)
