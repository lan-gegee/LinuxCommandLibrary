# TAGLINE

创建新的 Ruby on Rails 应用

# TLDR

**创建新的 Rails 应用**

```rails new [app_name]```

**创建以 PostgreSQL 作为数据库的应用**

```rails new [app_name] --database=postgresql```

**创建使用 MySQL 的应用**

```rails new [app_name] --database=mysql```

**创建仅 API 的应用**（无视图和资源文件）

```rails new [app_name] --api```

**创建不带 Action Mailer 的应用**

```rails new [app_name] --skip-action-mailer```

**使用指定的 Rails 版本创建应用**

```rails _[version]_ new [app_name]```

**在当前目录创建应用**

```rails new .```

# SYNOPSIS

**rails new** _app_name_ [**--database**=_adapter_] [**--api**] [**--skip-***] [_options_]

# PARAMETERS

**--database**, **-d** _adapter_
> 为选定的数据库预配置（sqlite3、mysql、postgresql、oracle、sqlserver 等）

**--api**
> 创建仅 API 的应用（更精简的中间件栈，无视图）

**--skip-git**
> 跳过 git init 和 .gitignore 生成

**--skip-docker**
> 跳过 Dockerfile 及相关文件

**--skip-action-mailer**
> 跳过 Action Mailer 文件

**--skip-action-mailbox**
> 跳过 Action Mailbox gem

**--skip-action-text**
> 跳过 Action Text gem

**--skip-active-record**
> 跳过 Active Record 文件（用于不使用数据库的应用）

**--skip-active-storage**
> 跳过 Active Storage 文件

**--skip-action-cable**
> 跳过 Action Cable 文件

**--skip-asset-pipeline**
> 跳过资源管线

**--skip-javascript**
> 跳过 JavaScript 文件

**--skip-hotwire**
> 跳过 Hotwire 集成

**--skip-jbuilder**
> 跳过 jbuilder gem

**--skip-test**
> 跳过测试文件

**--skip-bundle**
> 不运行 bundle install

**--css** _processor_
> 选择 CSS 处理器（tailwind、bootstrap、bulma、postcss、sass）

**--javascript** _bundler_
> 选择 JavaScript 打包器（importmap、bun、webpack、esbuild、rollup）

**--template**, **-m** _path_
> 从路径或 URL 应用应用模板

**--force**, **-f**
> 覆盖已存在的文件

**--pretend**, **-p**
> 运行但不做任何更改

**--quiet**, **-q**
> 抑制状态输出

# DESCRIPTION

**rails new** 创建一个新的 Ruby on Rails 应用，包含标准目录结构、配置文件和依赖项。它会生成立即开始开发 Web 应用所需的一切内容。

该命令会为模型、视图、控制器、测试和配置创建目录。它初始化包含常用依赖的 Gemfile，设置数据库配置，并可选择初始化 git 仓库。

Rails 应用遵循"约定优于配置"原则。生成的结构确立了其他 Rails 命令和框架所依赖的约定，从而支持自动路由和模型发现等特性。

# CAVEATS

**rails new** 命令通常应在任何现有 Rails 应用目录之外运行。在现有 Rails 应用内运行可能引起冲突。

默认数据库是 SQLite，适合开发环境但不建议用于生产环境。对于打算部署的应用，请用 **--database** 指定可用于生产的数据库。

除非指定 **--skip-bundle**，bundle install 会自动运行。首次运行时由于要下载和编译 gem，可能耗时较长。

# INSTALL

```nix: nix profile install nixpkgs#rails-new```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rails](/man/rails)(1), [bundle](/man/bundle)(1), [gem](/man/gem)(1), [ruby](/man/ruby)(1)
