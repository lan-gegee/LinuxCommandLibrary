# TAGLINE

生成文档网站

# TLDR

**创建新项目**

```mkdocs new [project-name]```

**本地提供服务**

```mkdocs serve```

**构建站点**

```mkdocs build```

**部署到 GitHub Pages**

```mkdocs gh-deploy```

**在自定义端口提供服务**

```mkdocs serve -a [localhost:8080]```

**严格模式**

```mkdocs build --strict```

# SYNOPSIS

**mkdocs** _command_ [_options_]

# PARAMETERS

_COMMAND_
> MkDocs 操作。

**new** _NAME_
> 创建新项目。

**serve**
> 启动开发服务器。

**build**
> 构建静态站点。

**gh-deploy**
> 部署到 GitHub Pages。

**-a** _ADDR_
> 服务器地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkdocs** 生成文档网站。它从 Markdown 文件构建静态站点。

该工具专为项目文档设计。支持主题和插件。

# CAVEATS

基于 Python。需要 mkdocs.yml 配置文件。Material 主题广受欢迎。

# HISTORY

MkDocs 的创建目标是提供从 Markdown 文件生成简单快速的 **documentation** 的能力。

# INSTALL

```dnf: sudo dnf install mkdocs```

```pacman: sudo pacman -S mkdocs```

```apk: sudo apk add mkdocs```

```brew: brew install mkdocs```

```nix: nix profile install nixpkgs#mkdocs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sphinx-build](/man/sphinx-build)(1), [jekyll](/man/jekyll)(1), [hugo](/man/hugo)(1)
