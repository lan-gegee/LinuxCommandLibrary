# TAGLINE

Vue.js 项目管理 CLI

# TLDR

**创建新项目**

```vue create [project-name]```

**使用预设创建**

```vue create -p [preset] [project-name]```

**启动 GUI**

```vue ui```

**添加插件**

```vue add [plugin]```

**调用生成器**

```vue invoke [plugin]```

**查看 webpack 配置**

```vue inspect```

**运行单文件服务**

```vue serve [App.vue]```

**构建单文件**

```vue build [App.vue]```

# SYNOPSIS

**vue** _command_ [_options_] [_args_]

# PARAMETERS

**create** _NAME_
> 创建项目。

**ui**
> 打开 GUI。

**add** _PLUGIN_
> 添加插件。

**invoke** _PLUGIN_
> 运行生成器。

**inspect**
> 显示 webpack 配置。

**serve** _FILE_
> 开发服务器。

**build** _FILE_
> 构建文件。

**-p**, **--preset** _NAME_
> 项目预设。

**-d**, **--default**
> 使用默认预设。

# DESCRIPTION

**vue** 是 Vue CLI 的命令行界面，提供创建、配置和管理 Vue.js 应用项目的工具。它通过交互式提示或已保存的预设来搭建新项目，并自动配置构建工具、代码检查、测试以及其他开发基础设施。

该 CLI 包含一个可通过 `vue ui` 访问的图形界面，可在浏览器中可视化管理项目、插件、依赖和构建任务。可以向现有项目添加插件，以集成 Vue Router、Vuex 状态管理、TypeScript 支持和测试框架等功能。

为了快速原型开发，`vue serve` 和 `vue build` 可以编译单个 Vue 单文件组件，而无需完整的项目设置。`vue inspect` 命令会显示解析后的 webpack 配置，有助于调试构建问题。

# CAVEATS

Vue CLI 对 Vue 2/3 项目处于维护模式。新的 Vue 3 项目建议使用 **create-vue**（基于 Vite）作为脚手架工具。要求 Node.js 8.9 或更高版本（建议 Node.js 10+）。

# HISTORY

**Vue CLI** 由 **Evan You** 创建，用于 Vue.js 项目管理。3+ 版本提供了基于插件的架构。

# INSTALL

```nix: nix profile install nixpkgs#vue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [vite](/man/vite)(1), [node](/man/node)(1), [vue-serve](/man/vue-serve)(1), [yarn](/man/yarn)(1)
