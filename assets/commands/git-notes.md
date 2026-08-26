# TAGLINE

为提交添加元数据

# TLDR

**为 HEAD 添加注释**

```git notes add -m "[note text]"```

**为特定提交添加注释**

```git notes add -m "[note]" [commit]```

**查看某个提交的注释**

```git notes show [commit]```

**列出所有注释**

```git notes list```

**编辑现有注释**

```git notes edit [commit]```

**向现有注释追加文本**

```git notes append -m "[more text]" [commit]```

**将注释从一个提交复制到另一个**

```git notes copy [from_commit] [to_commit]```

**移除注释**

```git notes remove [commit]```

**推送注释**到远程

```git push origin refs/notes/*```

**从远程抓取注释**

```git fetch origin refs/notes/*:refs/notes/*```

# SYNOPSIS

**git notes** [_subcommand_] [_options_]

# PARAMETERS

**add**
> 为给定对象添加新注释（默认：HEAD）。若已存在注释则失败，除非使用 **-f**。

**show**
> 打印给定对象的注释。

**list**
> 列出给定对象的注释；未指定对象时列出全部注释。

**edit**
> 在配置的编辑器中编辑现有注释。

**append**
> 向现有注释追加新内容。

**copy** _from_ _to_
> 将注释从一个对象复制到另一个。

**remove**
> 移除给定对象的注释。

**prune**
> 移除附加到已不存在对象上的注释。

**merge** _ref_
> 合并来自另一 notes ref 的注释。

**get-ref**
> 打印当前的 notes ref。

**-m** _MSG_
> 将给定信息用作注释文本。

**-F** _FILE_
> 从文件读取注释文本。

**-C** _OBJECT_
> 复用给定对象的注释。

**-c** _OBJECT_
> 复用并编辑给定对象的注释。

**-f**, **--force**
> 覆盖已存在的注释。

**--ref** _REF_
> 使用给定的 notes ref 而非默认的 **refs/notes/commits**。

# DESCRIPTION

**git notes** 在不修改提交的情况下为提交添加元数据。注释作为独立的引用存储在 **refs/notes/** 下，因此可以在提交创建之后、甚至推送到远程之后，再附加批注、代码评审意见、构建状态或其他元数据。

注释可以通过 **--ref** 选项组织到不同的命名空间中。由于注释不会改变提交哈希，它提供了一种非破坏性的方式来为提交历史补充上下文。

默认的 notes ref 是 **refs/notes/commits**，但你可以通过 **--ref** 或在 git config 中设置 **core.notesRef** 来维护独立的注释命名空间（例如 **refs/notes/review**、**refs/notes/build**）。

# CAVEATS

注释存储在独立的引用中，默认不会被推送或抓取。需要使用 **refs/notes/*:refs/notes/*** 这类显式 refspec 才能在仓库之间同步注释。并发编辑可能引发 notes 合并冲突。

# HISTORY

**git notes** 在 Git **1.6.6**（2009 年 12 月）中加入，用于在不改写历史的前提下为提交附加元数据。

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

[git-log](/man/git-log)(1), [git-commit](/man/git-commit)(1), [git-push](/man/git-push)(1), [git-fetch](/man/git-fetch)(1)
