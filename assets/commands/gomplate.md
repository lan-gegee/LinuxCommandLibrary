# TAGLINE

灵活的命令行模板渲染器

# TLDR

**渲染**一个模板文件

```gomplate -f [template.tmpl]```

使用环境变量数据源进行**渲染**

```gomplate -d [config=env:] -f [template.tmpl]```

从标准输入**渲染**

```cat [template.tmpl] | gomplate```

**输出**到文件

```gomplate -f [in.tmpl] -o [out.txt]```

# SYNOPSIS

**gomplate** [*options*]

# DESCRIPTION

**gomplate** 是一个基于 Go 模板构建的模板 CLI。它能从文件、HTTP、环境变量、AWS/GCP 元数据、Consul、Vault 等多种来源获取**数据源（datasources）**，进而渲染文本配置、脚本或清单文件。它常用于生成 Kubernetes YAML、dotenv 文件以及引导脚本，而不必运行完整的编程代码。

# PARAMETERS

**-f**, **--file** *path*

> 模板文件（可重复指定 / 提供目录模式）。

**-o**, **--out** *path*

> 输出文件（默认输出到标准输出）。

**-d**, **--datasource** *alias=url*

> 定义命名数据源（例如 **config=file:///…**、**env:/**）。

**-c**, **--context** *alias=url*

> 把数据源附加到模板上下文中。

**--input-dir** / **--output-dir**

> 批量渲染目录树。

丰富的数据源 URL 方案说明见 https://docs.gomplate.ca/

# CAVEATS

如果模板或数据源不可信，则会带来模板注入风险。网络数据源需要有网络连接和相应凭据。其语法是 Go text/template 加上 gomplate 函数——并非 Jinja/Mustache。

# INSTALL

```apk: sudo apk add gomplate```

```brew: brew install gomplate```

```nix: nix profile install nixpkgs#gomplate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[envsubst](/man/envsubst)(1), [jinja2](/man/jinja2)(1), [ytt](/man/ytt)(1), [helm](/man/helm)(1)

# RESOURCES

```[Source code](https://github.com/hairyhenderson/gomplate)```

```[Documentation](https://docs.gomplate.ca/)```

<!-- verified: 2026-07-19 -->
