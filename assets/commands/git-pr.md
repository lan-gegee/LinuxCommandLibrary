# TAGLINE

检出 GitHub 拉取请求

# TLDR

**检出拉取请求**到本地 `pr/N` 分支

```git pr [123]```

**从特定远程检出**

```git pr [123] [upstream]```

**通过完整的拉取请求 URL 检出**

```git pr [https://github.com/owner/repo/pull/123]```

**检出 PR 的合并引用**而不是其末端引用

```git pr --merge [123]```

**删除所有本地 `pr/*` 分支**

```git pr clean```

# SYNOPSIS

**git pr** [_number_ | _url_] [_remote_]

**git pr** **clean**

# PARAMETERS

_NUMBER_
> 拉取请求编号。

_URL_
> 完整的拉取请求 URL（任意主机）；远程和编号会从中解析出来。

_REMOTE_
> 数字编号 PR 对应的远程名称（默认：origin，若设置了 `git-extras.pr.remote` 则用它）。

**-m**, **--merge**
> 抓取 PR 的合并引用（`refs/pull/N/merge`）而不是其末端引用。

**clean**
> 删除所有本地 `pr/*` 分支。

# DESCRIPTION

**git pr** 将 GitHub 拉取请求检出到本地，便于测试、评审或贡献代码。它会把 `refs/pull/N/head`（使用 `-m` 时为 `refs/pull/N/merge`）抓取到名为 `pr/N` 的本地分支，并将其设置为跟踪该引用，因此在该分支内执行 `git pull` 会重新抓取该 PR 的最新版本。

对于 GitLab 仓库，等价命令是 `git mr`。

# CAVEATS

属于 git-extras 软件包。依赖 GitHub 特有的引用布局（`refs/pull/N/head`），对不发布这些引用的主机无效。`git pr clean` 会一次性删除**所有** `pr/*` 分支，而不只是某一个。

# INSTALL

```nix: nix profile install nixpkgs#git-pr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-mr](/man/git-mr)(1), [gh-pr](/man/gh-pr)(1), [git-checkout](/man/git-checkout)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-pr)```

<!-- verified: 2026-07-17 -->
