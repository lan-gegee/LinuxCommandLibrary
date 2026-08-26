# TAGLINE

一体化的 JavaScript 运行时和工具链

# TLDR

**运行** JavaScript 文件

```bun [script.js]```

**安装**依赖

```bun install```

**添加**软件包

```bun add [react]```

**运行** package.json 中的脚本

```bun run [dev]```

**创建**新项目

```bun create [react] [my-app]```

**测试**文件

```bun test```

# SYNOPSIS

**bun** _command_ [_options_]

# DESCRIPTION

**bun** 是一个集 JavaScript 运行时、包管理器、打包器和测试运行器于一体的工具。它被设计为 Node.js 的即插即用替代品，启动时间和软件包安装速度都显著更快。

该工具以性能为优先，目标是成为 JavaScript/TypeScript 开发的完整工具链。

# PARAMETERS

**run** _file_
> 执行 JavaScript/TypeScript 文件

**install**
> 从 package.json 安装依赖

**add** _package_
> 将软件包添加到依赖中

**remove** _package_
> 移除软件包

**test**
> 运行测试

**build** _file_
> 为生产环境打包

**create** _template_
> 创建新项目

**upgrade**
> 升级 Bun 本身

# FEATURES

- 快速的 JavaScript 运行时（使用 JavaScriptCore）
- 内置 TypeScript 支持
- 包管理器（与 npm 兼容）
- 打包器（与 esbuild 兼容）
- 测试运行器
- 原生 Web API
- 热重载
- SQLite 支持

# PERFORMANCE

- npm install 快 4 倍
- 脚本执行比 Node.js 快 2-3 倍
- 近乎即时的启动

# WORKFLOW

```bash
# Create project
bun create react my-app
cd my-app

# Install deps
bun install

# Run dev server
bun run dev

# Add package
bun add tailwindcss

# Run tests
bun test

# Build for production
bun build ./src/index.ts --outdir ./dist
```

# COMPATIBILITY

- 可直接替换 Node.js（大多数 API）
- npm 软件包生态
- Jest 兼容的测试运行器
- 支持 ESM 和 CommonJS

# CONFIGURATION

**bunfig.toml**
> Bun 的项目级和全局配置文件。控制软件包安装行为、运行时设置、测试运行器选项以及打包器默认值。在项目根目录中查找，或全局使用 ~/.bunfig.toml。

# CAVEATS

并非 100% 兼容 Node.js。某些原生模块无法工作。并非所有 npm 软件包都经过测试。自 v1.1（2024 年 4 月）起原生支持 Windows。

# HISTORY

**Bun** 由 Jarred Sumner 创建，于 **2021 年**首次发布，是一个基于 Zig 和 JavaScriptCore 构建的快速一体化 JavaScript 工具链。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [deno](/man/deno)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
