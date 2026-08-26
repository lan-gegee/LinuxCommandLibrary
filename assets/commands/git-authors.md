# TAGLINE

列出仓库的所有贡献者

# TLDR

将作者列表**打印**到标准输出

```git authors --list```

**打印**不带电子邮件地址的作者列表

```git authors --list --no-email```

将作者**追加**到仓库的 AUTHORS 文件并在编辑器中打开

```git authors```

将作者**追加**到指定文件

```git authors [CONTRIBUTORS]```

自行把列表**保存**到文件

```git authors --list > [AUTHORS]```

# SYNOPSIS

**git authors** [**--list**] [**--no-email**] [_file_]

# PARAMETERS

**-l**, **--list**
> 将作者列表打印到标准输出，而不是写入文件。

**--no-email**
> 省略电子邮件地址，只保留姓名。

_file_
> 要追加到的文件。与 **--list** 同用时被忽略。默认为仓库根目录下文件名匹配 **\*authors\*** 或 **\*contributors\*** 的已有文件，若找不到则为 **AUTHORS**。

# DESCRIPTION

**git authors** 从提交历史中收集仓库的所有去重贡献者，按提交数量降序排列。它是 **git-extras** 的一部分——一套不随核心 git 发布的 git 工具集。

默认行为不是打印。直接运行 **git authors** 会把列表**追加**到 AUTHORS 文件，然后在你的 git 编辑器中打开该文件，这正是这个工具的设计初衷：维护项目的致谢名单。当你只需要标准输出或管道中的名字时，就该用 **--list**。

它的底层是 **git shortlog -sne** 的封装，再经过若干 awk 处理来剥离提交计数并按姓名和邮箱对作者去重。

# CAVEATS

不带参数的 **git authors** 是**追加**而不是覆盖，因此运行两次会让 AUTHORS 文件中的每条记录重复一遍。它还会打开编辑器，因而不适合脚本和 CI；这些场合请使用 **--list**。

它通过在仓库根目录做通配匹配（大小写不敏感地匹配 **\*authors\*** 或 **\*contributors\***）来选择目标文件，因此在含有多个这类名称文件的仓库中，它可能追加到意料之外的文件。

作者信息取自每个提交的 author 字段，因此在不同机器上使用过不同姓名或地址的贡献者会出现多次。去重基于完全相同的姓名和完全相同的邮箱；要真正规范化，请配合 **.mailmap** 文件使用 **git shortlog**。

**--no-email** 先按邮箱去重再去掉地址，因此两个共用同一显示名的不同人可能合并成一条记录。

# HISTORY

**git authors** 是 **git-extras** 的一部分，由 **TJ Holowaychuk** 于 **2010 年**创建，用于打包常用的 git 辅助脚本。该项目现由社区维护。

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

[git-shortlog](/man/git-shortlog)(1), [git-log](/man/git-log)(1), [git-extras](/man/git-extras)(1), [git-blame](/man/git-blame)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-authors)```

<!-- verified: 2026-07-16 -->
