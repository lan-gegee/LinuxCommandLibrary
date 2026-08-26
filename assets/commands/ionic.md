# TAGLINE

管理 Ionic Framework 项目的 CLI

# TLDR

**创建新应用**

```ionic start [myapp] [blank|tabs|sidemenu]```

**本地启动开发服务器**

```ionic serve```

**生产构建**

```ionic build --prod```

**添加平台**

```ionic capacitor add [ios|android]```

**在设备上运行**

```ionic capacitor run [ios|android]```

**生成组件**

```ionic generate component [name]```

# SYNOPSIS

**ionic** _command_ [_options_]

# PARAMETERS

**start** _NAME_ _TEMPLATE_
> 创建新项目。

**serve**
> 启动开发服务器。

**build**
> 构建 Web 资源。

**capacitor** _COMMAND_
> Capacitor 集成命令。

**generate** _TYPE_ _NAME_
> 生成组件、页面、服务。

**--prod**
> 生产构建。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Ionic** CLI 管理 Ionic Framework 项目。它使用 Web 技术创建混合移动应用。

该工具与 Capacitor 或 Cordova 集成以实现原生功能，并提供开发服务器、构建工具和代码生成。

# CAVEATS

需要 Node.js。原生构建需要平台 SDK。框架更新可能需要迁移代码。

# HISTORY

Ionic 由 **Drifty Co.** 于 2013 年创建，是一个用 Web 技术构建混合移动应用的框架。

# SEE ALSO

[capacitor](/man/capacitor)(1), [cordova](/man/cordova)(1), [npm](/man/npm)(1), [angular](/man/ng)(1)
