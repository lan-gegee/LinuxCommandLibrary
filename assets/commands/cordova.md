# TAGLINE

混合移动应用开发框架

# TLDR

**创建新的 Cordova 项目**

```cordova create [myapp] [com.example.myapp] "[MyApp]"```

**添加平台**（iOS、Android 等）

```cordova platform add [android]```

**为所有平台构建应用**

```cordova build```

**为特定平台构建**

```cordova build [android]```

**在模拟器或设备上运行应用**

```cordova run [android]```

**添加插件**

```cordova plugin add [cordova-plugin-camera]```

**列出已安装的插件**

```cordova plugin list```

**移除平台**

```cordova platform remove [ios]```

# SYNOPSIS

**cordova** _command_ [_options_]

# PARAMETERS

**create** _DIR_ _ID_ _NAME_
> 在指定目录创建新的 Cordova 项目。

**platform add** _PLATFORM_
> 添加平台（android、ios、browser、electron）。

**platform remove** _PLATFORM_
> 从项目中移除平台。

**build** [_PLATFORM_]
> 为指定平台或所有平台构建应用。

**run** [_PLATFORM_]
> 在设备或模拟器上运行应用。

**emulate** _PLATFORM_
> 在平台模拟器中运行应用。

**plugin add** _PLUGIN_
> 向项目添加插件。

**plugin remove** _PLUGIN_
> 从项目中移除插件。

**plugin list**
> 列出已安装的插件。

**prepare**
> 将文件复制到各平台目录以备构建。

**--release**
> 以 release 模式构建。

**--device**
> 部署到已连接的设备而非模拟器。

# DESCRIPTION

**Apache Cordova** 是一个移动应用开发框架，允许使用 HTML、CSS 和 JavaScript 构建面向多个平台的应用。CLI 负责管理项目创建、平台配置、插件安装和应用构建。

Cordova 将 Web 应用封装在原生容器中，并通过 JavaScript API 提供对设备功能的访问。插件弥合了 Web 代码与原生功能之间的鸿沟，例如相机、GPS、联系人和文件系统访问。

典型工作流是：创建项目、添加目标平台、安装所需插件、在 **www** 目录中开发 Web 应用，然后使用 build/run 命令在设备或模拟器上进行测试。

# CAVEATS

各平台 SDK 需要单独安装（Android SDK、iOS 需要 Xcode）。iOS 开发需要 macOS。某些插件可能存在平台相关的限制。对于计算密集型任务，性能可能不及完全原生的应用。

# HISTORY

Cordova 源自 **PhoneGap**，由 Nitobi Software 于 **2009** 年创建。Adobe 在 **2011** 年收购 Nitobi 后，将代码库捐赠给 Apache 软件基金会，并更名为 Cordova。它至今仍是最广泛使用的混合移动开发框架之一。

# INSTALL

```pacman: sudo pacman -S cordova```

```nix: nix profile install nixpkgs#cordova```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ionic](/man/ionic)(1), [npm](/man/npm)(1)
