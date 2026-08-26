# TAGLINE

面向 monorepo 的构建系统

# TLDR

**为项目运行某个目标**

```nx run [project]:[target]```

**构建项目**

```nx build [project]```

**测试项目**

```nx test [project]```

**为受影响的项目运行目标**

```nx affected -t [build]```

**跨多个项目运行目标**

```nx run-many -t [build] -p [project1] [project2]```

**使用插件生成器生成代码**

```nx generate @nx/react:component [name]```

**可视化项目依赖图**

```nx graph```

**更新 Nx 并迁移工作区**

```nx migrate latest```

# SYNOPSIS

**nx** [_command_] [_options_]

# PARAMETERS

**run** _PROJECT:TARGET_
> 在项目上执行特定目标。

**build** _PROJECT_
> 构建项目。

**test** _PROJECT_
> 运行项目测试。

**serve** _PROJECT_
> 在本地运行项目的开发服务器。

**lint** _PROJECT_
> 对项目运行代码检查。

**affected** **-t** _TARGET_
> 为受近期更改影响的项目运行目标。

**run-many** **-t** _TARGET_
> 跨多个项目执行目标。

**generate** _GENERATOR_
> 运行插件中的代码生成器。

**graph**
> 可视化工作区的项目依赖关系。

**migrate** _PACKAGE@VERSION_
> 更新软件包并运行自动迁移。

**list**
> 列出已安装的插件和可用能力。

**show**
> 显示工作区信息（项目、目标）。

**reset**
> 清除缓存的产物和元数据，并停止守护进程。

**format:check**
> 检查未格式化的文件。

**format:write**
> 覆写未格式化的文件。

**release**
> 编排版本发布与发布流程。

**daemon**
> 管理 Nx 后台守护进程。

**repair**
> 修复不受支持的工作区配置。

**report**
> 打印版本信息用于调试。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nx** 是一款构建系统，对 monorepo 提供一流支持并拥有强大的集成能力。它通过智能缓存、任务分发和受影响分析来优化构建和测试工作流。

Nx 支持多种框架和语言。它使用守护进程快速计算项目依赖图，并为构建产物提供本地和远程缓存。

# CAVEATS

需要 nx.json 配置文件。从 Nx 16 开始，`@nrwl/*` 插件作用域更名为 `@nx/*`。需要 Node.js。

# HISTORY

Nx 由 **Nrwl**（现 Nx）创建，旨在为 monorepo 提供智能且可扩展的构建工具。它最初专注于 Angular，随后扩展支持 React、Node 及其他框架，后来演变为通用构建系统。

# INSTALL

```brew: brew install nx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [lerna](/man/lerna)(1), [turbo](/man/turbo)(1)
