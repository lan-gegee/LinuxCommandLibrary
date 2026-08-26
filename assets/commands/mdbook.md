# TAGLINE

通过编写 Markdown 文件创建在线书籍

# TLDR

在当前目录**创建** mdbook 项目

```mdbook init```

在**指定目录**创建 mdbook 项目

```mdbook init [path/to/directory]```

**清理**包含生成书籍的目录

```mdbook clean```

在 http://localhost:3000 上**提供**书籍服务，文件变化时自动构建

```mdbook serve```

**监视** Markdown 文件并在文件变化时自动构建

```mdbook watch```

# SYNOPSIS

**mdbook** _command_ [_options_]

# PARAMETERS

**init**
> 以默认结构创建新的 mdbook 项目

**build**
> 从 Markdown 源码构建书籍

**serve**
> 启动支持实时刷新的本地 Web 服务器

**watch**
> 源文件变化时自动重新构建

**clean**
> 删除生成的书籍输出目录

**test**
> 测试书中的 Rust 代码示例

# DESCRIPTION

**mdbook** 通过编写 Markdown 文件来创建在线书籍。它由 Rust 社区开发，可将一组 Markdown 文件编译成带有导航、搜索和主题支持的静态网站。

典型的 mdbook 项目包含一个定义书籍结构和章节组织的 **SUMMARY.md** 文件。该工具处理这些文件并生成 HTML，支持代码语法高亮、MathJax 公式和自定义主题。

**serve** 命令在写作过程中特别有用，它提供的本地开发服务器会在文件变化时自动重新构建并刷新浏览器。

# CAVEATS

若使用 **mdbook test**，Rust 代码块必须在语法上有效。大型书籍的构建时间可能较慢。自定义主题需要了解 Handlebars 模板。搜索功能基于客户端 JavaScript。

# HISTORY

mdbook 由 Rust 社区创建，最初是用于编写 Rust 文档和《The Rust Programming Language》一书的工具。此后它在 Rust 项目之外的技术文档领域也广受欢迎。

# INSTALL

```apt: sudo apt install mdbook```

```dnf: sudo dnf install mdbook```

```pacman: sudo pacman -S mdbook```

```apk: sudo apk add mdbook```

```zypper: sudo zypper install mdbook```

```brew: brew install mdbook```

```nix: nix profile install nixpkgs#mdbook```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pandoc](/man/pandoc)(1), [hugo](/man/hugo)(1), [mkdocs](/man/mkdocs)(1)
