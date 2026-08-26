# TAGLINE

用 Markdown 构建图书和文档

# TLDR

**初始化新书**

```gitbook init```

**本地预览书籍**

```gitbook serve```

**构建静态站点**

```gitbook build```

**构建到指定输出目录**

```gitbook build [.] [output_dir]```

**以特定版本构建**

```gitbook build --gitbook=[2.0.1]```

**安装插件**

```gitbook install```

**列出本地已安装版本**

```gitbook ls```

列出 NPM 上可用的远程版本

```gitbook ls-remote```

**安装特定版本**

```gitbook fetch [version]```

# SYNOPSIS

**gitbook** _command_ [_options_]

# PARAMETERS

**init**
> 用 README.md 和 SUMMARY.md 初始化书籍结构。

**serve**
> 构建书籍并在 localhost:4000 上提供服务。

**build**
> 构建静态网站。

**install**
> 从 book.json 安装插件。

**pdf**
> 生成 PDF（需要 Calibre）。

**epub**
> 生成 ePub。

**mobi**
> 生成 Mobi。

**ls**
> 列出本地已安装的 GitBook 版本。

**ls-remote**
> 列出 NPM 上可用的远程版本。

**fetch** _version_
> 下载并安装特定版本。

**update**
> 更新到最新的 GitBook 版本。

**uninstall** _version_
> 移除特定的已安装版本。

**--gitbook** _version_
> 强制该命令使用特定的 GitBook 版本。

**-d**, **--debug**
> 启用带堆栈跟踪的详细错误输出。

**--log** _level_
> 日志级别：debug、info、warn、error、disabled。

# DESCRIPTION

**gitbook** 是一个用于从 Markdown 文件构建图书和文档的命令行工具。它可以生成静态 HTML 站点或 PDF、ePub 等其他格式。

该工具使用 `book.json` 配置文件，并通过 `SUMMARY.md` 组织内容结构。插件可以扩展功能、提供自定义特性。

# CONFIGURATION

**book.json**
> 项目配置文件，定义标题、描述、插件和构建设置。

**GITBOOK_DIR**
> 环境变量，指定存放 GitBook 版本的自定义目录（默认：~/.gitbook）。

# CAVEATS

旧版 CLI 已不再积极开发。需要较旧的 Node.js 版本（在 Node 12+ 上可能无法工作）。仅支持 gitbook 2.0.0 及以上版本。插件可能无人维护。PDF/ePub/Mobi 生成需要 Calibre。

# HISTORY

**GitBook** 由 **Samy Pesse** 和 **Aaron O'Mullan** 在 **2014 年**前后创建。它曾广泛用于技术文档和图书出版。后来公司转向商业平台，CLI 遂成为遗留工具。社区分支仍在继续开发。

# SEE ALSO

[mdbook](/man/mdbook)(1), [mkdocs](/man/mkdocs)(1), [hugo](/man/hugo)(1), [pandoc](/man/pandoc)(1)
