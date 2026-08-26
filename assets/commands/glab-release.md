# TAGLINE

管理 GitLab 项目发布版本

# TLDR

**列出发布版本**

```glab release list```

创建发布

```glab release create [tag]```

带说明创建

```glab release create [tag] -N "[notes]"```

带附件资产创建

```glab release create [tag] [file1] [file2]```

从特定引用创建

```glab release create [tag] --ref [commit-sha]```

查看发布

```glab release view [tag]```

删除发布

```glab release delete [tag]```

# SYNOPSIS

**glab** **release** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出发布版本。

**create**
> 创建新的发布版本。

**view**
> 查看发布详情。

**delete**
> 删除发布版本。

**upload**
> 向现有发布上传资产。

**download**
> 下载发布资产。

# PARAMETERS (create)

**-n**, **--name** _text_
> 发布标题/名称。

**-N**, **--notes** _text_
> 发布说明（支持 Markdown）。

**-F**, **--notes-file** _file_
> 从文件读取发布说明，`-` 表示 stdin。

**-r**, **--ref** _ref_
> 用于创建发布的提交、标签或分支。

**-m**, **--milestone** _milestone_
> 关联里程碑；可重复使用以关联多个里程碑。

**-T**, **--tag-message** _text_
> 创建附注标签时使用的消息（仅当标签尚不存在时）。

**-D**, **--released-at** _datetime_
> 记录为发布日期的 ISO 8601 日期时间。

**-a**, **--assets-links** _json_
> 要附加到发布的额外资产链接的 JSON 数组。

**--no-close-milestone**
> 创建发布后不关闭关联的里程碑。

**--no-update**
> 若该标签的发布已存在则报错，而不是更新。

**--use-package-registry**
> 将给定资产上传到通用软件包注册表，而非作为发布链接。

**--package-name** _name_
> 与 **--use-package-registry** 配合使用的软件包名称。

**-R**, **--repo** _OWNER/REPO_
> 选择另一个仓库。

# DESCRIPTION

**glab release** 在命令行中管理 GitLab 项目发布版本。它提供创建发布、上传二进制资产、撰写发布说明以及管理现有发布等子命令。

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

[glab](/man/glab)(1), [git-tag](/man/git-tag)(1)

# RESOURCES

```[Documentation](https://docs.gitlab.com/cli/release/)```

```[Source code](https://gitlab.com/gitlab-org/cli)```

<!-- verified: 2026-07-17 -->
