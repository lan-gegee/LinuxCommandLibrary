# TAGLINE

创建 GitHub 仓库的 fork

# TLDR

**fork 当前仓库**

```hub fork```

**fork 但不添加 remote**

```hub fork --no-remote```

**fork 指定的仓库**

```hub fork [user/repo]```

**fork 到组织**

```hub fork --org [myorg]```

# SYNOPSIS

**hub fork** [_options_] [_repository_]

# PARAMETERS

**--no-remote**
> 跳过为 fork 添加 git remote。

**--remote-name** _REMOTE_
> 设置新 git remote 的名称。

**--org** _ORGANIZATION_
> 将仓库 fork 到该组织，而不是你的账号。

# DESCRIPTION

**hub fork** 创建 GitHub 仓库的 fork，并自动添加指向你 fork 的 remote。

该命令会将当前目录中检测到的仓库 fork 到你的账号或指定的组织，然后为它添加一个 git remote（默认名为 **origin**；若 **origin** 已被占用，则改用你的 GitHub 用户名）。

# CAVEATS

属于 **hub** 的一部分，hub 已被弃用，推荐改用官方 GitHub CLI（**gh**）；请使用 **gh repo fork**。需要 GitHub 认证。

# HISTORY

hub fork 是 **hub** 的组成部分。hub 是 GitHub 于 2012 年推出的、围绕 git 的仓库操作命令行包装工具。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [gh](/man/gh)(1), [hub-clone](/man/hub-clone)(1)

# RESOURCES

```[Source code](https://github.com/github/hub)```

```[Homepage](https://hub.github.com/)```

<!-- verified: 2026-07-19 -->
