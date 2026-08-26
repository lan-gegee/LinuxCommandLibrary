# TAGLINE

用 Ruby 构建的静态网站生成器

# TLDR

**创建新项目**

```middleman init [project_name]```

**启动开发服务器**

```middleman server```

**在指定端口启动**

```middleman server --port [4567]```

**构建静态网站**

```middleman build```

**以清理模式构建**

```middleman build --clean```

**创建新文章**（博客）

```middleman article "[Article Title]"```

**显示版本**

```middleman version```

# SYNOPSIS

**middleman** [_init_] [_server_] [_build_] [_article_] [_options_]

# PARAMETERS

**init** _NAME_
> 创建新项目。

**server**, **s**
> 启动开发服务器。

**build**, **b**
> 构建静态网站。

**article** _TITLE_
> 创建新的博客文章。

**console**
> 启动交互式控制台。

**--port** _PORT_
> 服务器端口（默认 4567）。

**--bind** _HOST_
> 服务器绑定地址。

**--clean**
> 构建时移除孤立文件。

**--verbose**
> 详细输出。

**--environment** _ENV_
> 构建环境（development、production）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Middleman** 是一个用 Ruby 构建的静态网站生成器。它使用模板、布局和数据文件来生成静态 HTML、CSS 和 JavaScript。

开发服务器提供实时重载。源文件的更改会自动刷新浏览器。这加快了设计和开发工作流。

模板支持 ERB、Haml、Slim 及其他 Ruby 模板语言。资源管道负责处理 Sass、CoffeeScript 和 JavaScript 打包。

YAML 或 JSON 格式的数据文件可以动态填充模板。这将内容与呈现分离，实现数据驱动的页面。

博客扩展提供文章创建、标签和分页功能。文章使用 Markdown 编写，并带有 YAML frontmatter。

构建会在 build 目录中生成静态网站，可直接部署到任何 Web 服务器或 CDN。

# CAVEATS

需要 Ruby 环境。插件依赖可能较复杂。构建时间随站点规模增长。部分插件可能相互冲突。

# HISTORY

**Middleman** 由 **Thomas Reynolds** 于 **2009 年**前后创建。它将现代 Web 开发实践（资源管道、实时重载）引入了静态网站生成。该项目影响了后来的静态网站生成器。

# SEE ALSO

[jekyll](/man/jekyll)(1), [hugo](/man/hugo)(1), [gatsby](/man/gatsby)(1), [bundle](/man/bundle)(1)
