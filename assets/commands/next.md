# TAGLINE

Next.js 命令行界面

# TLDR

**创建新的 Next.js 应用**（使用 create-next-app）

```npx create-next-app@latest [app-name]```

**启动开发服务器**

```next dev```

**构建生产版本**

```next build```

**启动生产服务器**

```next start```

**运行代码检查器**

```next lint```

**打印环境信息**用于错误报告

```next info```

**启用或禁用遥测**

```next telemetry --disable```

# SYNOPSIS

**next** [_command_] [_options_]

# PARAMETERS

**dev** [_directory_]
> 启动支持热模块替换的开发服务器。

**build** [_directory_]
> 创建优化的生产构建。

**start** [_directory_]
> 启动生产服务器（需先执行 **build**）。

**lint**
> 对项目运行 ESLint。

**info**
> 打印系统、二进制和软件包版本（用于错误报告）。

**telemetry** **--enable** | **--disable**
> 启用或禁用匿名遥测。

**-p**, **--port** _port_
> 监听端口（默认：3000）。适用于 **dev** 和 **start**。

**-H**, **--hostname** _host_
> 要绑定的主机名（默认：0.0.0.0）。

**--turbopack**
> 强制启用 Turbopack（近期版本中的默认值）。

**--webpack**
> 使用 Webpack 而非 Turbopack。

**--experimental-https**
> 使用自签名证书通过 HTTPS 提供 **dev** 服务。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示 Next.js 版本。

# DESCRIPTION

**next** 是 Next.js 的命令行界面，用于开发、构建和运行 React 应用。它开箱即用地提供基于文件的路由、服务端渲染、静态生成以及 API 路由。

不带命令运行 **next** 等同于 **next dev**。配置位于 **next.config.js**（或 **.mjs**/**.ts**）。从 Next 13 开始，默认输出目录为 **.next**。

# CAVEATS

需要 Node.js。独立的 **next export** 命令已在 Next.js 14 中移除，改用 **next.config.js** 中的 `output: 'export'`。从 Next.js 15.5 起，作为 **next build** 一部分的代码检查功能正在逐步淘汰。

# HISTORY

Next.js 由 **Vercel**（当时名为 ZEIT）创建，于 **2016 年**发布，是一款面向生产应用的 React 框架。后续版本引入了 App Router、React Server Components 和 Turbopack。

# INSTALL

```apk: sudo apk add mmh```

```nix: nix profile install nixpkgs#mmh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [vercel](/man/vercel)(1), [node](/man/node)(1)
