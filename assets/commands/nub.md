# TAGLINE

增强 Node.js 的一体化工具集

# TLDR

**运行** TypeScript 或 JavaScript 文件（自动转译）

```nub [file.ts]```

**运行**文件并在文件变化时重启

```nub watch [file.ts]```

**执行** package.json 中的 npm 脚本

```nub run [script]```

**执行**软件包二进制文件（更快的 npx 替代品）

```nubx [command]```

**安装**所有项目依赖

```nub install```

向项目**添加**软件包

```nub add [package]```

**安装**并切换到特定的 Node.js 版本

```nub node install [version]```

将 Nub 自身**更新**到最新版本

```nub upgrade```

# SYNOPSIS

**nub** [_options_] _file_

**nub** _subcommand_ [_arguments_]

**nubx** [_options_] _command_

# DESCRIPTION

**Nub** 是一个快速的增强型一体化工具集，它增强而不是取代 Node.js。它使用 **Rust** 编写，内置 oxc 解析器进行转译，通过单一命令打包了文件运行器、脚本运行器、包管理器、包执行器和 Node.js 版本管理器。

与其他替代运行时不同，Nub 不自带 JavaScript 引擎。它在现有的 Node.js 安装上运行文件，同时增加原生 TypeScript 执行、自动 **.env** 加载和 watch 模式。文件运行器的目标是成为 **node** 二进制文件的直接替代品，通过透传接受相同的标志和环境变量。

配套的 **nubx** 命令可以运行来自 registry 或本地 **node_modules/.bin** 的包二进制文件，是 **npx** 更快的替代品。包管理器子命令（install、ci、add、remove、update）提供了 **npm**、**pnpm** 和 **yarn** 之外的另一种选择，而 **nub node** 和 **nub pm** 则管理 Node.js 版本以及 Corepack 风格的包管理器垫片。

# PARAMETERS

**nub** _file_
> 运行 TypeScript 或 JavaScript 文件，支持自动转译和 .env 加载。

**nub run** _script_
> 执行 package.json 文件中定义的脚本。

**nub watch** _file_
> 运行文件并在源文件变化时自动重启。

**nubx** _command_
> 执行来自 registry 或本地 node_modules/.bin 的包二进制文件。

**nub install**
> 安装所有项目依赖。

**nub ci**
> 干净地安装依赖。

**nub add** _packages_
> 向项目添加一个或多个软件包。

**nub remove** _package_
> 从项目中移除软件包。

**nub update**
> 更新项目依赖。

**nub node install** _version_
> 下载并配置指定的 Node.js 版本。

**nub node ls**
> 列出已缓存的 Node.js 版本。

**nub node which**
> 打印解析到的 Node.js 二进制文件路径。

**nub pm shim**
> 注册全局包管理器垫片（Corepack 风格）。

**nub upgrade**
> 将 Nub 自身更新到最新版本。

# CAVEATS

Nub 是增强而非取代 Node.js，因此执行时仍需要可用的 Node.js 安装。作为一个年轻的项目，其命令界面和标志可能随版本变化；请查阅与你所安装版本对应的文档。

# HISTORY

Nub 于 2025 年发布，是一个基于 Rust 的 Node.js 配套工具，与 **bun** 和 **deno** 等一体化运行时定位相似，但专注于加速现有 Node.js 工作流，而不是引入独立的运行时。

# INSTALL

```aur: yay -S nub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [npx](/man/npx)(1), [pnpm](/man/pnpm)(1), [yarn](/man/yarn)(1), [bun](/man/bun)(1), [deno](/man/deno)(1)

# RESOURCES

```[Source code](https://github.com/nubjs/nub)```

```[Homepage](https://nubjs.com)```

```[Documentation](https://nubjs.com/docs)```

<!-- verified: 2026-06-25 -->
