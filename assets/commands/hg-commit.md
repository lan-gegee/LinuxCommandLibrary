# TAGLINE

将更改保存到仓库，形成新的变更集

# TLDR

**提交所有更改**

```hg commit -m "[message]"```

**提交指定文件**

```hg commit [file1] [file2] -m "[message]"```

**在编辑器中填写提交信息**

```hg commit```

**修补（amend）最后一次提交**

```hg commit --amend```

**关闭某个分支**

```hg commit --close-branch -m "[message]"```

# SYNOPSIS

**hg** **commit** [_options_] [_file_...]

# PARAMETERS

**-m**, **--message** _text_
> 提交信息。

**-A**, **--addremove**
> 提交前添加/移除文件。

**--amend**
> 修补父变更集。

**-u**, **--user** _user_
> 将该用户记录为提交者。

**-d**, **--date** _date_
> 将该日期记录为提交日期。

**--close-branch**
> 将分支标记为已关闭。

**-i**, **--interactive**
> 交互式选择要包含的更改。

**-I**, **--include** _PATTERN_
> 仅包含匹配指定模式的文件。

**-X**, **--exclude** _PATTERN_
> 排除匹配指定模式的文件。

**-l**, **--logfile** _FILE_
> 从文件读取提交信息。

**-s**, **--secret**
> 以 secret 阶段提交。

# DESCRIPTION

**hg commit** 将更改保存到仓库，形成一个新的变更集。未指定文件时，所有已修改的文件都会被提交。使用 **-m** 内联给出提交信息，或省略它以打开编辑器。**--amend** 标志会修改父提交而不是创建新提交。

# CAVEATS

只有已被跟踪的文件才会被提交；新文件需要先用 **hg add** 或 **-A**。**--amend** 会重写历史，应避免用于已经共享的变更集。

# HISTORY

commit 是 **Mercurial** 的核心命令，自该项目 2005 年首次发布以来一直存在。

# SEE ALSO

[hg](/man/hg)(1), [hg-add](/man/hg-add)(1), [hg-status](/man/hg-status)(1), [hg-init](/man/hg-init)(1)

# RESOURCES

```[Source code](https://foss.heptapod.net/mercurial/mercurial-devel)```

```[Documentation](https://wiki.mercurial-scm.org/)```

<!-- verified: 2026-07-19 -->
