# TAGLINE

将提交补丁发送到 pastebin 服务

# TLDR

**粘贴尚未进入上游分支的提交**

```git paste```

**粘贴特定的版本区间**

```git paste [HEAD~3..HEAD]```

**粘贴单个提交**

```git paste -1 [commit]```

# SYNOPSIS

**git** **paste** [_git-format-patch-args_]

# PARAMETERS

_ARGS_
> `git format-patch` 接受的任意参数（版本区间、`-1`、`-n` 等）。省略时默认为 `@{u}`（领先于上游分支的提交）。

# DESCRIPTION

**git paste** 对给定提交运行 `git format-patch --stdout`，并把得到的 diff 通过管道传给 **pastebinit**，最后打印出 pastebin URL。它是 git-extras 的一部分，提供一种无需先创建文件的快速分享补丁或小型提交序列的方式。

由于它委托给 `pastebinit`，目标 pastebin 服务（以及任何 API key）取决于 `pastebinit` 的配置，而不一定是 GitHub Gist。

# CAVEATS

需要单独安装 **pastebinit**；缺失时该命令会报错中止。被粘贴的内容会发送到第三方服务，因此请避免粘贴包含机密的补丁。

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

[git-format-patch](/man/git-format-patch)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-paste)```

<!-- verified: 2026-07-17 -->
