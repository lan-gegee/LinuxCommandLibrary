# TAGLINE

JavaScript 静态模块打包器

# TLDR

使用默认配置**构建项目**

```webpack```

**使用指定配置文件**构建

```webpack --config [webpack.config.js]```

**面向生产环境**构建

```webpack --mode production```

**面向开发环境**构建

```webpack --mode development```

**监视变更**并重新构建

```webpack --watch```

**指定输出目录**

```webpack --output-path [path/to/dist]```

**启动开发服务器**

```webpack serve```

**显示构建统计信息**

```webpack --stats verbose```

# SYNOPSIS

**webpack** [_command_] [_entries..._] [_options_]

# PARAMETERS

**build**, **bundle**, **b**
> 运行 webpack 打包项目（默认命令）。

**serve**, **server**, **s**
> 运行 webpack 开发服务器。

**watch**, **w**
> 运行 webpack 并监视文件变化。

**init**, **create**, **c**
> 初始化新的 webpack 项目。

**info**, **i**
> 输出系统相关信息。

**configtest**, **t**
> 校验 webpack 配置文件。

**-c**, **--config** _file_
> webpack 配置文件的路径。

**--config-name** _name_
> 要使用的配置名称。

**-m**, **--merge**
> 合并多个配置。

**--mode** _mode_
> 设置模式：**production**、**development** 或 **none**。

**-o**, **--output-path** _path_
> 输出目录（绝对路径）。

**-w**, **--watch**
> 监视模式，文件变化时重新构建。

**--env** _value_
> 传递给配置函数的环境变量。

**--stats** _preset_
> 统计输出级别：errors-only、minimal、normal、verbose。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**webpack** 是一款面向现代 JavaScript 应用的静态模块打包器。它从入口点构建依赖图，并将模块打包成针对浏览器优化的输出文件。

CLI 由 **webpack-cli** 提供，封装了 webpack 的配置选项。大多数选项既可以通过命令行指定，也可以写在 **webpack.config.js** 中。命令行选项优先于配置文件设置。

webpack 支持代码分割、懒加载、tree shaking，以及用于处理不同文件类型（CSS、图片、TypeScript 等）的各种 loader 和插件。

# CAVEATS

webpack-cli 必须与 webpack 核心分开安装（**npm install webpack webpack-cli**）。开发服务器（**webpack serve**）需要 webpack-dev-server。复杂的配置更适合放在配置文件中维护，而不是通过命令行参数传递。

# HISTORY

webpack 由 **Tobias Koppers** 创建，首次发布于 **2012 年 3 月**。它引入了代码分割和热模块替换等概念，革新了 JavaScript 构建工具生态。webpack 4（2018 年）聚焦零配置默认值，webpack 5（2020 年）改进了构建性能并加入 module federation。自 webpack 4 起，CLI 被拆分为独立的 webpack-cli。

# INSTALL

```brew: brew install webpack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [vite](/man/vite)(1), [rollup](/man/rollup)(1), [esbuild](/man/esbuild)(1), [parcel](/man/parcel)(1)
