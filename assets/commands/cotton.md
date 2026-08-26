# TAGLINE

基于 Markdown 的 API 测试规格运行器

# TLDR

**运行单个测试规格**文件

```cotton [spec.md]```

**运行目录中的所有规格**

```cotton [tests/]```

**以自定义基础 URL 运行**

```cotton -u [https://api.example.com] [tests/]```

**以详细模式运行**（verbose 输出）

```cotton -d [spec.md]```

**注入预定义变量**

```cotton -p [token=abc123] [spec.md]```

**在首次失败时停止**

```cotton -s [tests/]```

**监视文件变化**并自动重新运行

```cotton -w [tests/]```

# SYNOPSIS

**cotton** [_-u baseurl_] [_-i_] [_-d_] [_-w_] [_-s_] [_-p name=value_] _test-cases_

# PARAMETERS

**-u** _url_
> 所有请求的基础 URL（默认：http://localhost:8080）。

**-i**
> 不安全模式：禁用 TLS 证书校验。

**-d**
> 详细模式：为每个测试打印完整的输出。

**-w**
> 监视模式：文件变化时自动重新运行测试。

**-s**
> Panic 模式：在首次失败时停止执行。

**-p** _name=value_
> 向测试规格注入预定义变量（可重复使用）。

**-h**
> 显示帮助信息。

**-v**
> 显示版本信息。

# DESCRIPTION

**cotton** 是一个命令行测试运行器，执行以 Markdown 格式编写的 RESTful API 测试。测试规格是包含 HTTP 请求描述和预期响应断言的 Markdown 文件，使测试本身成为人类可读的活文档。

Cotton 读取每份 Markdown 规格，提取其中定义的 HTTP 请求和预期结果，对目标 API 执行请求，并报告通过/失败的结果。`_test-cases_` 参数可以是单个 Markdown 文件、一个存放 Markdown 文件的目录，或 glob 模式。

变量可以通过 **-p** 注入，并在规格内部用 `{{ variable_name }}` 语法引用。Cotton 支持在规格文件内进行 setup 和 teardown 操作，并区分带断言的 test case 和不带断言的 executable。

# CAVEATS

测试使用一种特定的 Markdown 方言编写；规格格式请参阅项目文档。TLS 校验默认启用；仅在开发环境中使用 `-i`。基础 URL 默认为 http://localhost:8080，访问远程 API 时必须覆盖它。

# SEE ALSO

[curl](/man/curl)(1)
