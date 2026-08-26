# TAGLINE

codespaces 管理的简写别名

# TLDR

**为仓库创建 codespace**

```gh cs create -R [owner/repo]```

**列出 codespaces**

```gh cs list```

**通过 SSH 连接到 codespace**

```gh cs ssh -c [codespace-name]```

**在 VS Code 中打开 codespace**

```gh cs code```

**停止运行中的 codespace**

```gh cs stop -c [codespace-name]```

**删除 codespace**

```gh cs delete -c [codespace-name]```

**将文件从 codespace 复制到本地机器**

```gh cs cp remote:[/path/to/file] [local/path]```

# SYNOPSIS

**gh cs** _command_ [_options_]

# PARAMETERS

**create**
> 创建新的 codespace。

**list**
> 列出可用的 codespaces。

**ssh**
> 通过 SSH 连入 codespace。

**code**
> 在 Visual Studio Code 中打开 codespace。

**stop**
> 停止运行中的 codespace。

**delete**
> 删除 codespaces。

**ports**
> 列出并管理端口转发。

**cp**
> 在本地与远程文件系统之间复制文件。

**logs**
> 查看 codespace 日志。

**rebuild**
> 重建 codespace。

**view**
> 查看某个 codespace 的详细信息。

**jupyter**
> 在 JupyterLab 中打开 codespace。

**edit**
> 编辑 codespace。

**-c** _CODESPACE_, **--codespace** _CODESPACE_
> 目标 codespace 名称。若省略，则显示列表供选择。

**-R** _REPO_, **--repo** _REPO_
> 新建 codespace 所用的仓库。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh cs** 是 **gh codespace** 的简写别名，用于在命令行中管理 GitHub Codespaces。Codespaces 是云端托管的开发环境，提供完整的 VS Code 体验，且计算资源可配置。

该命令无需访问 github.com 即可创建、连接和管理 codespaces。它支持通过 SSH 进行终端访问、与本地安装的 VS Code 集成，以及在本地与远程环境之间复制文件。

# CAVEATS

需要拥有 Codespaces 访问权限的 GitHub 账户。使用可能产生费用。Codespaces 有超时和保留期限限制。

# HISTORY

gh cs 被加入 **GitHub CLI** 以支持 Codespaces——GitHub 于 **2020 年**推出的云开发环境。

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

[gh](/man/gh)(1), [gh-codespace](/man/gh-codespace)(1), [gh-repo](/man/gh-repo)(1), [code](/man/code)(1)
