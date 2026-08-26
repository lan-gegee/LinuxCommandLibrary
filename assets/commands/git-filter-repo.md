# TAGLINE

快速、安全地重写 Git 仓库历史的工具

# TLDR

**从历史中移除文件**

```git filter-repo --path [file.txt] --invert-paths```

**重命名路径**

```git filter-repo --path-rename [old/path:new/path]```

**移除大文件**

```git filter-repo --strip-blobs-bigger-than [10M]```

**分析仓库**

```git filter-repo --analyze```

**子目录提升为根目录**

```git filter-repo --subdirectory-filter [dir/]```

# SYNOPSIS

**git filter-repo** [_options_]

# PARAMETERS

**--path** _PATH_
> 只保留给定路径（可重复）；与 **--invert-paths** 结合则改为移除该路径。

**--path-glob** _GLOB_
> 过滤匹配 glob 模式的路径。

**--path-regex** _REGEX_
> 过滤匹配正则表达式的路径。

**--invert-paths**
> 反转路径选择，排除而非包含匹配项。

**--path-rename** _OLD:NEW_
> 在整个历史中重命名路径。

**--replace-text** _FILE_
> 按照文件 _FILE_ 中列出的表达式替换整个历史中的文本（用于清除敏感信息）。

**--strip-blobs-bigger-than** _SIZE_
> 移除大于 _SIZE_ 的 blob（如 10M）。

**--mailmap** _FILE_
> 使用 mailmap 文件重写作者/提交者的姓名和邮箱。

**--tag-rename** _OLD:NEW_
> 重命名匹配模式的标签。

**--analyze**
> 生成分析报告而不进行任何改写。

**--subdirectory-filter** _DIR_
> 将 _DIR_ 设为新的仓库根目录，丢弃其余所有内容。

**--dry-run**
> 显示将要发生的更改而不实际改写仓库。

**--partial**
> 执行部分改写，使历史与未改写的引用混杂在一起（跳过某些安全检查）。

**-f**, **--force**
> 跳过全新克隆的安全检查。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git filter-repo** 以强大的过滤能力重写 Git 历史。它是被弃用的 git filter-branch 的官方推荐替代品，提供显著更快、更安全的历史操作。

该工具可以删除文件、重命名路径、清除敏感数据、更改作者以及重构仓库。它能防止 git filter-branch 常见的失误，并且在大型仓库上的运行速度要快得多。

# CAVEATS

**改写历史会销毁旧提交。** 默认要求全新的克隆（没有其他正在进行的工作）作为安全检查；只有在理解风险的情况下才使用 **--force** 覆盖。协作者必须重新克隆或硬重置到新历史。操作无法撤销。

# HISTORY

git filter-repo 由 **Elijah Newren** 创建，作为 git filter-branch 的官方替代品，自 Git 2.24 发布说明起即受到 git 项目本身的推荐。

# INSTALL

```dnf: sudo dnf install git-filter-repo```

```pacman: sudo pacman -S git-filter-repo```

```apk: sudo apk add git-filter-repo```

```zypper: sudo zypper install git-filter-repo```

```brew: brew install git-filter-repo```

```nix: nix profile install nixpkgs#git-filter-repo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-rebase](/man/git-rebase)(1), [git-filter-branch](/man/git-filter-branch)(1)

# RESOURCES

```[Source code](https://github.com/newren/git-filter-repo)```

```[Documentation](https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html)```

<!-- verified: 2026-07-17 -->
