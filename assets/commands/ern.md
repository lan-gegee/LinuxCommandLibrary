# TAGLINE

面向原生应用的 React Native 集成平台

# TLDR

**创建新的 MiniApp** 项目

```ern create-miniapp [app-name]```

在 Android 上**运行 MiniApp**

```ern run-android```

在 iOS 上**运行 MiniApp**

```ern run-ios```

**创建新的 API** 模块

```ern create-api [api-name]```

向 MiniApp **添加依赖**

```ern add [dependency]```

为 MiniApp **启动开发**服务器

```ern start```

通过 CodePush **推送 OTA 更新**

```ern code-push [miniapps] -d [descriptor]```

# SYNOPSIS

**ern** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 ERN 操作。

**create-miniapp** _NAME_
> 创建新的 MiniApp 项目（等价于 react-native init）。

**run-android**
> 在 Android 模拟器或设备上运行 MiniApp。

**run-ios**
> 在 iOS 模拟器或设备上运行 MiniApp。

**create-api** _NAME_
> 创建新 API 并生成客户端代码。

**start**
> 启动 Electrode Native 开发服务器（packager）。

**add** _DEPENDENCY_
> 向 MiniApp 添加 JavaScript 或原生依赖。

**cauldron** _COMMAND_
> 管理 Cauldron（原生应用容器的版本注册表）。

**code-push** _MINIAPPS_
> 通过 CodePush 推送 OTA 更新。

**link**
> 为本地开发和调试链接 MiniApp。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ern**（Electrode React Native）是一个用于将 React Native 集成到现有原生应用中的平台。它提供一系列工具，用于在原生移动应用内构建、管理和部署 React Native "MiniApp"。

该平台包含用于版本管理的 Cauldron、将 MiniApp 与原生依赖打包在一起的容器生成机制，以及用于 React Native 与原生代码之间通信的 API。

ERN 让现有移动应用能够渐进式地采用 React Native。

# CAVEATS

需要原生开发环境（Android SDK 和/或 Xcode）。架构复杂，有学习曲线。与现有应用的集成方式不同于独立的 React Native。

# HISTORY

Electrode React Native 由 **Walmart Labs** 开发，目的是让其在现有移动应用中渐进采用 React Native，解决企业级集成的难题。

# SEE ALSO

[react-native](/man/react-native)(1), [npm](/man/npm)(1), [yarn](/man/yarn)(1), [node](/man/node)(1)
