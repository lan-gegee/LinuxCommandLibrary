# TAGLINE

全栈 JavaScript 框架

# TLDR

**创建新项目**

```meteor create [project-name]```

**运行开发服务器**

```meteor```

**添加软件包**

```meteor add [package-name]```

**移除软件包**

```meteor remove [package-name]```

**为生产环境构建**

```meteor build [output-dir]```

**部署到 Galaxy**

```meteor deploy [app.meteorapp.com]```

# SYNOPSIS

**meteor** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Meteor 命令。

**create** _NAME_
> 创建新项目。

**add** _PKG_
> 添加软件包。

**remove** _PKG_
> 移除软件包。

**build** _DIR_
> 为生产环境构建。

**deploy** _HOST_
> 部署应用。

**--help**
> 显示帮助信息。

# DESCRIPTION

**meteor** 是 **Meteor.js** 全栈 JavaScript 框架的命令行驱动工具。在项目目录中运行 **meteor** 会将客户端、服务器和数据库脚本打包在一起，启动本地 MongoDB 实例，监视源码树的变更，并以热代码重载的方式向已连接的客户端提供应用服务。

除开发服务器外，该 CLI 还可以引导新项目（**meteor create**）、安装 Atmosphere 或 npm 软件包（**meteor add**、**meteor npm install**）、生成用于部署的特定架构 bundle（**meteor build**），以及将应用推送到 Meteor 托管的 **Galaxy** 平台（**meteor deploy**）。底层是一个响应式数据层（DDP），通过 WebSocket 在服务器端 MongoDB 集合与客户端 Minimongo 缓存之间同步文档。

# CAVEATS

基于 Node.js；现代版本要求 Node 14 或更高。MongoDB 是唯一的一等数据库，外部 SQL 存储需通过社区包访问。其响应式模型（Tracker、publications、subscriptions）有学习曲线，且在大规模场景下可能成为性能瓶颈。

# HISTORY

**Meteor** 由 **Meteor Development Group** 于 **2012 年**推出，并于 **2014 年**发布 **1.0**。2022 年项目移交至 **Tiny**，开发工作与 Meteor 的 Galaxy 托管服务一同继续进行。

# INSTALL

```nix: nix profile install nixpkgs#meteor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [mongod](/man/mongod)(1)
