# TAGLINE

Flutter UI 框架的命令行工具

# TLDR

**创建新项目**

```flutter create [app_name]```

**以调试方式运行应用**

```flutter run```

**构建发布版 APK**

```flutter build apk```

**获取依赖**

```flutter pub get```

**运行测试**

```flutter test```

# SYNOPSIS

**flutter** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：create、run、build、test、pub 等。

**create** _NAME_
> 创建新的 Flutter 项目。

**run**
> 在设备/模拟器上运行应用。

**build** _TARGET_
> 构建应用（apk、ios、web）。

**test**
> 运行单元测试和组件测试。

**pub** _SUBCMD_
> 软件包管理。

**doctor**
> 检查环境配置。

**devices**
> 列出已连接的设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flutter** 是驱动 Flutter UI 框架的命令行工具。它可以搭建项目脚手架、通过 **pub** 管理软件包依赖、为每个受支持的平台执行构建，并协调整个开发循环，包括 **flutter run** 期间的热重载和热重启。

单一的 Dart 代码库可编译为 **iOS**、**Android**、**macOS**、**Linux** 和 **Windows** 的原生二进制文件，以及面向 Web 的 JavaScript/WebAssembly。**doctor** 子命令会检查宿主机器并报告缺失的前置条件，例如 Android SDK、Xcode、命令行工具以及相应的设备模拟器。**flutter devices** 列出当前连接或运行中、可供 **flutter run** 部署的目标设备。

# CAVEATS

每个目标平台都要求宿主机上有对应的原生 SDK：Android 需要 Android SDK 和 JDK，iOS/macOS 需要 Xcode 和 CocoaPods，Windows 需要 Visual Studio，Linux 需要 GTK/clang。初次切换频道（**flutter channel stable | beta | master**）会触发大量下载。**flutter upgrade** 只更新当前频道；降级通常需要 **flutter downgrade** 或重新检出特定的标签。

# HISTORY

**Flutter** 由 **Google** 在 I/O **2017** 上发布，并于 **2018 年 12 月**达到 **1.0**。该框架使用自己的 GPU 加速渲染引擎（最初是 Skia，现在还包括 Impeller），而非原生控件工具包，这正是它能在各平台上呈现一致外观的原因。Dart **3** 为工具链带来了健全的空安全和模式匹配。

# INSTALL

```nix: nix profile install nixpkgs#flutter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dart](/man/dart)(1), [flutter-pub](/man/flutter-pub)(1), [adb](/man/adb)(1), [xcrun](/man/xcrun)(1)
