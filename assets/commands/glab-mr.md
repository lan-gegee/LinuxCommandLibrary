# TAGLINE

在命令行中管理 GitLab 合并请求

# TLDR

**列出合并请求**

```glab mr list```

创建合并请求

```glab mr create```

查看合并请求

```glab mr view [number]```

检出合并请求

```glab mr checkout [number]```

合并一个合并请求

```glab mr merge [number]```

批准合并请求

```glab mr approve [number]```

# SYNOPSIS

**glab** **mr** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出合并请求。

**create**
> 创建新的合并请求。

**view**
> 显示合并请求。

**checkout**
> 在本地检出合并请求的分支。

**update**
> 修改合并请求详情（标题、描述、标签等）。

**merge**
> 合并一个合并请求。

**rebase**
> 将合并请求的源分支变基到其目标分支上。

**approve**
> 批准一个合并请求。

**approvers**
> 查看或管理合并请求的审批人。

**revoke**
> 撤销对合并请求的批准。

**close**
> 关闭一个合并请求。

**reopen**
> 重新打开已关闭的合并请求。

**delete**
> 删除合并请求。

**diff**
> 显示合并请求中的更改。

**note**
> 向合并请求添加评论。

**issues**
> 查看与合并请求关联的议题。

**subscribe** / **unsubscribe**
> 订阅或取消关注合并请求的通知。

**todo**
> 将合并请求加入你的 GitLab 待办列表。

# DESCRIPTION

**glab mr** 在命令行中管理 GitLab 合并请求。它提供创建、查看、评审、批准和合并 MR 等子命令，无需离开终端。运行 `glab mr <subcommand> --help` 可查看各子命令的标志。

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

[glab](/man/glab)(1), [glab-mr-create](/man/glab-mr-create)(1)

# RESOURCES

```[Documentation](https://docs.gitlab.com/cli/mr/)```

```[Source code](https://gitlab.com/gitlab-org/cli)```

<!-- verified: 2026-07-17 -->
