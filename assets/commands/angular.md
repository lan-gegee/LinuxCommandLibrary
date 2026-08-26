# TAGLINE

用于构建 Angular Web 应用的命令行界面

# TLDR

**创建新的 Angular 工作区**和应用

```ng new [project-name]```

**启动应用服务**并支持实时重载

```ng serve```

**在指定端口上启动服务**并打开浏览器

```ng serve --port [4200] --open```

**生成新组件**

```ng generate component [component-name]```

**生成服务**

```ng generate service [service-name]```

面向生产环境**构建应用**

```ng build --configuration production```

**运行单元测试**

```ng test```

**运行端到端测试**

```ng e2e```

# SYNOPSIS

**ng** _command_ [_options_]

# PARAMETERS

**new** (alias: **n**)
> 创建新的 Angular 工作区和初始应用

**serve** (alias: **s**, **dev**)
> 构建并提供应用服务，文件变更时实时重载

**generate** (alias: **g**)
> 生成组件、服务、模块、管道、指令及其他 schematic

**build** (alias: **b**)
> 将应用编译到 dist/ 输出目录

**test** (alias: **t**)
> 使用配置好的测试运行器执行单元测试

**e2e** (alias: **e**)
> 构建、启动服务并运行端到端测试

**lint**
> 对应用代码运行 lint 工具

**add**
> 为外部库添加支持（安装并配置软件包）

**update**
> 更新工作区及其依赖

**deploy**
> 调用项目的部署构建器

**config**
> 获取或设置 angular.json 中的配置值

**cache**
> 配置和管理持久化磁盘缓存

**version** (alias: **v**)
> 显示 Angular CLI 版本信息

**analytics**
> 配置 Angular CLI 的匿名遥测设置

**completion**
> 设置 Angular CLI 的 Shell 自动补全

**run**
> 在工作区中运行 Architect 目标（如 my-project:build）

**extract-i18n**
> 从源代码提取 i18n 消息

**--help**
> 显示任意命令的帮助

**--dry-run**
> 预览变更而不写入文件

**--verbose**
> 启用详细日志输出

**--force**
> 强制覆盖已存在的文件（生成器）

# DESCRIPTION

**ng** 是 Angular 的命令行界面，Angular 是一个 Web 应用构建平台。它提供创建项目、生成代码、构建、测试和部署 Angular 应用的工具。

CLI 通过 schematic（生成样板代码的模板）自动完成常见开发任务，可为组件、服务、模块和其他 Angular 结构生成代码。**generate** 命令支持创建组件、指令、管道、服务、类、守卫、接口、枚举和模块。

项目通过 **angular.json** 进行配置，其中定义了构建目标、文件路径和环境相关设置。CLI 支持在单个工作区内管理多个项目，从而实现 monorepo 式开发。

**serve** 命令提供支持热模块替换的开发服务器，源文件变更时自动重新构建并刷新浏览器。生产构建使用 **build --configuration production**，启用预先编译、tree shaking 和压缩等优化。

# CONFIGURATION

**angular.json**
> 项目工作区配置，定义构建目标、文件路径和环境设置。

**tsconfig.json**
> Angular 项目的 TypeScript 编译器配置。

# CAVEATS

需要已安装 Node.js 和 npm。通过 **npm install -g @angular/cli** 全局安装可在系统范围内使用 ng 命令，但项目也可以使用本地安装的版本。某些命令（如 **deploy**）需要先通过 **ng add** 安装额外的软件包。

# HISTORY

Angular CLI 于 **2016 年 9 月**随 **Angular 2** 一同推出，旨在简化项目搭建和开发工作流。它取代了 TypeScript 编译、模块打包和构建优化所需的手动配置。CLI 此后经历了显著演进，每个 Angular 版本都伴随重大更新，陆续引入了差分加载、Ivy 编译和独立组件等特性。

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1), [webpack](/man/webpack)(1), [react-scripts](/man/react-scripts)(1), [vue](/man/vue)(1)
