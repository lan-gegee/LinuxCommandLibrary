# TAGLINE

GitHub 风格 Markdown 预览服务器

# TLDR

**预览当前目录的 README**

```grip```

**预览并在浏览器中打开**

```grip -b```

**预览指定文件**

```grip [README.md]```

**在指定端口预览**

```grip [file.md] [8080]```

**导出为 HTML 文件**

```grip --export [file.md]```

**导出为指定的 HTML 文件**

```grip [README.md] --export [output.html]```

**从标准输入预览**

```cat [file.md] | grip -```

# SYNOPSIS

**grip** [_options_] [_path_] [_address_]

# PARAMETERS

**-b**, **--browser**
> 启动后在浏览器中打开。

**--export**
> 导出为 HTML 文件而不是启动服务。

**--offline**
> 不使用 GitHub API 进行渲染。

**--norefresh**
> 文件变更时禁用自动刷新。

**--quiet**
> 不输出终端信息。

**--user** _user_
> 用于 API 身份验证的 GitHub 用户名。

**--pass** _pass_
> GitHub 密码或个人访问令牌。

**--wide**
> 渲染宽版页面布局。

**--user-content**
> 以用户生成内容（如评论或 issue）的形式渲染。

**--context** _repo_
> 相对 URL 链接所用的仓库上下文（例如 user/repo）。

**--title** _title_
> 渲染输出的自定义页面标题。

**--no-inline**
> 导出的 HTML 中不内联 CSS 样式。

**--api-url** _url_
> 使用自定义 GitHub API URL（用于 GitHub Enterprise）。

# DESCRIPTION

**grip**（GitHub Readme Instant Preview）是一款命令行服务器，它使用 GitHub 的 API 来渲染 GitHub 风格的 Markdown。它能以精确的样式展示 README 在 GitHub 上的呈现效果，文件变更无需刷新页面即可立即反映出来。

使用 **--offline** 可避免基础渲染受 API 速率限制的影响。

# CAVEATS

未进行身份验证时可能受到 GitHub API 速率限制。使用 **--user** 和 **--pass** 配合个人访问令牌可获得更高的限额。

# INSTALL

```dnf: sudo dnf install grip```

```brew: brew install grip```

```nix: nix profile install nixpkgs#grip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[markdown](/man/markdown)(1), [pandoc](/man/pandoc)(1), [glow](/man/glow)(1)
