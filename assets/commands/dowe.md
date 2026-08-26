# TAGLINE

面向多目标应用的全栈编译器与运行时

# TLDR

**安装** CLI（macOS/Linux）

```curl -fsSL https://get.dowe.dev/install | bash```

**初始化**空白项目

```dowe init --template blank```

以 watch 模式**开发** server 和 web 目标

```dowe dev --target server --target web```

**运行**项目测试

```dowe test```

**部署**发行版（静态、Docker 或 Cloudflare）

```dowe deploy```

**打印**已安装的版本

```dowe version```

# SYNOPSIS

**dowe** _command_ [_options_]

# DESCRIPTION

**dowe** 是 Dowe 的命令行界面。Dowe 是一个 Rust 编译器加运行时，从统一的声明式源图（**.dowe** 文件）构建全栈产品。同一个项目模型可以面向 server（Rust）、web（SSR HTML/JS/CSS）、桌面窗口、Android（Jetpack Compose）和 iOS（SwiftUI）。

Dowe Source Format 是编译器的输入，而不是 JavaScript 应用运行时：编译和运行不需要 Node.js、**node_modules**、React 及类似技术栈。编译器会在 **.dowe/** 下生成确定性的工件之前校验路由、类型和平台边界。

# COMMANDS

**init** [**--template** blank|crud] [**--i18n**]

> 脚手架生成新项目。**crud** 会加入全栈 CRUD 起步代码；**--i18n** 包含翻译目录。

**dev** [**--target** _name_]...

> 编译、监视并运行选定的开发目标。未给出标志时进入交互式目标选择。

**test**

> 发现并运行原生的 **.dowe** 字面量测试。

**deploy**

> 生成静态、Docker 或 Cloudflare 发行版。

**icons**

> 为 web、桌面、Android 和 iOS 生成带版本管理的图标集。

**agent**

> 安装或更新供编码智能体使用的公开编写指南。

**codegraph**

> 检查归属关系、依赖、模块化程度与重复代码。

**database** / **cache** / **vector**

> 管理 Dowe 数据库、缓存和向量实例及其数据。

**upgrade**

> 通过官方发布通道升级。

**version**

> 打印 CLI 版本。

# CAVEATS

早期访问阶段的工具链；目标支持和 API 可能变化。移动端生成器产出原生项目，设备构建仍需要平台 SDK（Android/iOS）。不要把 **.dowe/** 当作源码来编辑——它是生成产物。

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1)

# RESOURCES

```[Source code](https://github.com/usedowe/dowe-lang)```

```[Homepage](https://dowe.dev)```

```[Documentation](https://dowe.dev)```

<!-- verified: 2026-07-30 -->
