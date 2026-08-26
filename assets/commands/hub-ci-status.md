# TAGLINE

显示 GitHub 上某个提交或分支的汇总 CI 状态

# TLDR

**显示当前分支的 CI 状态**

```hub ci-status```

**显示指定 ref 的 CI 状态**

```hub ci-status [branch-name]```

**显示详细输出**

```hub ci-status -v```

**格式化输出**

```hub ci-status -f "[%S %U]"```

# SYNOPSIS

**hub** **ci-status** [_options_] [_ref_]

# PARAMETERS

_COMMIT_
> 要检查的提交 SHA 或分支名。默认为 **HEAD**。

**-v**, **--verbose**
> 打印所有状态检查及其 URL 的详细报告，而不仅仅是汇总状态。

**-f**, **--format** _FORMAT_
> 使用格式字符串美化打印所有状态检查（隐含 **--verbose**）。支持的占位符：**%U**（检查 URL）、**%S**（检查状态）、**%sC**（按状态着色）、**%t**（检查名称）。占位符语法参见 git-log(1) 的 "PRETTY FORMATS" 一节。

**--color**[=_WHEN_]
> 即使标准输出不是终端也启用彩色输出。_WHEN_ 可取 **always**、**never** 或 **auto**（默认）。

# DESCRIPTION

**hub ci-status** 显示某个提交或分支在 GitHub 上的检查汇总状态（Actions 运行、状态检查等），无需在浏览器中打开仓库。

退出状态码反映结果：成功或中性返回 **0**；failure、error、action_required、cancelled 或 timed_out 返回 **1**；pending 返回 **2**。因此它非常适合在脚本和 shell 提示符中使用。

# CAVEATS

Hub 已不再活跃维护，已被官方 GitHub CLI（**gh**）取代；功能最接近的替代是 **gh pr checks** 或 **gh run list**。

# SEE ALSO

[hub](/man/hub)(1), [gh-run](/man/gh-run)(1)

# RESOURCES

```[Source code](https://github.com/mislav/hub)```

<!-- verified: 2026-07-19 -->
