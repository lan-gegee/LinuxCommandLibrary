# TAGLINE

Ember.js 框架的命令行界面

# TLDR

**创建新的 Ember** 应用

```ember new [app-name]```

**生成组件**

```ember generate component [component-name]```

**启动开发**服务器

```ember serve```

**为生产环境构建**

```ember build --environment production```

**运行测试**

```ember test```

**安装插件**

```ember install [addon-name]```

# SYNOPSIS

**ember** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Ember CLI 命令：new、generate、serve、build、test、install。

**new** _NAME_
> 创建新应用。

**generate** _TYPE_ _NAME_
> 生成蓝图（组件、路由等）。

**serve**, **s**
> 启动开发服务器。

**build**, **b**
> 构建应用。

**test**, **t**
> 运行测试套件。

**install** _ADDON_
> 安装 Ember 插件（addon）。

**--help**
> 显示帮助信息。

# CONFIGURATION

**.ember-cli**
> 项目专属的 Ember CLI 配置文件。

**config/environment.js**
> 应用的主要配置文件，包括 API 端点、功能开关以及各环境专属设置。

# DESCRIPTION

**ember** 是 Ember.js 的命令行界面。Ember.js 是一个用于构建大型 Web 应用的 JavaScript 框架，该 CLI 负责项目脚手架搭建、开发、构建和测试。

CLI 提供生成器，可按照约定创建组件、路由、服务及其他 Ember 构造。开发服务器支持实时刷新。

Ember CLI 管理依赖、构建配置和插件安装，提供完整的开发工作流。

# CAVEATS

需要 Node.js 和 npm。初始项目体积较大。高度依赖约定的方式有一定学习曲线。部分插件可能已无人维护。

# HISTORY

Ember CLI 的诞生是为了给 Ember.js 开发提供标准化的工具链。Ember.js 本身由 **Yehuda Katz**（也因 jQuery 和 Rust 的 Cargo 而知名）与 **Tom Dale** 创建，于 **2011 年**发布。

# INSTALL

```aur: yay -S ember```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1), [angular](/man/angular)(1)

# RESOURCES

```[Source code](https://github.com/ember-cli/ember-cli)```

```[Homepage](https://emberjs.com/)```

```[Documentation](https://cli.emberjs.com/release/)```

<!-- verified: 2026-07-14 -->
