# TAGLINE

静态网站生成器

# TLDR

**创建新站点**

```jekyll new [site_name]```

**构建站点**

```jekyll build```

**本地运行服务**

```jekyll serve```

**带实时刷新的服务**

```jekyll serve --livereload```

**面向生产环境构建**

```JEKYLL_ENV=production jekyll build```

**构建时包含草稿**

```jekyll serve --drafts```

# SYNOPSIS

**jekyll** _command_ [_options_]

# PARAMETERS

**new** _NAME_
> 创建新站点。

**build**
> 构建站点到 _site/。

**serve**
> 本地提供服务并自动重新构建。

**--livereload**
> 启用浏览器实时刷新。

**--drafts**
> 包含草稿文章。

**-d** _DIR_
> 目标目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Jekyll** 是一款静态网站生成器。它将 Markdown 和 Liquid 模板转换为静态 HTML。

该工具是 GitHub Pages 的底层引擎。借助主题和插件，它可以支持博客、文档和自定义站点。

# CAVEATS

基于 Ruby。GitHub Pages 上的插件支持有限。大型站点构建可能较慢。

# HISTORY

Jekyll 由 **Tom Preston-Werner** 于 2008 年创建，后来成为 **GitHub Pages** 背后的引擎。

# INSTALL

```pacman: sudo pacman -S jekyll```

```apk: sudo apk add jekyll```

```nix: nix profile install nixpkgs#jekyll```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bundler](/man/bundle)(1), [hugo](/man/hugo)(1), [hexo](/man/hexo)(1), [gatsby](/man/gatsby)(1)
