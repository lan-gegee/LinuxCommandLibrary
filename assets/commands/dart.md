# TAGLINE

Dart 编程语言的命令行界面

# TLDR

直接**运行 Dart 文件**

```dart [path/to/file.dart]```

**从模板创建新项目**

```dart create -t [console|package|web] [project_name]```

**在当前目录运行项目**

```dart run```

**获取软件包依赖**

```dart pub get```

**编译为原生可执行文件**

```dart compile exe [bin/main.dart] -o [output]```

**分析代码**中的错误和警告

```dart analyze```

**格式化 Dart 源代码**

```dart format [path/to/directory]```

**运行测试**

```dart test```

# SYNOPSIS

**dart** [_OPTIONS_] [_COMMAND_] [_ARGS_]

**dart** [_DART_FILE_]

# COMMANDS

**run** [_DART_FILE_]
> 在 Dart VM 中运行 Dart 程序。

**create** _DIRECTORY_
> 创建新项目。用 -t 选择模板（console、package、web）。

**compile** _FORMAT_
> 将 Dart 编译为多种格式：exe（原生）、js（JavaScript）、aot-snapshot、jit-snapshot、kernel。

**analyze** [_DIRECTORY_|_FILE_]
> 分析 Dart 源代码的错误和警告。

**format** [_DIRECTORY_|_FILE_]
> 按照风格指南格式化 Dart 源代码。

**fix** [_DIRECTORY_|_FILE_]
> 对 Dart 源代码应用自动修复。

**test** [_DIRECTORY_|_FILE_]
> 运行包中的测试。

**pub** _SUBCOMMAND_
> 处理软件包（get、upgrade、publish 等）。

**doc** _DIRECTORY_
> 生成 API 参考文档。

**devtools**
> 启动 Dart DevTools 进行调试和性能分析。

**info**
> 输出 Dart 工具链的诊断信息。

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示 Dart SDK 版本。

**-v**, **--verbose**
> 显示额外的诊断输出。

**--enable-experiment**=_NAME_
> 启用实验性语言特性。

# DESCRIPTION

**dart** 是 Dart 编程语言的命令行界面。它提供运行、编译、测试和管理 Dart 应用与软件包的工具。

Dart 可以通过 JIT 编译直接在 Dart VM 中运行程序，也可以将其编译为原生可执行文件、JavaScript 或 WebAssembly 以便部署。**dart pub** 子命令管理定义在 pubspec.yaml 中的软件包依赖。

该工具为不同应用类型提供了项目模板，包括控制台应用、软件包和 Web 应用。代码分析与格式化工具帮助保持代码一致且无错。

# CAVEATS

开发 Dart 应用需要 Dart SDK。原生编译的可执行文件是平台相关的。使用软件包时，修改 pubspec.yaml 后务必运行 **dart pub get**。部分实验性特性需要通过 --enable-experiment 显式启用。

# HISTORY

Dart 由 Google 开发，于 **2011 年**首次公布。它最初被设计为 Web 开发中 JavaScript 的替代品。随着 **2018 年** Dart 2.0 发布，这门语言变为强类型。同样使用 Dart 的 Flutter 框架自 **2017 年**起推动了大规模采用。统一的 **dart** 命令行工具在 Dart 2.10（2020 年）中取代了 pub、dartanalyzer 和 dartfmt 等各自独立的工具。

# INSTALL

```pacman: sudo pacman -S dart```

```nix: nix profile install nixpkgs#dart```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flutter](/man/flutter)(1), [node](/man/node)(1), [go](/man/go)(1)
