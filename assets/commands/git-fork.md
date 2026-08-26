# TAGLINE

Fork GitHub 仓库并克隆到本地

# TLDR

**按 URL fork 并克隆仓库**

```git fork [https://github.com/owner/repo]```

**按 slug fork 并克隆仓库**

```git fork [owner/repo]```

**Fork 当前仓库（在现有克隆中运行）**

```git fork```

# SYNOPSIS

**git fork** [_url_]

# PARAMETERS

_URL_
> 要 fork 的仓库 URL。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git fork** 会 fork 一个 GitHub 仓库并克隆到本地，将"fork 项目以参与贡献"这一常见工作流自动化。给定 URL 或 `owner/repo` slug，它会通过 GitHub API fork 该仓库，把新的 fork 克隆到当前目录，并将原始仓库添加为名为 **upstream** 的远程。在 GitHub 仓库的现有克隆中不带参数运行时，它会 fork 该仓库，把现有的 **origin** 远程重命名为 **upstream**，并将 fork 添加为新的 **origin**。远程地址在已配置时使用 SSH，否则使用 HTTPS。

它是 git-extras 套件的组成部分，简化了 GitHub 开源协作中基础的 fork-and-clone 模式。

# CONFIGURATION

**git-extras.github-personal-access-token**
> 用于调用 GitHub API 的个人访问令牌；可用 **git config --global --add git-extras.github-personal-access-token \<token\>** 全局设置，也可针对单个仓库设置以便使用其他账户。

# CAVEATS

属于 git-extras 软件包。需要具有相应 OAuth 权限范围的 GitHub 个人访问令牌。仅支持 GitHub 相关功能。

# HISTORY

git fork 是 **git-extras** 的组成部分，为向项目贡献代码时常见的 GitHub fork 工作流而创建。

# INSTALL

```nix: nix profile install nixpkgs#git-fork```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-clone](/man/git-clone)(1), [gh-repo](/man/gh-repo)(1), [git-remote](/man/git-remote)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/man/git-fork.md)```

<!-- verified: 2026-07-17 -->
