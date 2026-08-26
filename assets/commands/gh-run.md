# TAGLINE

管理 GitHub Actions 工作流运行

# TLDR

**列出工作流运行**

```gh run list```

**查看运行详情**

```gh run view [run-id]```

**监视一次运行**

```gh run watch [run-id]```

**下载产物**

```gh run download [run-id]```

**重新运行失败的作业**

```gh run rerun [run-id] --failed```

# SYNOPSIS

**gh run** _command_ [_options_]

# PARAMETERS

**list**
> 列出最近的工作流运行。

**view** _RUN-ID_
> 查看运行详情。

**watch** _RUN-ID_
> 实时监视运行进度。

**download** _RUN-ID_
> 下载该运行的产物。

**rerun** _RUN-ID_
> 重新运行某次工作流运行。

**cancel** _RUN-ID_
> 取消正在运行的工作流。

**--workflow** _NAME_
> 按工作流名称过滤。

**--branch** _BRANCH_
> 按分支过滤。

**--failed**
> 只重新运行失败的作业。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh run** 用于在命令行中管理 GitHub Actions 工作流运行。无需访问 github.com 即可掌握 CI/CD 执行情况，包括日志、状态和产物。

watch 命令实时显示正在运行的工作流的进度。download 可获取工作流产出的产物；rerun 可重新触发工作流，并支持完整或部分重跑。

# CAVEATS

需要仓库启用 Actions。日志访问可能受限。产物有保留期限限制。

# HISTORY

随着更全面的 GitHub Actions 集成，gh run 被加入 **GitHub CLI**，使工作流管理可以在命令行中完成。

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

[gh](/man/gh)(1), [gh-workflow](/man/gh-workflow)(1), [gh-pr-checks](/man/gh-pr-checks)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_run)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
