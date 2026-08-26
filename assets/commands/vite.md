# TAGLINE

新一代前端构建工具

# TLDR

**启动开发服务器**

```vite```

**在指定端口启动开发服务器**

```vite --port [3000]```

**为生产环境构建**

```vite build```

在本地**预览生产构建**

```vite preview```

**使用指定的配置文件**

```vite --config [vite.config.js]```

**以指定的基础路径构建**

```vite build --base [/my/public/path/]```

**强制重新预打包依赖**

```vite --force```

**以指定模式构建**

```vite build --mode [production]```

# SYNOPSIS

**vite** [_command_] [_options_]

# PARAMETERS

**dev**, **serve**
> 启动开发服务器（默认命令）。

**build**
> 为生产环境构建。

**preview**
> 在本地预览生产构建。

**optimize**
> 预打包依赖。

**-c**, **--config** _file_
> 使用指定的配置文件。

**--base** _path_
> 构建的公共基础路径。

**--mode** _mode_
> 设置环境模式（development、production）。

**--port** _port_
> 开发服务器的端口号。

**--host** _host_
> 监听的主机名。

**--open** [_path_]
> 服务器启动时打开浏览器。

**--force**
> 强制重新预打包依赖。

**--clearScreen**
> 启动时清空终端屏幕。

**-l**, **--logLevel** _level_
> 日志级别：info、warn、error、silent。

**-d**, **--debug** [_filter_]
> 启用调试模式，可选过滤条件。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**Vite** 是一个新一代前端构建工具，提供极快的开发体验。它在开发阶段利用浏览器原生的 ES 模块，省去打包步骤，从而实现更快的热模块替换（HMR）。

在生产环境中，Vite 使用 Rollup 打包代码，生成优化过的静态资源。它开箱即用地支持 TypeScript、JSX、CSS 预处理器以及多种框架（Vue、React、Svelte）。

配置通常存放在 **vite.config.js** 或 **vite.config.ts** 中。Vite 要求 Node.js 20.19+ 或 22.12+。

# CAVEATS

预览服务器并非为生产环境设计；请用合适的静态文件服务器部署构建产物。开发期间部分 Node.js API 在浏览器中不可用。旧版浏览器的支持需要 @vitejs/plugin-legacy 插件。

# HISTORY

Vite 由 **Evan You**（Vue.js 的作者）创建，于 **2020 年 4 月**首次发布。其名字在法语中意为“快”。**2021 年 2 月**发布的 Vite 2.0 是一次重大重写，使其与框架无关。它作为 webpack 的替代方案迅速获得广泛采用，并影响了整个 JavaScript 工具生态。

# INSTALL

```apt: sudo apt install vite```

```brew: brew install vite```

```nix: nix profile install nixpkgs#vite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [webpack](/man/webpack)(1), [rollup](/man/rollup)(1), [esbuild](/man/esbuild)(1)
