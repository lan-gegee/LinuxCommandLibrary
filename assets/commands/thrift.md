# TAGLINE

Apache Thrift 跨语言代码生成器

# TLDR

从 Thrift 文件**为特定语言生成代码**

```thrift --gen [language] [file.thrift]```

在指定的输出目录中**生成代码**

```thrift --gen [language] -o [output_directory] [file.thrift]```

带语言专属选项**生成代码**

```thrift --gen [language]:key1=val1,key2=val2 [file.thrift]```

为所有被引用的 Thrift 文件一并**生成代码**

```thrift -r --gen [language] [file.thrift]```

为 Thrift 导入**添加 include 搜索路径**

```thrift -I [include_dir] --gen [language] [file.thrift]```

**列出所有可用的生成器**

```thrift --help```

# SYNOPSIS

**thrift** [**-o** _dir_] [**-out** _dir_] [**-I** _dir_] [**-nowarn**] [**-strict**] [**-v**] [**-r**] [**-debug**] **--gen** _lang_[:_options_] _file.thrift_

# PARAMETERS

**--gen** _lang_[:_key=val,..._]
> 使用指定的生成器生成代码。语言选项可以逗号分隔的 key=value 键值对形式传入。

**-o** _dir_
> 设置 gen-* 包的输出目录。默认为当前目录。

**-out** _dir_
> 直接设置输出位置，不创建 gen-* 文件夹。

**-I** _dir_
> 添加一个目录用于查找 include 指令。可多次指定。

**-r**, **--recurse**
> 递归地为被包含的 Thrift 文件也生成代码。

**-nowarn**
> 抑制所有编译器警告。

**-strict**
> 启用严格的编译器警告。

**-v**, **--verbose**
> 启用详细输出模式。

**-debug**
> 将解析调试跟踪打印到 stdout。

**-version**
> 打印编译器版本后退出。

# DESCRIPTION

**thrift** 是 Apache Thrift 的编译器，后者是一个可伸缩的跨语言服务开发框架。它将软件栈与代码生成引擎相结合，在 C++、Java、Python、PHP、Ruby、Erlang、Perl、Haskell、C#、JavaScript、Node.js 等语言之间构建高效且无缝衔接的服务。

编译器读取包含结构体和服务定义的 Thrift 接口定义语言（IDL）文件，然后生成特定语言的实现代码。这让开发者只需定义一次数据类型和服务接口，即可为多种编程语言生成样板代码。

常用生成器包括：**cpp**、**java**、**py**、**rb**、**php**、**js**、**go**、**rs**（Rust）、**swift** 等众多选项。不带参数运行 **thrift** 可查看当前安装支持的所有生成器。

# CAVEATS

不同语言生成器的代码结构和选项差异很大。某些生成器可能需要额外安装运行时库。一般不建议使用 **-nowarn** 标志，因为它可能掩盖重要的兼容性问题。

# HISTORY

Apache Thrift 最初由 **Facebook** 于 **2007 年**开发，并于 **2008 年 4 月**开源。它在 2008 年 5 月成为 Apache 孵化器项目，并于 **2010 年 10 月**毕业成为 Apache 顶级项目。该框架的设计目标是让跨编程语言的高效可靠通信能够大规模实现。

# INSTALL

```apt: sudo apt install thrift-compiler```

```dnf: sudo dnf install thrift```

```pacman: sudo pacman -S thrift```

```apk: sudo apk add thrift```

```zypper: sudo zypper install thrift```

```brew: brew install thrift```

```nix: nix profile install nixpkgs#thrift```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[protoc](/man/protoc)(1), [grpc](/man/grpc)(1)
