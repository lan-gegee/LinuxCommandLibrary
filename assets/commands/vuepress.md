# TAGLINE

由 Vue 驱动的静态文档生成器

# TLDR

**启动开发服务器**

```vuepress dev [docs]```

**构建静态网站**用于生产环境

```vuepress build [docs]```

**在指定端口启动开发服务器**

```vuepress dev [docs] --port [3000]```

**带调试输出构建**

```vuepress build [docs] --debug```

**构建到自定义输出目录**

```vuepress build [docs] --dest [dist]```

**显示环境信息**

```vuepress info```

# SYNOPSIS

**vuepress** _command_ [_sourceDir_] [_options_]

# PARAMETERS

**dev** [_sourceDir_]
> 启动带热更新的开发服务器。默认目标为当前目录。

**build** [_sourceDir_]
> 将网站构建为静态 HTML 文件以便部署。

**info**
> 显示系统和依赖信息。

**-c**, **--config** _file_
> 设置配置文件的路径。

**-p**, **--port** _port_
> 指定开发服务器的端口（默认：8080）。仅限开发模式。

**--host** _host_
> 指定开发服务器的主机（默认：0.0.0.0）。仅限开发模式。

**-d**, **--dest** _dir_
> 设置构建的输出目录（默认：.vuepress/dist）。仅限构建时。

**-t**, **--temp** _dir_
> 设置临时文件目录。

**--cache** _dir_
> 设置缓存文件目录。

**--debug**
> 启用调试模式并输出详细信息。

**--clean-temp**
> 在开发或构建前清理临时文件。

**--clean-cache**
> 在开发或构建前清理缓存文件。

**--open**
> 就绪后打开浏览器。仅限开发模式。

**--no-watch**
> 禁用对页面和配置文件的监视。仅限开发模式。

**--help**
> 显示某个命令的帮助。

# DESCRIPTION

**VuePress** 是一个由 Vue 驱动的静态网站生成器，专为创建文档网站设计。它将 Markdown 文件编译成单页应用（SPA），同时为每个页面预渲染静态 HTML，兼具 SEO 优势和 SPA 的导航体验。

VuePress 允许在 Markdown 文件中直接使用 Vue 组件，从而实现交互式文档。它自带一个为技术文档优化的默认主题，包含侧边栏导航、搜索和自动标题锚点等功能。

开发服务器为 Markdown 内容和 Vue 组件都提供热模块更新。生产环境的构建命令会生成优化过的静态文件，可部署到任何静态托管服务。

配置通过源目录中的 .vuepress/config.js 或 .vuepress/config.ts 文件完成，可控制主题、插件、导航和站点元数据。命令行选项会覆盖配置文件中的同名设置。

# CAVEATS

要求 Node.js 18.19.0 或更高版本。VuePress v1 处于维护模式；新项目建议使用 v2 或 VitePress（其继任者）。v1 的 `eject` 命令在 v2 中不存在。大型文档网站的构建时间可能较慢。自定义主题需要 Vue.js 知识。

# HISTORY

**VuePress** 由 Vue.js 的作者 **Evan You** 于 **2018 年 4 月**创建。它最初是为了给 Vue.js 本身编写文档而开发的，但由于在技术文档领域的实用性而成为独立项目。**2022 年**发布的 VuePress v2 基于 Vue 3 重构。使用 Vite 替代 Webpack 的 **VitePress** 现在是新项目的推荐选择。

# SEE ALSO

[vitepress](/man/vitepress)(1), [vue](/man/vue)(1), [docusaurus](/man/docusaurus)(1), [mkdocs](/man/mkdocs)(1)
