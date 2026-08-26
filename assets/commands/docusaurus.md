# TAGLINE

面向文档优化的静态网站生成器

# TLDR

使用 classic 模板**创建新的 Docusaurus 站点**

```npx create-docusaurus@latest [my-website] classic```

**启动开发服务器**（支持热重载）

```npx docusaurus start```

**在指定端口启动**

```npx docusaurus start --port [8080]```

**构建用于生产环境的站点**

```npx docusaurus build```

**在本地伺服生产构建产物**

```npx docusaurus serve```

**部署到 GitHub Pages**

```npx docusaurus deploy```

**清除生成的文件和缓存**

```npx docusaurus clear```

**将当前文档标记为新版本**

```npx docusaurus docs:version [1.0]```

# SYNOPSIS

**npx docusaurus** _command_ [_options_]

# PARAMETERS

**start** [**--port** _n_]
> 启动开发服务器（默认端口 3000）。

**build** [**--out-dir** _path_]
> 构建用于生产环境的静态站点。

**serve** [**--port** _n_]
> 在本地伺服已构建的站点。

**deploy**
> 部署到 GitHub Pages。

**clear**
> 清除生成的文件和缓存。

**swizzle** _theme_ _component_
> 弹出或包装主题组件以便自定义（交互式）。

**docs:version** _version_
> 将当前文档标记为新版本快照。

**write-translations**
> 提取待翻译字符串到 JSON 翻译文件。

**write-heading-ids**
> 为 Markdown 文档添加显式的标题 ID。

**--locale** _locale_
> 为命令指定区域设置。

**--config** _path_
> 使用自定义配置文件。

**--out-dir** _path_
> build 的自定义输出目录（默认：build/）。

# DESCRIPTION

**Docusaurus** 是一个专为文档网站优化的静态网站生成器。它使用 React 构建 UI，使用 Markdown/MDX 编写内容，并开箱即用地提供版本化、国际化和搜索等功能。

站点通过 **docusaurus.config.js** 进行配置，定义元数据、主题、插件和导航。内容存放在 **docs/** 目录（文档）和 **blog/** 目录（博客文章）中。

开发服务器支持热重载。生产构建会生成可托管在任何地方的静态 HTML、CSS 和 JavaScript。内置的部署功能面向 GitHub Pages。

# PROJECT STRUCTURE

```
my-website/
├── docs/           # Documentation markdown
├── blog/           # Blog posts
├── src/
│   ├── components/ # React components
│   └── pages/      # Custom pages
├── static/         # Static assets
├── docusaurus.config.js
└── sidebars.js     # Sidebar configuration
```

# CONFIGURATION

**docusaurus.config.js**
> 主配置文件，定义站点元数据、主题、插件、导航栏、页脚和构建选项。

**sidebars.js**
> 侧边栏结构配置，定义文档层级和导航。

# CAVEATS

需要 Node.js 18 及以上版本。大型站点的构建时间可能较长。自定义 React 组件需要熟悉 React。Swizzle（自定义）主题组件在版本升级时可能出现问题。全文搜索需要额外配置（Algolia DocSearch 或本地搜索插件）。

# HISTORY

Docusaurus 诞生于 **Facebook**（Meta），并于 **2017 年**开源。它的设计初衷是为 Facebook 的开源项目提供文档支持。Version 2 是一次基于 React 的完全重写，于 **2022 年**发布。该项目由 Meta 及社区贡献者共同维护。

# SEE ALSO

[gatsby](/man/gatsby)(1), [vitepress](/man/vitepress)(1), [mkdocs](/man/mkdocs)(1), [hugo](/man/hugo)(1)
