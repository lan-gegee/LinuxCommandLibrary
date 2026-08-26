# TAGLINE

语法受 Ruby 启发的静态类型编译型语言

# TLDR

**运行 Crystal 程序**

```crystal run [path/to/file.cr]```

**编译为可执行文件**

```crystal build [path/to/file.cr]```

**开启优化编译**（release 模式）

```crystal build --release [path/to/file.cr]```

**新建项目**

```crystal init app [project_name]```

**运行项目的 spec 测试**

```crystal spec```

只检查格式而不修改文件

```crystal tool format --check [path/to/file.cr]```

**格式化源代码**

```crystal tool format [path/to/file.cr]```

**生成文档**

```crystal docs```

# SYNOPSIS

**crystal** [_command_] [_options_] [_file_] [_--_] [_arguments_]

# PARAMETERS

**run** _file_
> 编译并运行程序。

**build** _file_
> 编译为可执行文件。

**spec**
> 运行项目的 spec 测试套件。

**init** _type name_
> 创建新的 Crystal 项目（app 或 lib）。

**docs**
> 生成 API 文档。

**tool format** _files_
> 格式化 Crystal 源代码。

**tool hierarchy** _type_
> 显示类型层级结构。

**tool implement** _type_
> 显示方法的实现。

**play**
> 启动 Crystal playground Web 服务器。

**--release**
> 以 release 模式开启优化编译。

**-o**, **--output** _file_
> 指定输出可执行文件的名称。

**--progress**
> 显示编译进度。

**--no-color**
> 禁用彩色输出。

**-D**, **--define** _flag_
> 定义一个编译期标志。

**--static**
> 静态链接。

**--cross-compile**
> 生成交叉编译所需的目标文件。

# DESCRIPTION

**crystal** 是 Crystal 编程语言的命令行接口。Crystal 是一种语法受 Ruby 启发的静态类型编译语言，目标是达到 C 级别的性能，同时保持对程序员友好的开发体验。

主要命令有 **run**（开发期间快速执行）和 **build**（构建可分发的二进制文件）。Crystal 通过 LLVM 编译，生成原生机器码。**--release** 标志可为生产构建启用优化。

Crystal 使用基于 spec 的测试框架。**spec** 命令运行 **spec/** 目录中的测试。其测试语法类似 Ruby 的 RSpec，Ruby 开发者会感到熟悉。

**init** 命令为新项目搭建标准目录结构、shard.yml（依赖清单）和初始文件。依赖（shard）则由单独的 **shards** 命令管理，类似于 Ruby 中的 Bundler。

Crystal 内置代码格式化和文档生成功能。playground 提供了一个基于 Web 的交互式环境，便于试验代码。

# CAVEATS

大型项目的编译可能缓慢且占用大量内存。交叉编译需要专门的配置。某些 Ruby 语法模式无法直接照搬。标准库比更成熟的语言要小。静态链接可能需要额外的系统库。

# HISTORY

**Crystal** 由 Ary Borenszweig 和 Juan Wajnerman 创建，开发始于 **2011** 年，首次公开发布在 **2014** 年。该语言的设计目标是将 Ruby 的表达力与静态类型和原生性能相结合。1.0 版本于 **2021 年 3 月**发布，标志着该语言已可用于生产环境。

# INSTALL

```apt: sudo apt install crystal```

```pacman: sudo pacman -S crystal```

```apk: sudo apk add crystal```

```brew: brew install crystal```

```nix: nix profile install nixpkgs#crystal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shards](/man/shards)(1), [ruby](/man/ruby)(1), [rustc](/man/rustc)(1)
