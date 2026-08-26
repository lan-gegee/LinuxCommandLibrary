# TAGLINE

基于 Vite 的静态网站生成器

# TLDR

**启动开发服务器**

```vitepress dev [docs]```

**为生产环境构建**

```vitepress build [docs]```

**预览生产构建**

```vitepress preview [docs]```

**初始化新项目**

```vitepress init```

**在当前目录启动**

```vitepress```

# SYNOPSIS

**vitepress** [_command_] [_root_] [_options_]

# COMMANDS

**dev** _root_：启动支持热更新的开发服务器。

**build** _root_：为生产环境构建静态网站。

**preview** _root_：在本地预览生产构建。

**init**：初始化新的 VitePress 项目。

# PARAMETERS

_root_
> 项目根目录（默认：当前目录）。

**--host** _host_
> 开发服务器的主机（默认：localhost）。

**--port** _port_
> 开发服务器的端口（默认：5173）。

**--base** _path_
> 公共基础路径。

**--cors**
> 启用 CORS。

**--strictPort**
> 端口被占用时退出。

**--force**
> 强制优化器忽略缓存。

**--minify**
> 启用压缩（仅限构建时）。

**--mpa**
> 多页应用模式。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**VitePress** 是一个由 Vite 和 Vue.js 驱动的静态网站生成器。它专为文档网站设计，借助热模块替换提供快速的开发体验，并能生成优化过的生产构建。

内容使用 Markdown 编写，同时支持 Vue 组件。该工具会生成对 SEO 友好的静态 HTML 页面，页面加载后再水合为单页应用。

配置通过 .vitepress/config.js 文件完成。主题可以自定义或完全替换。内置功能包括导航栏、侧边栏、搜索和深色模式。

VitePress 是 VuePress 的精神续作，基于 Vite 重构以获得更好的性能。

通过 npm 安装：`npm add -D vitepress`

# CAVEATS

要求 Node.js 18+。仅支持 Vue 3（不兼容 Vue 2）。自定义主题需要 Vue 知识。大型网站的构建时间可能较长。

# HISTORY

**VitePress** 由 Evan You（Vue.js 和 Vite 的作者）创建，作为 VuePress 的现代替代品。它利用了 Vite 快速的开发服务器和构建优化。该项目由 Vue.js 团队维护。

# SEE ALSO

[vite](/man/vite)(1), [vuepress](/man/vuepress)(1), [hugo](/man/hugo)(1), [jekyll](/man/jekyll)(1)
