# TAGLINE

类似 curl 的命令行 gRPC 客户端

# TLDR

**列出服务**（借助服务器反射）

```grpcurl [localhost:50051] list```

**描述某个服务**

```grpcurl [localhost:50051] describe [package.ServiceName]```

用 JSON 输入**调用方法**

```grpcurl -d '{"name": "[value]"}' [localhost:50051] [package.Service/Method]```

**改用 proto 文件调用**（不依赖反射）

```grpcurl -proto [service.proto] -d '{"id": 1}' [localhost:50051] [package.Service/Method]```

**以明文方式调用**（不用 TLS）

```grpcurl -plaintext [localhost:50051] [package.Service/Method]```

**添加元数据/请求头**

```grpcurl -H "Authorization: Bearer [token]" [localhost:50051] [package.Service/Method]```

**从文件流式发送数据**

```grpcurl -d @ [localhost:50051] [package.Service/Method] < [data.json]```

**列出服务的方法**

```grpcurl [localhost:50051] list [package.ServiceName]```

# SYNOPSIS

**grpcurl** [_options_] _target_ [_method_] [_request_]

# PARAMETERS

**-d** _data_
> 以 JSON 字符串形式提供请求数据（使用 @ 表示从标准输入读取）。

**-proto** _file_
> 定义服务的 proto 文件（反射的替代方案）。

**-protoset** _file_
> 预编译的 proto 描述符文件。

**-import-path** _path_
> 查找 proto 导入的路径。

**-plaintext**
> 使用明文（无 TLS）连接。

**-insecure**
> 跳过 TLS 证书验证。

**-H** _header_
> 添加格式为 "name: value" 的请求头（可重复）。

**-rpc-header** _header_
> 添加 gRPC 元数据头。

**-authority** _name_
> 设置 :authority 伪头。

**-connect-timeout** _seconds_
> 连接超时时间。

**-max-time** _seconds_
> 调用的最长时限。

**-format** _fmt_
> 输出格式：json（默认）或 text。

**-v**
> 详细输出（显示请求头）。

**list**
> 列出服务或方法。

**describe**
> 描述服务、方法或消息。

# DESCRIPTION

**grpcurl** 是一款用于与 gRPC 服务器交互的命令行工具，其角色类似于 curl 对 HTTP API 的作用。它可以调用 RPC 方法、检查服务，并帮助调试基于 gRPC 的应用。

该工具有两种发现服务的方式：服务器反射（由服务器自行描述其 API）或提供 proto 文件。反射很方便，但必须在服务器上启用。proto 文件适用于任何服务器，但要求持有服务定义。

对于一元（unary）调用，请求数据通过 -d 标志以 JSON 提供。流式调用可以从标准输入读取多条消息。响应数据默认以 JSON 输出，便于用 jq 等工具解析。

**grpcurl** 替你处理了 gRPC 的 HTTP/2 传输、protobuf 编码和 TLS 的复杂性。对于非 TLS 服务器（开发环境常见），需要使用 -plaintext 标志。对于启用了 TLS 的生产服务器，可能还需要正确的证书。

# CAVEATS

要发现服务，服务器必须启用反射，或者必须提供 proto 文件。protobuf 的 JSON 表示存在边缘情况（尤其是 bytes、枚举和 64 位整数）。流式调用的交互模式有所不同。截止时间（deadline）等某些 gRPC 特性需要显式配置。

# HISTORY

**grpcurl** 由 FullStory Inc. 创建并以开源形式发布。它的出现源于微服务通信日益普及的 gRPC 生态需要一个等价于 curl 的工具。该工具以 Go 编写，使用官方的 gRPC-Go 库。

# INSTALL

```dnf: sudo dnf install grpcurl```

```brew: brew install grpcurl```

```nix: nix profile install nixpkgs#grpcurl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [protoc](/man/protoc)(1)
