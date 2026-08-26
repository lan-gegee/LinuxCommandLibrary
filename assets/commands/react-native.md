# TAGLINE

用 React 构建原生移动应用

# TLDR

**创建新项目**

```npx react-native init [ProjectName]```

**启动 Metro 打包器**

```npx react-native start```

**在 Android 上运行**

```npx react-native run-android```

**在 iOS 上运行**

```npx react-native run-ios```

**在指定设备上运行**

```npx react-native run-ios --device "[iPhone 15]"```

**清除构建缓存**

```npx react-native start --reset-cache```

**链接原生依赖**

```npx react-native link```

**显示 doctor 诊断**

```npx react-native doctor```

# SYNOPSIS

**npx react-native** _command_ [_options_]

# PARAMETERS

**init** _NAME_
> 创建新项目。

**start**
> 启动 Metro 打包器。

**run-android**
> 构建并在 Android 上运行。

**run-ios**
> 构建并在 iOS 上运行。

**doctor**
> 检查开发环境。

**link**
> 链接原生依赖。

**upgrade**
> 升级 React Native。

**--device** _NAME_
> 目标设备。

**--reset-cache**
> 清除打包器缓存。

# DESCRIPTION

**react-native** 是 React Native 的命令行界面。React Native 是一个可以用 JavaScript 和 React 构建原生 iOS 和 Android 移动应用的框架。它管理从项目创建到构建、运行和调试应用的完整开发生命周期，覆盖模拟器、仿真器和物理设备。

该 CLI 启动 Metro 打包器，为运行中的应用提供 JavaScript 包，并通过热重载实现快速开发迭代。平台专属命令（**run-android**、**run-ios**）会编译原生代码并部署到目标设备。**doctor** 命令检查 Xcode、Android SDK、Node.js 及所需依赖，验证开发环境配置是否正确。

# CAVEATS

iOS 开发需要 macOS。Android 需要 SDK 和仿真器。原生构建可能较慢。

# HISTORY

**React Native** 由 **Facebook** 开发，于 **2015 年**发布。它让开发者能够使用 React 和 JavaScript 构建移动应用，并编译为原生代码。

# SEE ALSO

[expo](/man/expo)(1), [npm](/man/npm)(1), [metro](/man/metro)(1)
