# TAGLINE

Haskell 类型安全的 Web 框架 CLI

# TLDR

**创建项目**

```yesod init```

**运行开发服务器**

```yesod devel```

**添加 handler**

```yesod add-handler [HandlerName]```

**生成 Keter 部署包**

```yesod keter```

# SYNOPSIS

**yesod** _command_ [_options_]

# PARAMETERS

**init**
> 以交互方式搭建一个新的 Yesod 项目骨架。

**devel**
> 运行开发服务器，文件变化时自动重新编译。

**add-handler**
> 生成带有样板代码的新路由 handler。

**keter**
> 构建 Keter 部署包（.keter 归档）。

**test**
> 运行项目的测试套件。

**version**
> 显示 yesod-bin 的版本信息。

**-v, --verbose**
> 启用详细输出。

**--help**
> 显示用法信息。

# DESCRIPTION

**yesod** 是 Yesod Web 框架的命令行工具。该框架用于在 Haskell 中构建类型安全的 Web 应用。它提供项目脚手架、开发服务器管理和部署打包功能。

**init** 命令会创建一个新项目，包含完整的目录结构、配置和依赖。**devel** 子命令启动的开发服务器会监视文件变化并自动重新编译，在开发过程中提供实时重载。

可以使用 **add-handler** 添加路由 handler，它会按照 Yesod 约定生成样板代码。**keter** 命令将应用打包成部署包，供 Keter Web 应用部署系统使用。

# CAVEATS

需要 Haskell 知识。需要 Stack/Cabal。有学习曲线。

# HISTORY

**Yesod** 由 **Michael Snoyman** 创建，是一个类型安全的 Haskell Web 框架。

# INSTALL

```apt: sudo apt install yesod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stack](/man/stack)(1), [cabal](/man/cabal)(1), [ghc](/man/ghc)(1)
