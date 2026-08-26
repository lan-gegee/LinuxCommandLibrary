# TAGLINE

从提交历史生成格式化的更新日志

# TLDR

**生成/更新更新日志文件**（自动检测，或使用 History.md）

```git changelog```

**将更新日志写入指定文件**

```git changelog [CHANGELOG.md]```

**将更新日志打印到标准输出**而非写入文件

```git changelog --stdout```

**自起始标签以来以纯列表形式列出提交**（无小节标题）

```git changelog --list --start-tag [v1.0.0]```

**排除合并提交**

```git changelog --no-merges```

**替换更新日志**而非追加内容

```git changelog --prune-old```

# SYNOPSIS

**git changelog** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输出文件名；默认自动检测 Change*/History* 文件，否则使用 **History.md**。

**-a**, **--all**
> 包含所有提交，忽略 **--start-tag**/**--start-commit**/**--final-tag**。

**-l**, **--list**
> 以纯列表形式列出提交，不带小节标题/日期。

**-t**, **--tag** _LABEL_
> 用作最近未打标签提交的小节标题的标签文字。

**-s**, **--start-tag** _TAG_
> 提交范围起始于的最旧标签。

**--start-commit** _COMMIT_
> 与 **--start-tag** 类似，但从提交开始而非标签。

**-f**, **--final-tag** _TAG_
> 提交范围结束于的最新标签。

**-n**, **--no-merges**
> 排除合并提交。

**-m**, **--merges-only**
> 仅包含合并提交，含主题和正文。

**-p**, **--prune-old**
> 替换现有的更新日志文件，而不是向其追加内容。

**-x**, **--stdout**
> 写入标准输出而非文件。

**-h**, **--help**, **?**
> 显示帮助信息。

# DESCRIPTION

**git changelog** 根据 git 标签（附注或轻量标签）和提交信息生成更新日志。它将提交整理为发布说明，按标签分组为多个小节，适合用作项目的 CHANGELOG。

如果仓库中没有任何标签，则会包含全部提交；否则默认只显示最近一个标签之后的提交（可用 **--start-tag**/**--final-tag** 指定具体范围）。当前目录中已有的 Change*/History* 文件会被自动检测，其内容会追加在新生成的小节之后，除非指定了 **--prune-old**。

提交的格式由 git 配置项 **changelog.format**（默认 `  * %s`）和 **changelog.mergeformat** 控制。

# CAVEATS

属于 git-extras 软件包。生成质量取决于提交信息。基于标签的分组要求仓库中已存在附注或轻量标签。

# HISTORY

git changelog 是 **git-extras** 的一部分，由 **TJ Holowaychuk** 创建，用于从仓库历史自动生成更新日志。

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

[git-log](/man/git-log)(1), [git-tag](/man/git-tag)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog)```

<!-- verified: 2026-07-17 -->
