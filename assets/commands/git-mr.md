# TAGLINE

检出 GitLab 合并请求

# TLDR

**从 origin 检出合并请求**

```git mr [51]```

**从特定远程检出合并请求**

```git mr [51] [upstream]```

**通过 URL 检出合并请求**

```git mr [https://gitlab.com/owner/repo/merge_requests/51]```

**清理所有本地 mr/ 分支**

```git mr clean```

# SYNOPSIS

**git mr** _number_ [_remote_]

**git mr** _url_

**git mr** **clean**

# PARAMETERS

_NUMBER_
> 合并请求编号。

_REMOTE_
> 远程名称（默认：origin）。

_URL_
> GitLab 合并请求 URL（例如 https://gitlab.tld/owner/repo/merge_requests/453）。

**clean**
> 删除所有本地 mr/ 分支。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mr** 通过编号或 URL 抓取 GitLab 合并请求的末端，并将其检出到名为 mr/_number_ 的本地分支。它把引用抓取和分支创建合为一步，简化了代码评审工作流。

对于 GitHub 仓库，等价命令是 `git pr`。

# CAVEATS

属于 git-extras 软件包。仅适用于 GitLab。GitHub 的等价命令是 git pr。

# HISTORY

git mr 是 **git-extras** 的一部分，提供类似 git pr（针对 GitHub pull request）的 GitLab 合并请求检出功能。

# INSTALL

```zypper: sudo zypper install git-mr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-pr](/man/git-pr)(1), [git-checkout](/man/git-checkout)(1)
