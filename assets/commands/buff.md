# TAGLINE

对 Protocol Buffer 文件进行静态检查、格式化和管理

# TLDR

**对 Protocol Buffer 文件进行 lint 检查**

```buf lint [path/to/protos]```

**构建并校验 Protobuf 文件**

```buf build [path/to/protos]```

**检查破坏性变更（breaking changes）**

```buf breaking --against [.git#branch=main]```

**从 Protobuf 生成代码**

```buf generate```

**格式化 Protobuf 文件**

```buf format -w [path/to/protos]```

**将模块推送到 BSR**

```buf push```

**添加依赖**

```buf dep add [buf.build/googleapis/googleapis]```

# SYNOPSIS

**buf** _command_ [_options_] [_path_]

# PARAMETERS

**lint**
> 对 Protobuf 文件运行 lint 规则。

**build**
> 构建 Protobuf 文件并验证能否编译。

**breaking**
> 检查破坏性 API 变更。

**generate**
> 使用已配置的插件生成代码。

**format**
> 格式化 Protobuf 文件。

**push**
> 将模块推送到 Buf Schema Registry（BSR）。

**dep**
> 管理依赖（add、update）。

**convert**
> 在二进制、文本或 JSON 格式之间转换消息。

**curl**
> 调用 RPC 端点，类似 cURL。

**export**
> 将 proto 文件从一个位置导出到另一个位置。

**config**
> 操作 buf 配置文件。

**registry**
> 管理 Buf Schema Registry 上的资源。

**--against** _reference_
> 用于破坏性变更比对的参考基准。

**-w**, **--write**
> 将格式化后的内容写回文件。

**--config** _path_
> buf.yaml 配置文件路径。

**--error-format** _format_
> 错误输出格式：text、json、msvs、github-actions。

# DESCRIPTION

**buf** 是一个处理 Protocol Buffers 的工具，提供 lint 检查、破坏性变更检测、代码生成以及依赖管理生态。它解决了 protoc 和大型 Protobuf 代码库中的常见痛点。

其 lint 引擎在 Protobuf 定义之间强制执行最佳实践和风格一致性。破坏性变更检测会与 git 分支或已发布版本比对，防止意外的 API 不兼容。

代码生成通过 **buf.gen.yaml** 配置，取代了复杂的 protoc 命令行。Buf Schema Registry（BSR）支持以依赖的形式共享 Protobuf 模块并对其进行版本管理，类似于其他语言的软件包管理器。

# CONFIGURATION

**buf.yaml**
> 模块配置，定义 lint 规则、破坏性变更策略和依赖。

**buf.gen.yaml**
> 代码生成配置，指定插件和输出目录。

**buf.lock**
> 依赖锁定文件，保证构建可复现。

# CAVEATS

大多数操作都需要 buf.yaml 配置文件。向 BSR 推送模块需要进行身份验证。破坏性变更检测可能将有意的变更标记为 breaking；请仔细审查。部分 protoc 插件可能与 buf generate 不能直接兼容。

# HISTORY

Buf 由前 Uber 工程师 **Peter Edge** 创建，并于 **2020 年**成立 **Buf Technologies** 公司。它的开发动机是解决管理大型 Protobuf 代码库时遇到的问题，包括风格不一致、意外的破坏性变更和复杂的构建配置。Buf Schema Registry 的推出为 Protobuf 依赖提供了类 npm/Maven 的体验。

# SEE ALSO

[protoc](/man/protoc)(1), [grpcurl](/man/grpcurl)(1)
