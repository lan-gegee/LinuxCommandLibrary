# TAGLINE

Protocol Buffers 编译器与代码生成器

# TLDR

从 .proto 文件**生成 Python 代码**

```protoc --python_out=[path/to/output_directory] [input_file.proto]```
  
从导入了其他 .proto 文件的 .proto 文件**生成 Java 代码**

```protoc --java_out=[path/to/output_directory] --proto_path=[path/to/import_search_path] [input_file.proto]```
  
使用插件**生成 Go 代码**

```protoc --go_out=[path/to/output_directory] --go_opt=paths=source_relative [input_file.proto]```

将文本格式的消息**编码**为来自 .proto 文件的 **protocol message**

```protoc < [message.txt] --encode=[TypeName] [input_file.proto]```

将 **protocol message** **解码**为来自 .proto 文件的文本格式

```protoc < [message.bin] --decode=[TypeName] [input_file.proto]```

将 **protocol message** **解码**为原始的 tag/value 对

```protoc < [message.bin] --decode_raw```

# SYNOPSIS

**protoc**  [**--cpp_out=**_OUT_DIR_] [**--java_out=**_OUT_DIR_] [**--python_out=**_OUT_DIR_] [**-I**_PATH_  |  **--proto_path=**_PATH_]  _PROTO_FILE_

# DESCRIPTION

**protoc** 是 Google Protocol Buffers 的官方编译器。Protocol Buffers 是一个语言中立的序列化框架。它读取描述结构化数据格式的 **.proto** 定义文件，并生成特定语言的源代码，用于在 C++、Java、Python、Go 及许多其他语言中通过插件高效地序列化和反序列化数据。

编译器使用 **-I**（或 **--proto_path**）指定的搜索路径解析 .proto 文件之间的导入，并且可以在一次调用中为多种目标语言生成代码。它还支持在命令行上编码和解码 protocol buffer 消息，便于调试和测试。

protoc 是 gRPC 生态的核心组件，在 gRPC 中 .proto 文件同时定义远程过程调用的数据结构和服务接口。

# OPTIONS

**-I**_PATH_,  **--proto_path=**_PATH_

> 指定搜索导入文件的目录。可以多次指定，目录将按顺序搜索。若未指定，则使用当前工作目录。

**--cpp_out=**_OUT_DIR_

> 启用 C++ 绑定生成，并将其存储到 _OUT_DIR_。

**--java_out=**_OUT_DIR_

> 启用 Java 绑定生成，并将其存储到 _OUT_DIR_。

**--python_out=**_OUT_DIR_

> 启用 Python 绑定生成，并将其存储到 _OUT_DIR_。

**-h**,  **--help**

> 显示选项摘要。

**--go_out=**_OUT_DIR_

> 启用 Go 绑定生成，并将其存储到 _OUT_DIR_（需要 protoc-gen-go 插件）。

**--plugin=**_NAME=PATH_

> 指定用于代码生成的外部插件可执行文件。

**--version**

> 显示程序版本。

必须至少给出一个输出选项（例如 **--cpp_out**、**--java_out**、**--python_out**、**--go_out**）。一次调用中可以指定多个输出。

# CAVEAT

路径解析十分挑剔：它要求为所有 .proto 文件和导入提供精确的 --proto_path (-I) 标志，如果路径不完全匹配就会经常报 "file not found" 错误（没有智能的相对/绝对路径等价处理）。务必从 proto 根目录运行，在 -I 中包含父级路径，并考虑使用 Buf 之类的封装工具以简化处理。

# HISTORY

最初于 **2001 年**在 **Google** 内部开发，用于比 XML 更高效地处理结构化数据序列化，首个公开版本于 **2008 年**以开源许可发布。protoc 编译器也随之演进，最初是基于 C++ 的工具，后来通过生成的代码存根扩展支持 Java、Python 和 Go 等多种语言。多年来它持续更新，版本 3 在 **2016 年**引入了重大的语法变化，近期的迭代则侧重于性能优化以及与 gRPC 的更好集成。

# INSTALL

```apt: sudo apt install protobuf-compiler```

```dnf: sudo dnf install protobuf-compiler```

```apk: sudo apk add protoc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[buff](/man/buff)(1), [grpc](/man/grpc)(1)

# RESOURCES

```[Source code](https://github.com/protocolbuffers/protobuf)```

```[Homepage](https://protobuf.dev)```

```[Documentation](https://protobuf.dev/reference/)```

<!-- verified: 2026-06-09 -->
