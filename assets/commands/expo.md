# TAGLINE

React Native 开发平台与构建工具链

# TLDR

**创建新项目**

```expo init [project-name]```

**启动开发**服务器

```expo start```

**在指定平台**上启动

```expo start --ios```

**构建生产版本**

```expo build:android```

**发布到 Expo**

```expo publish```

**登录到** Expo 账户

```expo login```

**安装软件包**

```expo install [expo-camera]```

# SYNOPSIS

**expo** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Expo CLI 命令。

**init** _NAME_
> 创建新项目。

**start**
> 启动开发服务器。

**build:android**/**build:ios**
> 为对应平台构建。

**publish**
> 发布到 Expo。

**install** _PACKAGE_
> 安装兼容版本的软件包。

**login**
> 向 Expo 进行身份验证。

**--help**
> 显示帮助信息。

# CONFIGURATION

**app.json**
> Expo 项目配置，包括应用名称、版本、SDK 版本以及平台特定设置。

**eas.json**
> 用于托管构建和部署的 EAS Build 与 Submit 配置。

# DESCRIPTION

**Expo** 是用于构建 React Native 应用程序的平台。其 CLI 提供跨平台移动应用的开发、构建和部署工具。

Expo 通过托管式工作流、预配置的原生模块和 OTA（空中下载）更新简化了 React Native 开发。Expo Go 应用让你无需原生构建即可进行测试。

该平台在云端处理 iOS 和 Android 构建，无需本地工具链。

# CAVEATS

部分原生模块在托管工作流中不可用。构建服务可能存在排队等待。eject 之后会失去部分 Expo 功能。应用体积包含 Expo 运行时。

# HISTORY

Expo 的诞生是为了简化 React Native 开发，提供托管式工作流和构建服务。它由 **Expo**（原 Exponent）维护，被广泛用于 React Native 项目。

# SEE ALSO

[react-native](/man/react-native)(1), [npm](/man/npm)(1)
