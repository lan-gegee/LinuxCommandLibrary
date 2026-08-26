# TAGLINE

生成适合邮件提交的拉取请求摘要

# TLDR

**生成拉取请求摘要**

```git request-pull [start] [url]```

**生成某个标签与指定分支端点之间的摘要**

```git request-pull [v1.0] [https://example.com/repo.git] [my-branch]```

**在输出中包含补丁文本**

```git request-pull -p [v1.0] [https://example.com/repo.git]```

# SYNOPSIS

**git** **request-pull** [**-p**] _start_ _url_ [_end_]

# PARAMETERS

**-p**
> 在输出中包含补丁文本。

_start_
> 起始提交。它指代一个已存在于上游历史中的提交。

_url_
> 要从中拉取的仓库 URL。

_end_
> 结束提交（默认为 HEAD）。它指代你请求拉取的历史顶端所在的提交。

# DESCRIPTION

**git request-pull** 生成一份适合通过邮件提交的待处理变更摘要。它会创建一条消息，描述起点与当前 HEAD 之间的提交，以及用于拉取的 URL。

该命令常用于基于邮件的补丁工作流中，请维护者从你的仓库拉取变更。

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

[git-format-patch](/man/git-format-patch)(1), [git-send-email](/man/git-send-email)(1), [git-pull](/man/git-pull)(1)
