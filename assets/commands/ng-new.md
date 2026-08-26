# TAGLINE

创建新的 Angular 工作区并生成初始应用

# TLDR

**创建新的 Angular 工作区**

```ng new [my-app]```

**跳过交互提示创建**，使用默认值

```ng new [my-app] --defaults```

**创建时启用路由**

```ng new [my-app] --routing```

**以指定样式格式创建**

```ng new [my-app] --style [scss|sass|less|css]```

**创建时不初始化 git 仓库**

```ng new [my-app] --skip-git```

**创建时不安装依赖**

```ng new [my-app] --skip-install```

**以 standalone 方式创建**不依赖 NgModules 的应用

```ng new [my-app] --standalone```

**以试运行模式创建**，预览将要发生的变更

```ng new [my-app] --dry-run```

# SYNOPSIS

**ng** **new** [_name_] [_options_]

# PARAMETERS

_NAME_
> 新工作区和初始项目的名称。

**--routing**
> 为初始项目生成路由模块。

**--style** _STYLE_
> 样式文件的扩展名（css、scss、sass、less）。

**--skip-git**
> 不初始化 git 仓库。

**--skip-install**
> 不安装依赖软件包。

**--skip-tests**
> 不为初始项目生成 spec 文件。

**--standalone**
> 基于 standalone API 创建应用，不使用 NgModules（Angular 17 起为默认行为）。

**--defaults**
> 禁用交互提示，改用默认值。

**--dry-run**
> 试运行，不做实际修改（预览模式）。

**--prefix** _PREFIX_
> 生成选择器时使用的前缀（默认：app）。

**--package-manager** _PM_
> 要使用的包管理器（npm、yarn、pnpm、cnpm）。

**--directory** _DIR_
> 用于创建工作区的目录。

**--inline-style**
> 把样式内联写在组件 TS 文件中。

**--inline-template**
> 把模板内联写在组件 TS 文件中。

**--view-encapsulation** _MODE_
> 视图封装策略（Emulated、None、ShadowDom）。

**--ssr**
> 为服务端渲染（SSR）配置应用。

**--create-application**
> 设为 false 时，创建不含初始应用的空工作区。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng new** 创建一个新的 Angular 工作区并生成初始应用。它会搭建完整的项目结构，包括配置文件、源码目录，并可选择性地安装 npm 依赖。

该命令会设置 TypeScript 配置、angular.json 中的 Angular 专属设置以及测试基础设施。生成的工作区遵循 Angular 最佳实践与惯例。

在不带 **--defaults** 标志运行时，CLI 会询问路由偏好和样式表格式。自 Angular 17 起，该命令默认生成 standalone 组件。

# CAVEATS

需要已安装 Node.js 和全局安装的 Angular CLI（**npm install -g @angular/cli**）。工作区名称必须是有效的 npm 包名（小写、不含空格）。若完整安装所有依赖，创建大型工作区可能需要几分钟，具体取决于网络速度。

# HISTORY

**ng new** 自 **2016 年** Angular CLI 首次发布起就是其中一员。它随 Angular 一同演进：Angular 4 引入路由选项，Angular 10 引入严格模式，Angular 17 引入 SSR 项目脚手架。自 Angular 17 起，该命令默认生成 standalone 组件。

# SEE ALSO

[ng](/man/ng)(1), [ng-generate](/man/ng-generate)(1), [ng-serve](/man/ng-serve)(1), [ng-build](/man/ng-build)(1)
