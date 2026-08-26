# TAGLINE

Swift 语言编译器与软件包管理器

# TLDR

**启动 REPL**

```swift```

**运行脚本**

```swift [script.swift]```

**构建包**

```swift build```

**以 release 模式构建**

```swift build -c release```

**运行包**

```swift run```

**运行测试**

```swift test```

**创建新包**

```swift package init --type [executable]```

**显示依赖**

```swift package show-dependencies```

# SYNOPSIS

**swift** [_build_] [_run_] [_test_] [_package_] [_options_] [_files_]

# PARAMETERS

**build**
> 构建包。

**run** [_TARGET_]
> 构建并运行。

**test**
> 运行测试。

**package init**
> 创建新包。

**package update**
> 更新依赖。

**package resolve**
> 解析依赖。

**-c** _CONFIG_
> 构建配置（debug、release）。

**-Xswiftc** _FLAG_
> 向编译器传递标志。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**swift** 是 Swift 编程语言的编译器和软件包管理器，用于构建、运行和测试 Swift 应用程序。

REPL 提供交互式的 Swift 执行环境，适合实验和学习。

Swift Package Manager 负责依赖管理和构建。Package.swift 定义目标、依赖和产品。

Debug 构建编译速度快并支持调试。Release 构建则针对性能进行优化。

测试集成 XCTest 框架，通过 swift test 运行，支持并行执行。

跨平台支持覆盖 Apple 平台之外的 Linux 和 Windows。服务端 Swift 是常见的使用场景。

# CAVEATS

在 macOS 上功能完整。Linux 支持良好但部分 Apple 框架不可用。Windows 支持较新。

# HISTORY

**Swift** 由 **Apple** 在 **2014 年** WWDC 上发布，由 **Chris Lattner** 等人开发，并于 **2015 年**开源。此后 Swift 不断演进，Swift 6 引入了严格的并发机制。

# INSTALL

```brew: brew install swift```

```nix: nix profile install nixpkgs#swift```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swiftc](/man/swiftc)(1), [xcodebuild](/man/xcodebuild)(1), [vapor](/man/vapor)(1)
