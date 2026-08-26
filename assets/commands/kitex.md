# TAGLINE

从 Thrift 或 Protobuf IDL 文件生成 Go 代码

# TLDR

**生成服务端代码**

```kitex -module [module] [idl_file.thrift]```

**生成客户端代码**

```kitex -module [module] -client [idl_file.thrift]```

**指定服务名称**

```kitex -module [module] -service [svc] [idl.thrift]```

**使用 Protobuf**

```kitex -module [module] [idl.proto]```

**指定 IDL include 路径**

```kitex -module [module] -I [path/to/includes] [idl.thrift]```

**复用现有的 kitex_gen 目录**

```kitex -module [module] -service [svc] -use [import/path/to/kitex_gen] [idl.thrift]```

# SYNOPSIS

**kitex** [_options_] _idl_file_

# PARAMETERS

_IDL_FILE_
> Thrift 或 Protobuf IDL 文件。

**-module** _NAME_
> Go module 名称。

**-service** _NAME_
> 服务名称。

**-I** _PATH_
> 添加 IDL include 的搜索路径。可多次指定。

**-use** _PATH_
> 跳过生成 kitex_gen，改用指定的 import 路径。

**-v**, **-verbose**
> 生成过程中输出更多日志。

**-type** _TYPE_
> 当无法从文件扩展名判断时指定 IDL 类型。

**-combine-service**
> 将 IDL 中的所有服务合并为一个服务（仅限 Thrift）。

**-gen-path** _DIR_
> 指定生成代码的输出目录（默认：kitex_gen）。

**-thrift** _VALUE_
> 向 thriftgo 编译器传递参数。

**-protobuf** _VALUE_
> 向 protoc 编译器传递参数。

# DESCRIPTION

**kitex** 是 Kitex 高性能 RPC 框架的代码生成工具，Kitex 属于字节跳动开源的 CloudWeGo 生态系统。它读取 Thrift 或 Protocol Buffers 接口定义语言（IDL）文件，为服务器和客户端生成 Go 脚手架代码，包括服务接口、请求/响应类型、序列化逻辑以及一个可运行的项目骨架。

生成的代码面向构建 Go 微服务，连接池、负载均衡和熔断等特性已内置于 Kitex 框架中。默认情况下，kitex 会同时生成服务端和客户端代码，而 `-client` 标志则将输出限制为仅客户端存根。可以通过 `-template` 选项提供自定义代码模板，以控制生成项目的结构和风格。

# CAVEATS

CloudWeGo 的一部分。仅针对 Go。需要 Thrift 或 Protobuf IDL。

# HISTORY

kitex 是 **Kitex** 的代码生成器。Kitex 是 **ByteDance**（字节跳动）创建的高性能 RPC 框架。

# INSTALL

```brew: brew install kitex```

```nix: nix profile install nixpkgs#kitex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[thrift](/man/thrift)(1), [protoc](/man/protoc)(1), [go](/man/go)(1)
