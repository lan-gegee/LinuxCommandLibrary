# TAGLINE

在命令行中管理 GitHub 拉取请求

# TLDR

**创建拉取请求**

```gh pr create```

**列出打开的拉取请求**

```gh pr list```

**检出 PR 分支**

```gh pr checkout [pr-number]```

**在浏览器中查看 PR**

```gh pr view --web```

**合并拉取请求**

```gh pr merge [pr-number]```

# SYNOPSIS

**gh pr** _command_ [_options_]

# PARAMETERS

**create**
> 创建新的拉取请求。

**list**
> 列出拉取请求。

**checkout**
> 在本地检出 PR 分支。

**view**
> 查看拉取请求详情。

**merge**
> 合并拉取请求。

**close**
> 关闭拉取请求。

**reopen**
> 重新打开拉取请求。

**ready**
> 将 PR 标记为可审查。

**checks**
> 显示 CI 状态检查。

**review**
> 为 PR 添加审查。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh pr** 用于在命令行中管理 GitHub 拉取请求。它提供完整的拉取请求生命周期管理，包括创建、审查、合并以及 CI 状态监控。

该命令与 git 工作流集成，会自动识别当前分支对应的拉取请求上下文。它既支持结合编辑器的交互式创建，也支持面向脚本化工作流的自动化创建。

# CAVEATS

大多数操作需要仓库写权限。创建 PR 前需将分支推送到远程。合并可能需要获得批准或通过检查。

# HISTORY

gh pr 是 **GitHub CLI** 的核心命令之一，承载着作为 GitHub 协作模式核心的拉取请求工作流。

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

[gh](/man/gh)(1), [gh-pr-merge](/man/gh-pr-merge)(1), [gh-pr-checks](/man/gh-pr-checks)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_pr)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
