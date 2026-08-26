# TAGLINE

通过 GitHub 集成扩展 git 功能

# TLDR

**克隆仓库**

```hub clone [user/repo]```

**创建 pull request**

```hub pull-request```

**fork 仓库**

```hub fork```

**带标题和消息创建 issue**

```hub issue create -m "[title]"```

**在浏览器中浏览仓库**

```hub browse```

**带 tag 创建 release**

```hub release create -m "[Release title]" [tag]```

**带消息发起 pull request**

```hub pull-request -m "[title]"```

# SYNOPSIS

**hub** _command_ [_options_]

# PARAMETERS

_COMMAND_
> GitHub 命令。

**clone**
> 克隆仓库。

**pull-request**
> 创建 pull request。

**fork**
> fork 仓库。

**issue**
> issue 相关操作。

**browse**
> 在浏览器中打开。

**release**
> release 管理。

**create**
> 在 GitHub 上创建仓库。

**ci-status**
> 显示当前提交的 CI 状态。

**api**
> 直接发起 GitHub API 请求。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hub** 通过 GitHub 集成扩展了 git 的功能。它添加了用于 pull request、fork、issue 以及其他 GitHub 操作的命令。

该工具包装 git 命令并加入 GitHub 特有的功能。它可以被别名为 git，从而实现无缝集成。

# CAVEATS

Hub 已不再活跃维护，已被官方 GitHub CLI（**gh**）取代。需要通过 **GITHUB_TOKEN** 或 OAuth 进行 GitHub 认证。当被别名为 **git** 时，hub 会透明地包装所有标准 git 命令。

# HISTORY

hub 由 **GitHub** 创建，是 git 的命令行包装器，后来被官方的 **gh** CLI 取代。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [gist](/man/gist)(1)
