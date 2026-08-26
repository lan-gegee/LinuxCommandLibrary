# TAGLINE

快速、简洁的静态博客框架

# TLDR

**创建新博客**

```hexo init [blog-name]```

**创建新文章**

```hexo new [post-title]```

**生成静态文件**

```hexo generate```

**启动本地服务器**

```hexo server```

**部署到远程**

```hexo deploy```

**清理生成的文件**

```hexo clean```

# SYNOPSIS

**hexo** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的子命令。

**init**
> 初始化新博客。

**new** _TITLE_
> 创建新的文章/页面。

**generate**, **g**
> 生成静态文件。

**publish** _TITLE_
> 将草稿移入文章文件夹并作为已发布文章。

**server**, **s**
> 启动本地服务器。

**deploy**, **d**
> 部署到远程。

**list** _TYPE_
> 列出站点数据（例如 posts、pages、routes、tags）。

**clean**
> 移除缓存文件（`db.json`）和已生成的 `public` 目录。

**-p**, **--port** _PORT_
> 服务器端口（默认 4000）。

**-w**, **--watch**
> 监视文件变更（配合 `generate` 或 `server` 使用）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Hexo** 是一个快速、简洁的静态博客框架。它使用 Markdown 编写内容，支持主题、插件和多种部署目标。

该框架从 Markdown 文章生成静态 HTML。它在开发者博客和文档站点中很受欢迎。

# CAVEATS

需要 Node.js。主题有一定学习曲线。插件兼容性因实现而异。

# HISTORY

Hexo 由 **Tommy Chen** 创建，是一款面向博客的快速静态站点生成器，在开发者社区广受欢迎。

# INSTALL

```brew: brew install hexo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo](/man/hugo)(1), [jekyll](/man/jekyll)(1), [gatsby](/man/gatsby)(1)
