# TAGLINE

管理 GitHub 发布和分发资源

# TLDR

**列出发布**

```gh release list```

**创建发布**

```gh release create [tag]```

**创建带标题和说明的发布**

```gh release create [tag] -t "[title]" -n "[notes]"```

**创建带资源文件的发布**

```gh release create [tag] [file1] [file2]```

**创建草稿发布**

```gh release create [tag] --draft```

**下载发布资源文件**

```gh release download [tag]```

**查看发布**

```gh release view [tag]```

**删除发布**

```gh release delete [tag]```

# SYNOPSIS

**gh** **release** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出发布。

**create**
> 创建发布。

**view**
> 查看发布。

**download**
> 下载资源文件。

**delete**
> 删除发布。

**upload**
> 上传资源文件。

**edit**
> 编辑发布。

# PARAMETERS

**-t**, **--title** _title_
> 发布标题。

**-n**, **--notes** _notes_
> 发布说明。

**-F**, **--notes-file** _file_
> 从文件读取发布说明。

**--draft**
> 以草稿形式创建。

**--prerelease**
> 标记为预发布。

**--generate-notes**
> 根据提交和 PR 自动生成发布说明。

**--target** _branch_
> 创建标签时使用的目标分支或提交 SHA。

**--latest**
> 标记为最新发布。

**--verify-tag**
> 若远程仓库中不存在指定标签，则中止发布。

**--notes-start-tag** _tag_
> 用作生成发布说明起点的标签。

**--discussion-category** _name_
> 在指定分类中发起讨论。

**-R**, **--repo** _OWNER/REPO_
> 选择其他仓库。

**-p**, **--pattern** _pattern_
> 只下载匹配 glob 模式的资源文件。

**--archive** _format_
> 下载源码归档（zip 或 tar.gz）。

**--clobber**
> 覆盖同名的现有资源文件（用于上传）。

# DESCRIPTION

**gh release** 管理 GitHub 发布（release），用于软件的版本化分发。发布将 git 标签、发布说明和可下载的二进制资源组合在一起，提供一种官方分发机制。

该命令支持基于现有标签创建发布，也可以自动创建标签。发布说明可以手动撰写、从文件加载，或使用 --generate-notes 标志根据提交信息和已合并的拉取请求自动生成。编译后的二进制文件、软件包和归档等资源可以在创建时上传，也可以稍后添加。

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

[gh](/man/gh)(1), [gh-repo](/man/gh-repo)(1)
