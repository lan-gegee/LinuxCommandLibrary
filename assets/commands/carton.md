# TAGLINE

Perl 模块依赖管理器

# TLDR

**从 cpanfile 安装依赖**

```carton install```

**更新所有依赖**

```carton update```

**以本地依赖环境运行命令**

```carton exec [perl script.pl]```

**以本地依赖环境运行 Plack 应用**

```carton exec plackup [app.psgi]```

**显示已安装的模块**

```carton list```

**显示依赖树**

```carton tree```

**检查所有依赖是否满足**

```carton check```

**从 cpanfile.snapshot 安装精确版本（部署模式）**

```carton install --deployment```

**从缓存的归档安装（离线）**

```carton install --cached```

**将依赖打包到 vendor/cache 目录**

```carton bundle```

# SYNOPSIS

**carton** _command_ [_options_]

# PARAMETERS

**install**
> 安装 cpanfile 中声明的依赖。

**update** [_modules_]
> 将依赖更新到最新版本。

**exec** _command_
> 以本地库路径执行命令。

**list**
> 列出已安装的模块。

**bundle**
> 将依赖打包到 vendor/cache。

**check**
> 验证依赖是否满足。

**tree**
> 显示依赖树。

**--deployment**
> 从 cpanfile.snapshot 安装精确版本。

**--cached**
> 从缓存的归档安装（离线）。

**--path** _directory_
> 指定本地 lib 目录（默认：local/）。

# DESCRIPTION

**Carton** 是一个 Perl 模块依赖管理器，类似于 Ruby 的 Bundler 或 Node.js 的 npm。它管理在 **cpanfile** 中定义的项目专属依赖，并将其安装到一个与系统 Perl 隔离的本地目录中。

依赖通过简单的 DSL 在 cpanfile 中声明。运行 **carton install** 会生成锁定精确版本的 cpanfile.snapshot，确保跨环境的可复现安装。

**carton exec** 命令在设置好正确库路径的情况下运行程序，避免与系统 Perl 模块冲突。这使得多个使用不同依赖版本的项目可以在同一系统上共存。

# CONFIGURATION

**cpanfile**
> 使用 Perl DSL 语法声明项目依赖。

**cpanfile.snapshot**
> 记录精确解析出的依赖版本的锁定文件，用于可复现安装。

# CAVEATS

Carton 需要 cpanfile，无法自动检测依赖。庞大的依赖树解析和安装可能耗时较长。XS 模块需要编译工具。快照格式在 Carton 主版本之间不兼容。

# HISTORY

Carton 由 **Tatsuhiko Miyagawa**（同时也是 Plack/PSGI 和 cpanm 的作者）创建，于 **2011** 年发布。它受 Ruby 的 Bundler 启发，解决了长期以来 Perl 依赖只能按系统而非按项目管理的问题。该工具已成为现代 Perl 开发工作流的重要组成部分。

# INSTALL

```apk: sudo apk add perl-carton```

```brew: brew install carton```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpanm](/man/cpanm)(1), [cpan](/man/cpan)(1)
