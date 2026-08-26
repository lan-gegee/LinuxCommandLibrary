# TAGLINE

用纯文本运行和测试 HTTP 请求

# TLDR

**从 Hurl 文件运行请求**

```hurl [path/to/file.hurl]```

**以测试模式运行**并报告进度

```hurl --test [path/to/file.hurl]```

**带详细输出运行**

```hurl --verbose [path/to/file.hurl]```

**带变量运行**

```hurl --variable [name]=[value] [path/to/file.hurl]```

**并行运行多个文件**

```hurl --parallel [path/to/file1.hurl] [path/to/file2.hurl]```

**以 JSON 输出结果**

```hurl --json [path/to/file.hurl]```

**失败时自动重试**

```hurl --retry [3] [path/to/file.hurl]```

# SYNOPSIS

**hurl** [_options_] [_FILE ..._]

# PARAMETERS

**-u, --user** _user:password_
> 添加基本认证凭据

**-H, --header** _header_
> 添加自定义 HTTP 头

**-L, --location**
> 跟随 HTTP 重定向

**--test**
> 启用测试模式并报告进度

**--json**
> 以 JSON 格式输出结果

**--parallel**
> 并发运行多个文件

**--retry** _num_
> 失败时的重试次数

**--delay** _ms_
> 每个请求前的暂停时间

**--variable** _name=value_
> 定义一个模板变量

**--variables-file** _file_
> 从文件加载变量

**--secret** _name=value_
> 定义一个脱敏变量（不出现在日志中）

**-o, --output** _file_
> 将响应体写入文件

**-k, --insecure**
> 允许不安全的 SSL 连接

**--verbose**
> 启用详细日志

**--very-verbose**
> 启用更详细的日志，包括请求/响应体

**--continue-on-error**
> 即使断言失败也继续执行

**--from-entry** _num_
> 从指定条目开始执行

**--to-entry** _num_
> 在指定条目处停止执行

# DESCRIPTION

**hurl** 是一款命令行工具，用于执行定义在简单纯文本 **.hurl** 文件中的 HTTP 请求。它可以串联多个请求、从响应中捕获值，并通过 XPath、JSONPath 和正则表达式查询对响应头、状态码和响应体内容进行断言。

Hurl 支持 REST、SOAP、GraphQL 以及任何基于 XML/JSON 的 API。它能处理认证、cookie、表单数据、multipart 上传和二进制响应体。它使用 **Rust** 编写并由 **libcurl** 驱动，是一个没有运行时依赖的单一二进制文件。

Hurl 既可用于获取数据，也可用于测试 HTTP 会话，内置对响应状态、请求头、响应体内容、耗时和 SSL 证书的断言支持。多种报告格式（text、JUnit、TAP、HTML）使它能够方便地集成到 CI/CD 流水线中。

# CAVEATS

尽管共享 libcurl 后端，Hurl 文件所用的自定义格式与 curl 命令语法并不兼容。这种纯文本格式要求学习 Hurl 特有的断言与捕获语法。对于格式错误的 .hurl 文件，其报错信息可能晦涩难懂。

# HISTORY

**hurl** 由 **Orange-OpenSource**（法国电信公司）创建，于 **2020 年 8 月**首次发布到 GitHub。它使用 Rust 编写，以 libcurl 作为 HTTP 引擎，目前 GitHub star 数已超过 18000，并且仍在活跃维护。

# INSTALL

```pacman: sudo pacman -S hurl```

```zypper: sudo zypper install hurl```

```brew: brew install hurl```

```nix: nix profile install nixpkgs#hurl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [httpie](/man/httpie)(1)
