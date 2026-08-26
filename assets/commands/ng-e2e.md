# TAGLINE

为 Angular 应用运行端到端测试

# TLDR

**运行端到端测试**

```ng e2e```

**为特定项目运行 e2e 测试**

```ng e2e [project-name]```

**使用指定配置运行 e2e 测试**

```ng e2e --configuration production```

**在指定端口上运行 e2e 测试**

```ng e2e --port [4200]```

# SYNOPSIS

**ng e2e** [_project_] [_options_]

# PARAMETERS

_project_
> 要为其运行端到端测试的项目。默认为默认项目。

**--configuration** _name_
> 目标构建配置。

**--port** _port_
> 测试期间使用的开发服务器端口。

**--dev-server-target** _target_
> 测试所针对的开发服务器目标。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng e2e** 会构建应用、启动开发服务器，并针对它运行端到端测试。该命令要求在项目的 **angular.json** 文件中配置好 e2e 测试框架构建器（builder）。

自 Angular CLI 12 起，不再内置默认的 e2e 框架。用户必须通过 **ng add** 添加 **Cypress**、**Playwright** 或 **Nightwatch** 等测试包来提供 e2e 构建器。

# CONFIGURATION

使用此命令前必须先添加 e2e 构建器：

```ng add @cypress/schematic```
```ng add @playwright-ng/schematics```

# CAVEATS

需要先安装并配置 e2e 测试框架。Protractor 在 Angular CLI 12 中被移除出默认配置。开发服务器必须处于可用状态，测试才有目标可运行。本命令是 Angular CLI 的一部分。

# HISTORY

**ng e2e** 最初默认使用 **Protractor** 作为端到端测试框架。随着 Angular CLI **12**（**2021 年**）发布，Protractor 被弃用，该命令改为框架无关，需要用户显式安装测试构建器。

# SEE ALSO

[ng](/man/ng)(1), [ng-test](/man/ng-test)(1), [playwright](/man/playwright)(1)
