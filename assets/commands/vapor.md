# TAGLINE

服务端 Swift Web 框架工具箱

# TLDR

**创建新的 Vapor 项目**

```vapor new [ProjectName]```

**使用自定义模板创建项目**

```vapor new [ProjectName] --template [https://github.com/user/template.git]```

**创建项目并自动对所有提示回答 "no"**

```vapor new [ProjectName] -n```

**在指定输出目录创建项目**

```vapor new [ProjectName] --output [path/to/directory]```

**创建项目但不初始化 Git 仓库**

```vapor new [ProjectName] --no-git```

# SYNOPSIS

**vapor** [**new**] [_options_] [_name_]

# PARAMETERS

**-n**
> 自动对所有交互式问题回答 "no"。

**--output** _path_
> 为新项目指定自定义的文件夹位置。

**--template** _url_
> 使用来自 Git 仓库 URL 的自定义模板。

**--branch** _name_
> 为模板指定不同的 Git 分支（默认：main）。

**--no-git**
> 跳过 Git 仓库初始化。

**--no-commit**
> 初始化 Git 但跳过初始提交。

**--help**
> 显示帮助信息。

# DESCRIPTION

**vapor** 是 Vapor Web 框架（一个服务端 Swift HTTP 框架）的命令行工具箱。该工具箱的主要用途是从模板创建新的 Vapor 项目。**new** 是默认子命令，可以省略。

项目从模板创建，模板包含路由、中间件，以及可选用于数据库操作的 Fluent ORM。工具箱通过清单文件（YAML 或 JSON）支持动态项目生成，清单文件定义了变量，并根据用户响应决定是否包含某些文件。

项目创建后，直接使用 Swift Package Manager（`swift build`、`swift run`）来构建和运行应用。

# CAVEATS

在 macOS 上需要 Swift 工具链和 Xcode Command Line Tools。Linux 上需要安装 Swift。工具箱要求 macOS 15.0+ 或 Swift 6.1+ 支持的 Linux 发行版。数据库驱动（PostgreSQL、MySQL、SQLite）作为 Swift 软件包依赖添加。

# HISTORY

**Vapor** 由 Tanner Nelson 于 2016 年创建，是最早的大型服务端 Swift 框架之一，并迅速成为最流行的 Swift Web 框架。2020 年发布的 Vapor 4 带来了完整的 async/await 支持和性能改进。该框架由 Vapor 社区维护，在全球众多公司的生产环境中使用。

# INSTALL

```brew: brew install vapor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swift](/man/swift)(1), [swiftc](/man/swiftc)(1), [docker](/man/docker)(1)
