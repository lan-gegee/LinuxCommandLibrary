# TAGLINE

从命令行下载 GitHub release 资产

# TLDR

从最新 release 中**下载**资产

```dra download [owner/repo]```

**交互式选择**资产

```dra download -s [owner/repo]```

**下载指定标签**的 release

```dra download -t [v1.2.3] [owner/repo]```

将二进制资产**安装**到目录中

```dra download -i [~/.local/bin] [owner/repo]```

# SYNOPSIS

**dra** *command* [*options*] [*repo*]

# DESCRIPTION

**dra**（Download Release Assets）用于获取附加在 GitHub Releases 上的文件。它可以列出或下载最新或指定标签的 release，按名称/模式过滤资产，并可选择将可执行文件安装到目标目录——非常适合引导安装你的发行版尚未打包的工具。

# PARAMETERS

**download** [*owner/repo*]

> 下载 release 资产。repo 也可以是 GitHub URL。

**-t**, **--tag** *tag*

> Release 标签（默认：latest）。

**-s**, **--select**

> 交互式选择资产。

**-a**, **--asset** *pattern*

> 资产名称/模式过滤器。

**-i**, **--install** *dir*

> 将下载的二进制文件安装到 *dir*。

**--source** / 认证标志

> 在遇到速率限制时使用带令牌的 GitHub API（**GITHUB_TOKEN** / 具体标志见 **--help**）。

# CAVEATS

受 GitHub API 速率限制；访问私有仓库或高频使用时请设置令牌。下载的二进制文件如有校验和，务必进行验证。

# INSTALL

```pacman: sudo pacman -S dra```

```brew: brew install dra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)

# RESOURCES

```[Source code](https://github.com/devmatteini/dra)```

<!-- verified: 2026-07-19 -->
