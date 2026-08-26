# TAGLINE

基于模板搭建新项目脚手架

# TLDR

**从模板创建项目**

```bun create [template] [project-name]```

**创建 Hono 项目**

```bun create hono@latest [my-app]```

**创建 Elysia 项目**

```bun create elysia [my-app]```

**从 GitHub 模板创建**

```bun create [github-user/repo] [project-name]```

**从本地模板创建**

```bun create [./path/to/template] [project-name]```

# SYNOPSIS

**bun create** _template_ [_destination_]

# DESCRIPTION

**bun create** 基于模板搭建新项目脚手架。它支持来自 npm、GitHub 仓库和本地目录的模板。克隆完成后，它会自动安装依赖并初始化项目。

若只是进行基本的项目初始化而不使用模板，请改用 **bun init**。

# PARAMETERS

_template_
> 模板来源：npm 包、GitHub 仓库（user/repo）或本地路径

_destination_
> 项目目录名（默认为模板名）

# TEMPLATES

**From npm**
> bun create hono@latest my-app

**From GitHub**
> bun create user/repo my-project

**From local directory**
> bun create ./my-template new-project

# RELATED COMMANDS

**bun init**
> 在当前目录初始化空白项目

**bun init --react**
> 搭建 React 项目脚手架

**bun init --react=tailwind**
> 搭建带 Tailwind CSS 的 React 项目

**bun init --react=shadcn**
> 搭建带 shadcn/ui 的 React 项目

# CAVEATS

模板可用性取决于其来源。GitHub 模板需要网络访问。某些模板可能有额外的设置步骤，详见其 README。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-init](/man/bun-init)(1), [npm-init](/man/npm-init)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
