# TAGLINE

用 Web 代码构建跨平台移动应用

# TLDR

在项目中**初始化 Capacitor**

```npx cap init [appName] [appId]```

为项目**添加平台**

```npx cap add [android|ios]```

将 **Web 资源同步**到原生项目

```npx cap sync```

**同步指定平台**

```npx cap sync [android|ios]```

只**复制 Web 资源**，不更新原生插件

```npx cap copy```

**打开平台对应的原生 IDE**

```npx cap open [android|ios]```

在设备或模拟器上**构建并运行**

```npx cap run [android|ios]```

**检查系统配置**并诊断问题

```npx cap doctor```

# SYNOPSIS

**npx cap** [**-V**] [**-h**] [_COMMAND_]

# PARAMETERS

**-V**, **--version**
> 显示版本号。

**-h**, **--help**
> 显示用法信息。可用于单个命令。

# COMMANDS

**init** _appName_ _appId_
> 初始化新的 Capacitor 项目并生成配置文件。

**add** _platform_
> 添加原生平台支持（android 或 ios）。

**sync** [_platform_]
> 复制 Web 资源并更新原生插件。相当于同时运行 copy 和 update。

**copy** [_platform_]
> 将 Web 资源复制到原生项目，不更新插件。

**update** [_platform_]
> 更新原生插件和依赖。

**open** _platform_
> 打开该平台的原生 IDE（Android Studio 或 Xcode）。

**run** _platform_
> 在设备或模拟器上构建并运行应用。

**build** _platform_
> 构建原生项目。

**ls**
> 列出已安装的 Capacitor 插件和平台。

**doctor**
> 检查系统配置并诊断常见问题。

**migrate**
> 在 Capacitor 版本之间迁移项目。

# DESCRIPTION

**Capacitor** 是 Ionic 出品的开源原生运行时，用于以 Web 技术（JavaScript、HTML、CSS）构建跨平台移动应用。它让 Web 开发者能够用单一代码库创建原生 iOS、Android 应用以及渐进式 Web 应用（PWA）。

Capacitor CLI 管理原生项目的完整生命周期，包括初始化、平台管理、资源同步和构建。与 Cordova 不同，Capacitor 直接采用原生项目配置的方式，让开发者可以直接使用原生 IDE 和构建系统。

Web 资源先单独构建（可使用任何 Web 框架），然后通过 **cap sync** 复制到原生项目中。原生功能通过 Capacitor 插件访问，插件在 JavaScript 与原生 iOS/Android API 之间架起桥梁。

# CONFIGURATION

**capacitor.config.ts**（或 **capacitor.config.json**）
> 项目级 Capacitor 配置，包括应用 ID、应用名称、Web 目录和各平台特定设置。

# CAVEATS

需要 Node.js 和 npm。iOS 开发需要配备 Xcode 的 macOS。Android 开发必须安装 Android Studio 和 Android SDK。CLI 通常通过 **npx** 运行而非全局安装，以确保各项目间版本一致。

# HISTORY

Capacitor 由 Ionic 团队创建，于 **2019** 年首次发布，作为 Apache Cordova 的现代替代品。它旨在通过更好的原生项目集成、改进的插件生态和对渐进式 Web 应用的支持来解决 Cordova 的局限。该项目已成为 Ionic Framework 应用的推荐运行时，也可与任何 Web 框架搭配使用。

# SEE ALSO

[ionic](/man/ionic)(1), [npm](/man/npm)(1), [npx](/man/npx)(1), [cordova](/man/cordova)(1)

# RESOURCES

```[Source code](https://github.com/ionic-team/capacitor)```

```[Homepage](https://capacitorjs.com/)```

<!-- verified: 2026-06-22 -->
