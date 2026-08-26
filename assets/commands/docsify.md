# TAGLINE

动态 Markdown 文档站点生成器

# TLDR

**初始化新文档**站点

```docsify init [./docs]```

**使用指定主题初始化**

```docsify init [./docs] --theme [dark]```

**启动本地预览**服务器

```docsify serve [./docs]```

**在指定端口提供服务**

```docsify serve [./docs] --port [4000]```

**提供服务并自动在浏览器打开**

```docsify serve [./docs] --open```

**自动生成侧边栏**

```docsify generate [./docs]```

# SYNOPSIS

**docsify** _command_ [_options_] [_path_]

# PARAMETERS

_COMMAND_
> 操作：init、serve、generate。

_PATH_
> 文档目录。

**init** [_PATH_]
> 初始化新的 docsify 项目。简写：**i**。

**--local, -l**
> 将 docsify 文件复制到文档路径，而不是使用 CDN（默认：false）。

**--theme, -t** _THEME_
> 选择主题：vue、buble、dark、pure（默认：vue）。

**--plugins, -p**
> 在 index.html 中添加插件脚本标签。

**serve** [_PATH_]
> 启动支持实时重载的本地服务器。简写：**s**。

**--port, -p** _N_
> 服务器端口（默认：3000）。

**--host, -H** _HOST_
> 绑定的主机（默认：localhost）。

**--open, -o**
> 自动打开浏览器。

**generate** [_PATH_]
> 生成侧边栏文件。简写：**g**。

**--sidebar, -s** _FILE_
> 侧边栏文件名（默认：_sidebar.md）。

**--overwrite, -o**
> 允许覆盖现有文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**docsify** 是一个动态渲染 Markdown 文件的文档站点生成器，无需构建静态 HTML。它在加载时即时解析 Markdown 文件，编辑时可获得即时更新。

该工具从 Markdown 文件创建简洁优雅的文档网站，功能包括全文搜索、多种主题、插件支持和 GitHub Pages 兼容性。配置极简，通常只需一个 index.html 和若干 Markdown 文件。

docsify 特别适合项目文档：无需构建步骤，并支持封面页、侧边栏和内嵌代码示例等特性。

# CAVEATS

渲染依赖 JavaScript（没有静态 HTML）。客户端渲染可能影响 SEO。大型文档站点的首次加载可能有延迟。

# HISTORY

docsify 由 **QingWei-Li**（cinwell）创建并以开源项目发布。作为 GitBook 和 VuePress 等文档生成器的轻量级替代方案而广受欢迎，强调简洁且无需构建步骤。可通过 npm 安装：**npm i docsify-cli -g**。

# SEE ALSO

[mkdocs](/man/mkdocs)(1), [vuepress](/man/vuepress)(1), [gitbook](/man/gitbook)(1), [npm](/man/npm)(1)
