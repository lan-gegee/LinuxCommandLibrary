# TAGLINE

从 OpenAPI 生成 API 客户端、服务端存根和文档

# TLDR

**生成客户端库**

```openapi-generator generate -i [spec.yaml] -g [python] -o [./client]```

**生成服务端存根**

```openapi-generator generate -i [spec.yaml] -g [spring] -o [./server]```

**列出可用的生成器**

```openapi-generator list```

**使用配置文件生成**

```openapi-generator generate -i [spec.yaml] -g [typescript-axios] -c [config.yaml] -o [./client]```

**校验规范**

```openapi-generator validate -i [spec.yaml]```

**生成文档**

```openapi-generator generate -i [spec.yaml] -g [html2] -o [./docs]```

# SYNOPSIS

**openapi-generator** _command_ [_options_]

# PARAMETERS

**generate**
> 生成代码。

**validate**
> 校验规范。

**list**
> 列出生成器。

**-i** _file_
> 输入的规范文件。

**-g** _generator_
> 生成器名称。

**-o** _dir_
> 输出目录。

**-c** _file_
> 配置文件。

**-p** _params_
> 附加属性。

# DESCRIPTION

**OpenAPI Generator** 从 OpenAPI（Swagger）规范生成 API 客户端、服务端存根和文档。它支持 50 多种语言和框架。

该工具是 Swagger Codegen 的分支，由社区积极开发。

# POPULAR GENERATORS

```
Clients: python, typescript-axios, go, java
Servers: spring, python-flask, go-server
Docs: html2, markdown
```

# CAVEATS

生成的代码可能需要定制。大型规范会生成很多文件。各生成器的成熟度参差不齐。

# HISTORY

OpenAPI Generator 于 **2018 年**由 **William Cheng** 等人从 Swagger Codegen 分叉而来，旨在打造一个更加社区驱动的项目。

# INSTALL

```pacman: sudo pacman -S openapi-generator```

```brew: brew install openapi-generator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oapi-codegen](/man/oapi-codegen)(1)
