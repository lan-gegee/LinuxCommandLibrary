# TAGLINE

在网页浏览器中打开仓库页面

# TLDR

**在浏览器中打开仓库**

```gh browse```

**打开特定文件**

```gh browse [path/to/file]```

**打开到特定行**

```gh browse [path/to/file]:[line]```

按编号**打开特定 issue 或 PR**

```gh browse [123]```

**打开发布页面**

```gh browse --releases```

**打开特定分支**

```gh browse --branch [branch_name]```

**打开特定仓库**

```gh browse --repo [owner/repo]```

只打印 URL 不打开浏览器

```gh browse -n```

# SYNOPSIS

**gh** **browse** [_options_] [_file[:line]]_

# PARAMETERS

**-a**, **--actions**
> 打开仓库的 Actions 页面。

**-b**, **--branch** _branch_
> 按名称选择分支。

**-c**, **--commit** _sha_
> 按 SHA 选择提交（默认为最近一次提交）。

**-n**, **--no-browser**
> 只打印 URL 而不打开浏览器。

**-p**, **--projects**
> 打开仓库的项目看板。

**-r**, **--releases**
> 打开仓库的发布页面。

**-R**, **--repo** _[HOST/]OWNER/REPO_
> 选择其他仓库。

**-s**, **--settings**
> 打开仓库设置。

**-w**, **--wiki**
> 打开仓库的 wiki。

**--blame**
> 打开文件的 blame 视图。

# DESCRIPTION

**gh browse** 在网页浏览器中打开 GitHub 仓库。它能根据提供的参数智能跳转到特定的仓库页面、文件甚至行号。

在 git 仓库中运行时，它会自动检测 GitHub 远程地址并打开对应页面。该命令支持打开仓库的各种部分，包括 issues、pull requests、wiki、设置和发布页面。它还可以定位到特定文件和行号，便于与他人分享代码引用。

--no-browser 标志允许只打印 URL 而不打开浏览器，方便脚本编写和与其他工具集成。

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

[gh](/man/gh)(1), [gh-repo](/man/gh-repo)(1)
