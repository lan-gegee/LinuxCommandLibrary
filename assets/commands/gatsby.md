# TAGLINE

基于 React 的静态网站生成器

# TLDR

**创建新站点**

```gatsby new [site-name]```

**从 starter 创建**

```gatsby new [site-name] [https://github.com/user/starter]```

**启动开发服务器**

```gatsby develop```

**构建生产版本**

```gatsby build```

**运行生产构建**

```gatsby serve```

**清理缓存**

```gatsby clean```

**显示信息**

```gatsby info```

# SYNOPSIS

**gatsby** _command_ [_options_]

# SUBCOMMANDS

**new**
> 创建新站点。

**develop**
> 启动开发服务器。

**build**
> 构建生产站点。

**serve**
> 运行生产构建。

**clean**
> 清理缓存和构建产物。

**info**
> 显示环境信息。

**repl**
> 交互式 REPL。

# PARAMETERS

**-H**, **--host** _host_
> 为 develop/serve 设置主机（默认：localhost）。

**-p**, **--port** _port_
> 为 develop/serve 设置端口（develop 默认 8000，serve 默认 9000）。

**-o**, **--open**
> 在默认浏览器中打开站点。

**-S**, **--https**
> 为开发服务器启用 HTTPS。

**--inspect**
> 打开 Node.js inspector 的调试端口。

**--prefix-paths**
> 以路径前缀构建/运行（需要在 gatsby-config 中配置 pathPrefix）。

**--no-uglify**
> 构建时不压缩 JS bundle（用于调试）。

**--profile**
> 构建期间启用 React 性能分析。

**--verbose**
> 开启详细输出。

**-C**, **--clipboard**
> 将环境信息复制到剪贴板（gatsby info）。

# CONFIGURATION

**gatsby-config.js**（或 **gatsby-config.ts**）
> 主配置文件，定义插件、站点元数据和构建设置。

**gatsby-node.js**（或 **gatsby-node.ts**）
> Node API 配置，用于动态页面创建和构建期定制。

# DESCRIPTION

**gatsby** 是一个基于 React 的静态网站生成器，使用 React 组件和 GraphQL 获取数据，构建快速优化的网站。它将现代 Web 技术与自动代码分割、图片优化和渐进增强相结合。

Gatsby 在构建时生成静态 HTML，同时通过 hydration 保持 React 的交互能力。该框架拥有丰富的插件生态，可集成 CMS、API 和各类服务。GraphQL 提供统一的数据层，可从多个来源查询内容。

开发服务器内置热模块替换，支持快速迭代；生产构建则通过预取、懒加载和资源优化等技术针对性能做了优化。

# CAVEATS

大型站点构建可能较慢。GraphQL 层有学习曲线。某些插件可能已过时。实时数据需要客户端获取。依赖 Node.js 和 npm。

# HISTORY

Gatsby 由 **Kyle Mathews** 于 **2015 年**创建，是一款现代静态网站生成器。它因结合 React 与 GraphQL 而广受欢迎，并于 **2023 年 2 月**被 **Netlify** 收购。该框架推动了 Jamstack 架构的普及。**2022 年 11 月**发布的 Gatsby 5 引入了 Slice API 和部分水合（partial hydration）。

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1), [hugo](/man/hugo)(1)
