# TAGLINE

从 OpenAPI 3 生成 Go 代码

# TLDR

**生成 Go 服务端代码**

```oapi-codegen -generate server -package [api] [spec.yaml] > [server.go]```

**生成 Go 客户端代码**

```oapi-codegen -generate client -package [api] [spec.yaml] > [client.go]```

**仅生成类型定义**

```oapi-codegen -generate types -package [api] [spec.yaml] > [types.go]```

**使用配置文件生成**

```oapi-codegen --config [config.yaml] [spec.yaml]```

**生成所有组件**

```oapi-codegen -generate server,client,types -package [api] [spec.yaml]```

# SYNOPSIS

**oapi-codegen** [_options_] _spec_

# PARAMETERS

**-generate** _type_
> server、client、types、spec、chi-server、gin-server、echo-server。

**-package** _name_
> Go 软件包名称。

**-o** _file_
> 输出文件。

**--config** _file_
> 配置文件。

**-include-tags** _tags_
> 仅包含这些标签。

**-exclude-tags** _tags_
> 排除这些标签。

# DESCRIPTION

**oapi-codegen** 从 OpenAPI 3.0 规范生成 Go 代码。它可以生成服务端样板代码、客户端和类型定义。

支持多种服务端框架，包括 Chi、Gin 和 Echo。

# CONFIG FILE

```yaml
# config.yaml
package: api
generate:
  - types
  - chi-server
  - client
output: api.gen.go
```

# CAVEATS

仅支持 OpenAPI 3.0 及以上版本。生成的代码可能需要修改。大型规范会生成很大的文件。

# HISTORY

oapi-codegen 由 **DeepMap, Inc.** 创建，旨在从 OpenAPI 规范生成高质量的 Go 代码。

# INSTALL

```nix: nix profile install nixpkgs#oapi-codegen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openapi-generator](/man/openapi-generator)(1)
