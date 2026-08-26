# TAGLINE

查找并运行 macOS 开发者工具

# TLDR

**查找开发者工具的路径**

```xcrun --find [clang]```

**运行活动开发者目录中的工具**

```xcrun [clang] [arguments]```

**列出可用的 SDK**

```xcrun --show-sdk-path --sdk [iphoneos]```

**配合指定 SDK 运行**

```xcrun --sdk [macosx] [tool] [arguments]```

**显示当前开发者目录路径**

```xcrun --show-sdk-platform-path```

**切换工具链**并运行命令

```xcrun --toolchain [XcodeDefault] [swift] --version```

**用指定设备启动模拟器**

```xcrun simctl boot "[iPhone 15]"```

**对应用进行公证**以便分发

```xcrun notarytool submit [app.zip] --apple-id [email] --team-id [TEAM_ID] --password [password]```

# SYNOPSIS

**xcrun** [_--sdk sdkname_] [_--toolchain name_] [_--find tool_] [_--run tool_] [_--show-sdk-path_] [_--log_] [_--verbose_] [_--kill-cache_] [_tool arguments ..._]

# PARAMETERS

**--sdk** _sdkname_
> 使用指定的 SDK（如 macosx、iphoneos、iphonesimulator）。

**--toolchain** _name_
> 使用指定的工具链。

**--find** _tool_
> 打印指定工具的完整路径。

**--run** _tool_
> 运行指定的工具（给出工具名时的默认行为）。

**--show-sdk-path**
> 打印所选 SDK 的路径。

**--show-sdk-version**
> 打印所选 SDK 的版本。

**--show-sdk-platform-path**
> 打印所选 SDK 的平台路径。

**--show-sdk-platform-version**
> 打印所选 SDK 的平台版本。

**--log**
> 将执行的命令打印到 stderr。

**--verbose**
> 显示详细输出。

**--no-cache**
> 不使用缓存中的工具路径。

**--kill-cache**
> 清空工具路径缓存。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**xcrun** 是 macOS 上用于定位和调用 Xcode 工具链中开发者工具的命令行实用程序。它是一个智能包装器，会根据活动的 Xcode 安装和所选 SDK 找到 **clang**、**swift**、**ld** 等工具的正确版本。

当系统安装了多个 Xcode 版本或多个 SDK 时，该工具会自动选择合适的工具版本，从而化解其中的复杂性。它会遵循 **DEVELOPER_DIR** 环境变量以及 **xcode-select** 的设置，因此对于需要一致工具解析的构建脚本和 CI/CD 流水线来说必不可少。

除了简单的工具调用之外，xcrun 还提供了许多强大的子命令，例如用于 iOS 模拟器管理的 **simctl**、用于应用公证的 **notarytool**、用于 App Store 上传的 **altool**，以及用于附加公证票据的 **stapler**。

# CAVEATS

仅在安装了 Xcode 或 Command Line Tools 的 macOS 上可用。如果未配置有效的开发者目录，工具解析将失败（用 **xcode-select --install** 修复）。Xcode 更新后缓存的路径可能失效；使用 **--kill-cache** 刷新。某些工具需要完整的 Xcode 安装，仅有 Command Line Tools 不够。

# HISTORY

**xcrun** 由 Apple 在开发者工具被整合进 Xcode 应用包的过程中引入。自约 **2011 年**的 **Xcode 4** 起，它成为调用命令行开发者工具的标准方式，取代了此前位于 /usr/bin 中工具的直接路径。这种架构允许多个 Xcode 版本共存，并使工具能够随其所属的 Xcode 发布版本一起更新。

# SEE ALSO

[xcode-select](/man/xcode-select)(1), [xcodebuild](/man/xcodebuild)(1), [clang](/man/clang)(1), [swift](/man/swift)(1), [simctl](/man/simctl)(1)
