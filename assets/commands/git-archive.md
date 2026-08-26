# TAGLINE

从指定的树创建文件归档

# TLDR

**创建** HEAD 的 tar 归档

```git archive HEAD -o [archive.tar]```

**创建** zip 归档

```git archive --format=zip HEAD -o [archive.zip]```

**归档**一个标签，这是构建发布 tarball 的常用方式

```git archive --format=tar.gz --prefix=[project-1.0/] [v1.0] -o [project-1.0.tar.gz]```

只**归档**某个子目录

```git archive HEAD [path/to/dir] -o [archive.tar]```

**归档**时加上顶层目录，使其解压后整洁

```git archive --prefix=[project/] HEAD -o [archive.tar]```

**管道**传给你选择的压缩器

```git archive HEAD | gzip > [archive.tar.gz]```

将一棵树直接**解压**到另一个目录

```git archive HEAD | tar -x -C [/path/to/dest]```

**列出**支持的格式

```git archive --list```

# SYNOPSIS

**git archive** [**--format**=_fmt_] [**--list**] [**--prefix**=_prefix/_] [_extra_] [**-o** _file_] [_options_] _tree-ish_ [_path_...]

# PARAMETERS

**--format** _fmt_
> 归档格式：**tar**（默认）、**zip**，以及在相应压缩器可用时的 **tar.gz**、**tgz** 等类似格式。若给出 **-o**，格式会根据文件扩展名推断。

**-l**, **--list**
> 列出可用的归档格式。

**-o**, **--output** _file_
> 写入 _file_ 而不是标准输出。

**--prefix** _prefix/_
> 在归档中每个路径前添加 _prefix_ 前缀。末尾的斜杠很重要。

**--add-file** _file_
> 将一个未跟踪的文件加入归档，位于根目录或 **--prefix** 之下。

**--add-virtual-file** _path_:_content_
> 添加一个具有指定字面内容的文件，无需它在磁盘上存在。

**--worktree-attributes**
> 同时采用工作树中的 **.gitattributes**，而不只是被归档树中的。

**--remote** _repo_
> 从远程仓库而不是本地仓库归档一棵树。

**--exec** _cmd_
> 远程上 **git-upload-archive** 的路径。与 **--remote** 配合使用。

**-v**, **--verbose**
> 向标准错误报告进度。

**-0** .. **-9**
> 压缩级别。**-0** 只存储不压缩；**-9** 压缩最狠。适用于 **zip** 和压缩 tar 格式。

**_extra_**
> 透传给归档后端的选项。

# DESCRIPTION

**git archive** 将一棵树的内容写入 tar 或 zip 归档，不包含 **.git** 目录或任何其他版本控制元数据。它是 git 对"把这个修订版本给我一个干净的副本文件"的回答，也是生成发布 tarball 的标准方式。

由于它基于 tree-ish 工作，你可以归档任意提交、分支或标签，而无需检出它们，也不会干扰你的工作树。尾部的路径参数可将归档限制在这些路径内，因此可以从大型仓库中单独提取某个子目录。

**--prefix** 的存在是因为把内容直接炸开到当前目录的归档被视为无礼。传入 **--prefix=project-1.0/** 会给归档一个唯一的顶层目录，符合人们对下载到的 tarball 的预期。

提交 ID 会存储在归档中：tar 格式放在扩展 pax 头部里，zip 格式放在文件注释里，因此 **git get-tar-commit-id** 可以恢复出归档基于哪个修订版本构建。

**.gitattributes** 会影响结果。标记为 **export-ignore** 的路径会被省略，仓库正是借此把 CI 配置和测试夹具排除在发布 tarball 之外；而 **export-subst** 会在归档时展开 **$Format:%H$** 这类占位符。

# CAVEATS

**--remote** 需要服务器允许。许多托管平台（包括 GitHub）禁用了 **git-upload-archive**，对这些平台该命令会失败，你必须改用克隆或抓取。

只有被跟踪的内容会被归档。未跟踪和被忽略的文件绝不会出现，这通常正是你想要的，但意味着归档并不是工作目录的快照。**--add-file** 是注入构建产物的逃生舱口。

默认情况下，归档在不同 git 版本之间并非逐位可复现：内嵌的提交 ID、时间戳以及压缩器自身的输出都可能不同。如果需要可复现的发布产物，请固定 git 和压缩器的版本。

**--format=tar.gz** 与通过管道交给 **gzip** 的区别对 **-9** 很重要：内置格式接受压缩级别参数，而管道则需要把级别传给 **gzip** 本身。

子模块内容不包含在内；子模块在归档中表现为空目录。

# HISTORY

**git archive** 于 **2006 年**加入，用单一前端加可插拔后端的设计取代了较早的 **git-tar-tree** 和 **git-zip-tree** 命令。**--add-file** 支持随 git **2.28**（**2020 年**）到来，**--add-virtual-file** 则随 git **2.34**（**2021 年**）到来。

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

[git-bundle](/man/git-bundle)(1), [git-checkout](/man/git-checkout)(1), [git-clone](/man/git-clone)(1), [tar](/man/tar)(1), [zip](/man/zip)(1), [gzip](/man/gzip)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-archive)```

<!-- verified: 2026-07-16 -->
