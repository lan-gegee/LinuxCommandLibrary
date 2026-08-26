# TAGLINE

运行 Bruno 集合中的 API 请求

# TLDR

运行单个 API 请求

```bru run [request.bru]```

**运行一个文件夹中的所有请求**

```bru run [folder/]```

使用指定的环境运行

```bru run [folder/] --env [production]```

附带环境变量运行

```bru run [request.bru] --env-var [API_KEY=secret]```

生成 JSON、JUnit 和 HTML 报告

```bru run [folder/] --reporter-json [results.json] --reporter-junit [results.xml] --reporter-html [results.html]```

将 OpenAPI 规范导入为 Bruno 集合

```bru import openapi --source [api.yml] --output [~/collections] --collection-name [MyAPI]```

遇到第一个失败即停止运行

```bru run [folder/] --env [staging] --bail```

使用自定义 CA 证书运行

```bru run [request.bru] --cacert [/path/to/ca.crt]```

# SYNOPSIS

**bru** **run** [_paths..._] [_options_]

**bru** **import** _format_ [_options_]

# PARAMETERS

**--env** _name_
> 本次运行使用指定的环境。

**--env-var** _key=value_
> 为本次运行设置环境变量。

**--reporter-json** _file_
> 以 JSON 格式输出结果。

**--reporter-junit** _file_
> 以 JUnit XML 格式输出结果。

**--reporter-html** _file_
> 以 HTML 格式输出结果。

**--cacert** _path_
> 用于 HTTPS 请求的 CA 证书文件路径。

**--insecure**
> 跳过 SSL 证书校验。

**-r**, **--recursive**
> 递归运行子文件夹中的请求。

**--bail**
> 在某个请求、测试或断言失败后停止执行。

**--sandbox** _mode_
> JavaScript 执行模式：safe（默认）或 developer。

**--parallel**
> 并行而非顺序地运行请求。

**--delay** _ms_
> 请求之间的延迟毫秒数。

**--tests-only**
> 只执行包含测试或有效断言的请求。

**--csv-file-path** _file_
> 对 CSV 文件中的每一行各运行一次集合。

**--env-file** _file_
> 环境文件（.bru 或 .json）的路径。

# DESCRIPTION

**bru** 是 Bruno 的命令行界面。Bruno 是一款类似 Postman 或 Insomnia 的开源 API 客户端，直接以纯文本 .bru 文件的形式在文件系统中存储 API 集合，因此对版本控制非常友好。

该 CLI 支持无头执行 API 请求，可用于 CI/CD 流水线、自动化测试和脚本化操作。集合可以与代码仓库存放在一起，便于协作。

# CAVEATS

需要 Node.js 运行时。使用 **npm install -g @usebruno/cli** 安装。从 v3.0.0 起，默认运行时为安全模式；使用 **--sandbox=developer** 可启用外部 npm 包和文件系统访问。该 CLI 用于包含 .bru 文件和可选环境配置的 Bruno 集合文件夹。

# HISTORY

Bruno 作为专有 API 客户端的轻量开源替代品而创建。该项目强调以纯文本形式将集合存储为代码，从而获得更好的 Git 集成和开发工作流。

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [newman](/man/newman)(1)
