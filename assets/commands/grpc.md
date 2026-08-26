# TAGLINE

高性能远程过程调用框架

# TLDR

**从 proto 生成 Go 代码**

```protoc --go_out=. --go-grpc_out=. [service.proto]```

**生成 Python 代码**

```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. [service.proto]```

**调用 gRPC 服务**

```grpcurl -plaintext [localhost:50051] [package.Service/Method]```

**列出服务**

```grpcurl -plaintext [localhost:50051] list```

# DESCRIPTION

**gRPC** 是一个使用 Protocol Buffers 进行序列化的高性能 RPC 框架。它以流式传输、身份验证和负载均衡等特性实现服务之间的高效通信。

gRPC 使用 HTTP/2 作为传输层，并能根据 .proto 服务定义为多种语言生成代码。

# PROTO FILE EXAMPLE

```protobuf
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
  rpc SayHelloStream (HelloRequest) returns (stream HelloReply);
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

# TOOLS

```
protoc          Protocol buffer compiler
grpcurl         Command-line gRPC client
grpc_cli        Official gRPC CLI
evans           Interactive gRPC client
```

# CAVEATS

需要 protocol buffer 定义。需要 HTTP/2；部分代理不支持。调试比 REST 困难。浏览器支持需要 gRPC-Web。

# HISTORY

gRPC 由 **Google** 开发并于 **2015 年**开源。它基于 Google 内部的 Stubby RPC 框架构建，如今是 CNCF 项目，在云原生应用中被广泛使用。

# INSTALL

```dnf: sudo dnf install grpc```

```pacman: sudo pacman -S grpc```

```brew: brew install grpc```

```nix: nix profile install nixpkgs#grpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[protoc](/man/protoc)(1), [grpcurl](/man/grpcurl)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/grpc/grpc)```

```[Homepage](https://grpc.io/)```

```[Documentation](https://grpc.io/docs/)```

<!-- verified: 2026-07-17 -->
