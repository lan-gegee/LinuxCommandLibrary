# TAGLINE

在命令行中管理 GitLab 议题

# TLDR

**列出议题**

```glab issue list```

创建议题

```glab issue create```

查看议题

```glab issue view [number]```

关闭议题

```glab issue close [number]```

重新打开议题

```glab issue reopen [number]```

带标题创建

```glab issue create -t "[title]" -d "[description]"```

# SYNOPSIS

**glab** **issue** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出议题。

**create**
> 创建议题。

**view**
> 查看议题。

**update**
> 更新议题（标题、描述、标签等）。

**close**
> 关闭议题。

**reopen**
> 重新打开议题。

**note**
> 向议题添加评论/备注。

**subscribe**
> 订阅议题。

**unsubscribe**
> 取消订阅议题。

**board**
> 查看或管理议题看板。

**delete**
> 删除议题。

# PARAMETERS

**-t**, **--title** _title_
> 议题标题。

**-d**, **--description** _text_
> 议题描述。

**-l**, **--label** _labels_
> 添加标签（逗号分隔）。

**-a**, **--assignee** _users_
> 分配用户（逗号分隔的用户名）。

**-m**, **--milestone** _name_
> 分配里程碑。

**-c**, **--confidential**
> 创建为机密议题。

**-w**, **--web**
> 在浏览器中打开。

# DESCRIPTION

**glab issue** 在命令行中管理 GitLab 议题。它提供创建、查看、列出、关闭和评论议题等子命令，无需离开终端。

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

[glab](/man/glab)(1), [glab-mr](/man/glab-mr)(1)
