# TAGLINE

从命令行运行 Postman 集合

# TLDR

**运行 Postman 集合**

```newman run [collection.json]```

**使用环境变量运行**

```newman run [collection.json] -e [environment.json]```

**运行指定文件夹**

```newman run [collection.json] --folder "[folder name]"```

**导出结果**

```newman run [collection.json] -r [html] --reporter-html-export [report.html]```

**多次迭代运行**

```newman run [collection.json] -n [10]```

**使用数据文件运行**

```newman run [collection.json] -d [data.csv]```

**设置超时时间**

```newman run [collection.json] --timeout-request [5000]```

# SYNOPSIS

**newman** **run** _collection_ [_options_]

# PARAMETERS

_COLLECTION_
> Postman 集合文件路径或 URL。

**-e** _FILE_
> 指定环境文件。

**-g** _FILE_
> 指定全局变量文件。

**--folder** _NAME_
> 只运行集合中的特定文件夹。

**-r** _REPORTERS_
> 逗号分隔的报告器类型（cli、json、junit、html）。

**-n** _COUNT_
> 运行的迭代次数。

**-d** _FILE_
> 用于迭代变量的数据文件（CSV 或 JSON）。

**--global-var** _KEY=VALUE_
> 通过命令行设置全局变量（可重复）。

**--env-var** _KEY=VALUE_
> 通过命令行设置环境变量（可重复）。

**--bail**
> 在第一个测试失败时停止运行。

**--timeout** _MS_
> 等待整个集合运行完成的毫秒数。

**--timeout-request** _MS_
> 等待每个请求完成的毫秒数。

**-x**, **--suppress-exit-code**
> 覆盖本次运行的默认退出码。

**--color** _VALUE_
> 控制彩色输出：on、off 或 auto（默认）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**newman** 是 Postman 的命令行配套工具，可运行导出的集合，实现自动化 API 测试。它按顺序执行集合中的所有请求，运行前置脚本和测试脚本，并报告结果。

Newman 可集成到 CI/CD 流水线中以实现 API 测试自动化。它支持通过 CSV/JSON 文件进行数据驱动测试、多种报告器格式化输出，以及环境/全局变量管理。

# CAVEATS

需要 Node.js。集合必须以 JSON 格式从 Postman 导出。HTML 报告器需要额外的 npm 包（newman-reporter-html）。Collection v1 格式已弃用；请使用 v2 或更高版本。

# HISTORY

Newman 由 **Postman** 创建，用于在命令行执行 API 集合，实现测试自动化。

# INSTALL

```brew: brew install newman```

```nix: nix profile install nixpkgs#newman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [postman](/man/postman)(1), [npm](/man/npm)(1)
