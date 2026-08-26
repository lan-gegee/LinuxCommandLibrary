# TAGLINE

用于 React Native 项目脚手架和代码生成的 CLI

# TLDR

**创建新的 React Native 应用**

```npx ignite-cli new [MyApp]```

以 Expo 工作流**创建新应用**

```npx ignite-cli new [MyApp] --workflow=expo```

**生成组件**

```npx ignite-cli generate component [Header]```

**生成屏幕**

```npx ignite-cli generate screen [Login]```

**生成模型**

```npx ignite-cli generate model [User]```

**检查环境**问题

```npx ignite-cli doctor```

从生成的项目中**移除演示代码**

```npx ignite-cli remove-demo```

# SYNOPSIS

**ignite** _command_ [_options_]

# PARAMETERS

**new** _name_
> 使用 Ignite 样板搭建新的 React Native 应用。

**generate** _type_ _name_
> 从模板生成组件、屏幕、模型或导航器。

**doctor**
> 检查本地开发环境的常见问题。

**remove-demo**
> 移除由 Ignite 生成的项目中的演示/示例代码。

**--workflow** _type_
> 创建新应用时使用的工作流：**expo**（默认）或 **cng**（Continuous Native Generation，持续原生生成）。

**--yes**, **-y**
> 创建新应用时接受所有默认选项（非交互式）。

**--help**
> 显示帮助信息。

**--version**
> 显示 CLI 版本。

# DESCRIPTION

**Ignite** 是由 **Infinite Red** 开发的 React Native 开发 CLI。它提供带有行业最佳实践的强观点（opinionated）项目脚手架，包括用于状态管理的 MobX-State-Tree、TypeScript、React Navigation 以及基于 Jest 的测试配置。

**generate** 命令根据模板为常见模式创建样板文件：组件、屏幕、模型和导航器。生成的代码遵循项目既定的约定和目录结构。

# CAVEATS

需要 React Native 和 Node.js。生成的样板带有较强的观点倾向，遵循 Infinite Red 推荐的架构。Ignite v9+ 默认采用基于 Expo 的工作流。

# HISTORY

Ignite 由 **Infinite Red** 创建，最初是一个 React Native 样板和 CLI 工具。它经历了多个主要版本的演进，从多个样板选项转向单一且持续维护的样板（先是 Ignite Bowser，后是 Ignite v9+），并聚焦于 Expo。

# INSTALL

```brew: brew install ignite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npx](/man/npx)(1), [react-native](/man/react-native)(1), [expo](/man/expo)(1), [npm](/man/npm)(1)
