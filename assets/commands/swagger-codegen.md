# TAGLINE

从 OpenAPI 规范生成 API 客户端代码

# TLDR

**生成客户端**

```swagger-codegen generate -i [api.yaml] -l [java] -o [output/]```

**列出语言**

```swagger-codegen langs```

**使用配置生成**

```swagger-codegen generate -i [api.yaml] -l [python] -c [config.json] -o [output/]```

**校验规范**

```swagger-codegen validate -i [api.yaml]```

**显示某种语言的帮助**

```swagger-codegen config-help -l [typescript-angular]```

# SYNOPSIS

**swagger-codegen** _command_ [_-i input_] [_-l language_] [_-o output_] [_options_]

# PARAMETERS

**generate**
> 生成代码。

**langs**
> 列出支持的语言。

**validate**
> 校验规范文件。

**-i** _FILE_
> 输入的规范文件。

**-l** _LANG_
> 目标语言。

**-o** _DIR_
> 输出目录。

**-c** _FILE_
> 配置文件。

# DESCRIPTION

**swagger-codegen** 可以根据 OpenAPI（Swagger）规范文件生成 API 客户端库、服务端存根和文档。它读取 YAML 或 JSON 格式的 API 定义，并生成数十种目标语言和框架的代码，包括 Java、Python、TypeScript、Go、Ruby 等。

客户端生成会创建开箱即用的 SDK 代码，包含与 API 规范匹配的模型、API 类和序列化逻辑。服务端存根生成则搭建带路由定义和请求/响应模型的后端代码骨架。文档生成可产出 HTML 或其他格式。

该工具使用 Mustache 模板，模板可以自定义以精确控制输出格式。配置文件可以指定额外选项，如包名、模型命名约定以及目标语言偏好的库。

# CAVEATS

需要 Java。依赖较重。可以考虑改用 openapi-generator。

# HISTORY

**swagger-codegen** 的诞生是为了从 OpenAPI/Swagger 规范生成 API 客户端库。

# INSTALL

```brew: brew install swagger-codegen```

```nix: nix profile install nixpkgs#swagger-codegen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openapi-generator](/man/openapi-generator)(1), [oapi-codegen](/man/oapi-codegen)(1)
