# TAGLINE

显示提交历史

# TLDR

**显示提交历史**

```git log```

**显示紧凑日志**

```git log --oneline```

**显示图形视图**

```git log --graph --oneline --all```

**显示特定文件的历史**

```git log [file.txt]```

**显示最近 N 条提交**

```git log -n [5]```

# SYNOPSIS

**git log** [_options_] [_revision_] [_--_] [_path_]

# PARAMETERS

**--oneline**
> 紧凑的单行格式。

**--graph**
> 显示分支图形。

**--all**
> 显示所有分支。

**-n** _NUM_
> 限制为 N 条提交。

**--author** _AUTHOR_
> 按作者过滤。

**--since** _DATE_
> 显示指定日期之后的提交。

**--stat**
> 显示变更的文件。

**-p**, **--patch**
> 显示差异。

**--format** _FORMAT_
> 自定义格式字符串。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git log** 按时间倒序显示提交历史。每个条目会显示提交哈希、作者、日期和提交信息。丰富的格式化和过滤选项可以为任何使用场景定制输出。

该命令支持按作者、日期范围、文件路径和提交内容进行过滤。图形模式用 ASCII 字符画直观呈现分支结构。自定义格式字符串便于对日志做脚本化处理和报告生成。

# CAVEATS

庞大的历史记录可能较慢。某些选项不能组合使用。图形视图可能需要较宽的终端。

# HISTORY

git log 是 **Git** 自初始发布就有的核心命令，提供查看提交历史这一基础能力。

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

[git-show](/man/git-show)(1), [git-blame](/man/git-blame)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-log)```

<!-- verified: 2026-07-17 -->
