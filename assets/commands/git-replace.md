# TAGLINE

创建、列出或删除对象替换引用

# TLDR

**用一个对象替换另一个对象**

```git replace [object] [replacement]```

**强制替换对象，覆盖已有的替换**

```git replace -f [object] [replacement]```

**列出所有替换引用**

```git replace --list```

**列出匹配某模式的替换引用**

```git replace --list 'refs/replace/abc*'```

**删除一个替换引用**

```git replace -d [object]```

**交互式编辑对象并创建替换**

```git replace --edit [object]```

**嫁接提交使其拥有不同的父提交**

```git replace --graft [commit] [parent1] [parent2]```

**将旧式 grafts 文件转换为替换引用**

```git replace --convert-graft-file```

# SYNOPSIS

**git** **replace** [-f] _object_ _replacement_
**git** **replace** [-f] **--edit** _object_
**git** **replace** [-f] **--graft** _commit_ [_parent_...]
**git** **replace** [-f] **--convert-graft-file**
**git** **replace** **-d** _object_...
**git** **replace** [**--format**=_format_] **-l** [_pattern_]

# PARAMETERS

**-l** [_pattern_], **--list** [_pattern_]
> 列出替换引用。如果按 glob(7) 给出了模式，则只列出匹配的替换。

**-d**, **--delete**
> 删除给定对象已有的替换引用。

**-f**, **--force**
> 覆盖同一对象已有的替换引用，而不是失败退出。

**--graft** _commit_ [_parent_...]
> 创建一个嫁接（graft）提交。新建一个内容与给定提交相同但父提交为指定值的提交，然后创建一个替换引用来替换原提交。

**--convert-graft-file**
> 将 `$GIT_DIR/info/grafts` 中的所有条目转换为替换引用并删除 grafts 文件。这是从旧式 grafts 机制出发的一次性迁移。

**--edit** _object_
> 交互式编辑对象内容。现有内容会以美化格式写入临时文件，然后启动编辑器，其结果用于创建替换对象。

**--raw**
> 与 `--edit` 搭配使用时，提供原始对象内容而非美化格式的内容。对编辑损坏的对象很有用。

**--format**=_format_
> `--list` 输出的格式：`short`（仅显示被替换的 SHA）、`medium`（显示 被替换 -> 替换）或 `long`（包含对象类型）。默认：`short`。

# DESCRIPTION

**git replace** 在 `refs/replace/` 命名空间中创建、列出或删除引用，用某个对象替代另一个对象。这样可以在不修改原始对象的情况下改变对象的呈现方式。

除可达性遍历（prune、包传输、fsck）之外，所有 Git 命令默认都会应用替换。要绕过替换，可使用 `git --no-replace-objects` 或设置 `GIT_NO_REPLACE_OBJECTS` 环境变量。

常见用途包括修复已发布的历史、将不同历史嫁接在一起，或替换过大的 blob。`--graft` 选项简化了重写提交父级关系的过程，取代了旧式的 `$GIT_DIR/info/grafts` 机制。

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

[git-commit](/man/git-commit)(1), [git-tag](/man/git-tag)(1), [git-filter-branch](/man/git-filter-branch)(1), [git-fsck](/man/git-fsck)(1)
