# TAGLINE

面向 Cocoa 项目的去中心化依赖管理器

# TLDR

**更新并构建依赖**

```carthage update```

**构建 XCFramework**

```carthage update --use-xcframeworks```

**不更新直接引导构建**

```carthage bootstrap```

**构建指定依赖**

```carthage build [dependency_name]```

**只更新不构建**

```carthage update --no-build```

**针对特定平台构建**

```carthage update --platform [iOS]```

**检查过期的依赖**

```carthage outdated```

# SYNOPSIS

**carthage** _command_ [_options_]

# DESCRIPTION

**carthage** 是面向 Swift 和 Objective-C Cocoa 项目的去中心化依赖管理器。与 CocoaPods 不同，它将依赖构建为二进制框架，而不修改你的 Xcode 工程文件、工作区或构建设置，把项目结构的完全控制权留给开发者。

依赖在 **Cartfile** 中以简单语法声明，支持 GitHub 仓库、Git URL 和仅二进制的框架。运行 `carthage update` 会解析版本、检出源码，并把框架构建到 Carthage/Build 目录。Cartfile.resolved 锁定文件可确保团队成员之间的构建可复现。

自 0.37.0 版本起，Carthage 支持构建 XCFramework，它将多个平台和架构的二进制文件打包为单个可分发包。

# COMMANDS

**update**
> 更新并重新构建依赖

**bootstrap**
> 不更新而直接构建依赖

**build**
> 构建指定依赖

**outdated**
> 检查过期的依赖

**archive**
> 创建已构建框架的归档

**copy-frameworks**
> 将框架复制到应用 bundle

**version**
> 显示版本

# PARAMETERS

**--use-xcframeworks**
> 构建为 XCFramework（推荐）

**--platform** _name_
> 针对特定平台构建（iOS、macOS、tvOS、watchOS）

**--no-build**
> 检出后跳过构建

**--no-use-binaries**
> 从源码构建，不使用预编译二进制

**--cache-builds**
> 缓存已构建的框架

**--project-directory** _path_
> 包含 Cartfile 的目录

**--verbose**
> 显示详细输出

# CARTFILE FORMAT

```
github "Alamofire/Alamofire" ~> 5.0
github "realm/realm-swift" == 10.0.0
git "https://example.com/repo.git" "branch-name"
```

# CONFIGURATION

**Cartfile**
> 以版本约束声明项目依赖。

**Cartfile.resolved**
> 记录精确解析版本的锁定文件，用于可复现构建。

**Cartfile.private**
> 仅开发和测试所需的依赖。

# CAVEATS

在 iOS 8+ 上支持动态框架。静态框架自 0.30.0 版本起受支持。新项目建议考虑 Swift Package Manager。框架会输出到 Carthage/Build 目录。

# INSTALL

```brew: brew install carthage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swift](/man/swift)(1), [xcodebuild](/man/xcodebuild)(1), [git](/man/git)(1)
