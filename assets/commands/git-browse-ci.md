# TAGLINE

在浏览器中打开仓库的 CI 页面

# TLDR

**打开**当前分支远程的 CI 页面

```git browse-ci```

**打开**特定远程的 CI 页面

```git browse-ci [upstream]```

# SYNOPSIS

**git browse-ci** [_remote_]

# PARAMETERS

_remote_
> 要打开其 CI 页面的远程。默认使用当前分支配置的远程，若无则回退到 **origin**。

# DESCRIPTION

**git browse-ci** 是 git-extras 的辅助命令，可在网页浏览器中打开仓库的持续集成页面，省去手动访问托管平台网页界面的步骤。

它完全依据远程 URL 工作。远程地址会从 SSH（**git@host:owner/repo.git**）或 HTTP 形式规范化为一个可浏览的 URL，并根据主机追加相应的后缀以进入 CI 部分：

- **GitHub** 主机追加 **/actions**
- **GitLab** 主机追加 **/-/pipelines**
- **Bitbucket** 主机追加 **/addon/pipelines/home**

得到的 URL 会交给平台对应的打开工具：macOS 上是 **open**，Git-Bash 上是 **start**，WSL 下是 **powershell.exe start**，Linux 和 BSD 上是 **xdg-open**。

# CAVEATS

仅识别 **GitHub**、**GitLab** 和 **Bitbucket**，且匹配方式只是对远程 URL 做子串检测。托管域名中不含这三个词之一的自建实例不会被识别，CircleCI、Travis CI、Jenkins、Drone 等独立 CI 服务同样不被识别，无论仓库实际使用的是哪种 CI。

当主机未被识别时，CI URL 会为空，命令不会报告问题，而是直接让浏览器打开空内容。

URL 是通过对远程字符串做拼接得到的，因此只是推测而非查询。它不会检查 CI 是否已配置，甚至不会检查页面是否存在。

SSH 远程会被改写为 **http://** 而非 **https://**，依赖主机端的重定向。

# HISTORY

**git browse-ci** 是 **git-extras** 的一部分。git-extras 是由 **TJ Holowaychuk** 于 **2010 年**发起的一组 git 辅助脚本合集，现由社区维护。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-browse](/man/git-browse)(1), [git-extras](/man/git-extras)(1), [git-remote](/man/git-remote)(1), [gh-run](/man/gh-run)(1), [xdg-open](/man/xdg-open)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-browse-ci)```

<!-- verified: 2026-07-16 -->
