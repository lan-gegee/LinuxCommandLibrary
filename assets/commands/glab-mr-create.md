# TAGLINE

创建新的 GitLab 合并请求

# TLDR

**交互式创建 MR**

```glab mr create```

带标题创建

```glab mr create -t "[title]"```

**创建为草稿**

```glab mr create --draft -t "[title]"```

指定评审人创建

```glab mr create -t "[title]" --reviewer [user1],[user2]```

创建到特定分支

```glab mr create --target-branch [main]```

从提交信息自动填充

```glab mr create --fill```

跳过提示并推送分支

```glab mr create --fill --push --yes```

为关联议题创建

```glab mr create --related-issue [issue-number]```

# SYNOPSIS

**glab** **mr** **create** [_options_]

# PARAMETERS

**-t**, **--title** _title_
> MR 标题。

**-d**, **--description** _text_
> MR 描述。使用 `-` 打开编辑器。

**--draft**, **--wip**
> 将合并请求标记为草稿。

**-a**, **--assignee** _users_
> 按用户名将 MR 分配给用户；逗号分隔或重复使用该标志。

**--reviewer** _users_
> 按用户名请求用户评审；逗号分隔或重复使用该标志。

**-b**, **--target-branch** _branch_
> 要合并到的目标/基础分支。

**-s**, **--source-branch** _branch_
> 用于创建 MR 的分支（默认：当前分支）。

**-f**, **--fill**
> 不提示输入标题/描述，改用提交信息。隐含 **--push**。

**--fill-commit-body**
> 当存在多个提交时，用每个提交的正文填充描述。需要 **--fill**。

**-l**, **--label** _labels_
> 按名称添加标签；逗号分隔或重复使用该标志。

**-m**, **--milestone** _milestone_
> 按 ID 或标题分配里程碑。

**-i**, **--related-issue** _issue_
> 为某个议题创建 MR；省略 **--title** 时会使用议题标题。

**--push**
> 创建 MR 后将本地提交推送到源分支。

**--remove-source-branch**
> MR 合并后删除源分支。

**--squash-before-merge**
> 合并时将提交压缩为一个。

**-H**, **--head** _repo_
> 使用另一个头仓库，格式为 `OWNER/REPO`、`GROUP/NAMESPACE/REPO`、项目 ID 或完整 URL。

**--template** _name_
> 使用 `.gitlab/merge_request_templates/` 中的模板预填描述。

**-y**, **--yes**
> 跳过提交确认提示。与 **--fill** 一起使用可跳过所有可选提示。

**-w**, **--web**
> 在浏览器中继续创建 MR。

# DESCRIPTION

**glab mr create** 从当前分支创建新的 GitLab 合并请求。它支持草稿、指派评审人、标签、里程碑，以及从提交信息自动填充标题和描述。

不带任何标志运行时，它会启动交互式提示来撰写合并请求。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab-mr](/man/glab-mr)(1), [glab](/man/glab)(1)

# RESOURCES

```[Documentation](https://docs.gitlab.com/cli/mr/create/)```

```[Source code](https://gitlab.com/gitlab-org/cli)```

<!-- verified: 2026-07-17 -->
