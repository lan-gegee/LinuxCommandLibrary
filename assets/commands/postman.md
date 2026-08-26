# TAGLINE

API 开发与测试平台

# TLDR

**启动 Postman**

```postman```

**从命令行运行集合**

```newman run [collection.json]```

**使用环境变量运行**

```newman run [collection.json] -e [environment.json]```

**导出结果**

```newman run [collection.json] --reporters cli,json --reporter-json-export [results.json]```

# SYNOPSIS

**postman** [_options_]

**newman** run _collection_ [_options_]

# PARAMETERS (newman)

**-e**, **--environment** _file_
> 环境文件。

**-g**, **--globals** _file_
> 全局变量。

**-d**, **--iteration-data** _file_
> 用于迭代的数据文件。

**-n** _count_
> 迭代次数。

**--reporters** _list_
> 输出报告器。

**--timeout** _ms_
> 请求超时时间。

# DESCRIPTION

**Postman** 是一个 API 开发平台，提供用于设计、测试和编写 HTTP API 文档的图形界面。它将请求组织成集合，集合中可以包含测试脚本、环境变量和预请求钩子，便于构建完整的 API 测试套件。

**Newman** 是 Postman 的命令行配套工具，可在 GUI 之外运行 Postman 集合。它支持在 CI/CD 流水线中进行自动化 API 测试，支持环境文件、基于 CSV 或 JSON 数据的数据驱动迭代，以及多种输出报告器，便于与测试报告系统集成。

# EXAMPLES

```bash
# Launch GUI
postman

# Run collection with Newman
newman run my-api-tests.json

# With environment
newman run collection.json -e staging.json

# Data-driven testing
newman run collection.json -d testdata.csv -n 10

# Multiple reporters
newman run collection.json --reporters cli,htmlextra
```

# COLLECTION FORMAT

Postman 集合（JSON）包含：
- 带有 URL、方法和请求头的请求
- 测试（JavaScript 断言）
- 变量和环境

# CAVEATS

Postman 图形界面的云功能需要账户。Newman 可在本地无需账户运行。免费版有限制。

# HISTORY

Postman 由 **Abhinav Asthana** 于 2014 年创立，从一款 Chrome 扩展发展为完整的 API 平台。

# INSTALL

```nix: nix profile install nixpkgs#postman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1)
