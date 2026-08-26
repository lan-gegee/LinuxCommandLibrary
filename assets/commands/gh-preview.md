# TAGLINE

在浏览器中预览 GitHub 风格的 Markdown

# TLDR

**预览 Markdown 文件**（打开浏览器并支持实时刷新）

```gh markdown-preview [README.md]```

**以深色模式预览**

```gh markdown-preview --dark-mode [file.md]```

**在指定端口上预览**

```gh markdown-preview --port [8080] [file.md]```

**预览但不自动打开**浏览器

```gh markdown-preview --disable-auto-open [file.md]```

# SYNOPSIS

**gh markdown-preview** [_options_] [_file_]

# PARAMETERS

**--dark-mode**
> 强制以深色模式渲染。

**--light-mode**
> 强制以浅色模式渲染。

**-p**, **--port** _port_
> 本地服务器的 TCP 端口（默认：3333）。

**--host** _hostname_
> 服务器绑定的主机名（默认：localhost）。

**--disable-auto-open**
> 不自动打开浏览器。

**--disable-reload**
> 禁用文件变更时的实时刷新。

**--verbose**
> 显示详细输出。

**--version**
> 显示版本。

# DESCRIPTION

**gh markdown-preview** 是一个 GitHub CLI 扩展，它会启动本地 Web 服务器，以与 GitHub 一致的渲染效果预览 Markdown 文件。它使用 GitHub Markdown API 以及从 GitHub 网站提取的 CSS，使输出看起来与在 GitHub 上完全一样。

该扩展支持实时刷新，对文件的修改会自动反映到浏览器中。未指定文件时，它会检测并打开当前目录下的 README。

安装方式：**gh extension install yusukebe/gh-markdown-preview**。

# CAVEATS

需要安装 GitHub CLI（**gh**），并且需要联网调用 GitHub Markdown API。渲染结果取决于 GitHub API 的可用性。这是一个社区扩展，不是内置的 gh 命令。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [glow](/man/glow)(1)
