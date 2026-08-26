# TAGLINE

按作者生成贡献统计

# TLDR

**显示行数统计**

```git fame```

**按提交数量排序**

```git fame --sort=commits```

**排除路径（逗号分隔或正则表达式）**

```git fame --excl=[vendor/]```

**显示指定目录**

```git fame [src/]```

**显示邮箱而非姓名**

```git fame --show-email```

**检测移动/复制的行以获得更准确的归属**

```git fame -M -C```

# SYNOPSIS

**git fame** [_options_] [_gitdir_...]

# PARAMETERS

_GITDIR_
> 要分析的 Git 目录（默认：当前目录）。可以重复指定。

**--branch** _BRANCH_
> 要分析的分支或标签（默认：HEAD）。

**--sort** _KEY_
> 按 loc（默认）、commits、files、hours 或 months 排序。

**--excl** _PATTERN_
> 排除的文件，逗号分隔或正则表达式。

**--incl** _PATTERN_
> 包含的文件（默认：全部）。

**--loc** _TYPE_
> 统计存活行数、插入行数或删除行数。

**--since** _DATE_, **--until** _DATE_
> 限定某个日期范围内的提交。

**--cost** _METHOD_
> 通过 months、cocomo、hours 或 commits 估算成本。

**-e**, **--show-email**
> 显示作者的邮箱而非姓名。

**-w**, **--ignore-whitespace**
> 在进行 blame 归属时忽略纯空白字符的改动。

**-M**
> 检测文件内部行的移动和复制。

**-C**
> 检测跨文件行的移动和复制。

**-R**, **--recurse**
> 递归查找仓库和子模块。

**-t**, **--bytype**
> 按文件扩展名细分统计。

**--format** _FORMAT_
> 输出格式：pipe、md、yaml、json、csv、tsv 或 tabulate。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**git fame** 生成贡献统计，展示每位作者的代码行数、提交数和文件数。它借助 blame 分析来统计当前归属于各作者的行数，全面呈现谁为代码库贡献了什么。

输出包含用于比较相对贡献占比的百分比，还可以选择使用 COCOMO 模型或提交耗时来估算开发成本。该工具有助于了解代码所有权模式和团队贡献分布。

# CAVEATS

基于 blame 的统计在大型历史上可能较慢。默认跳过二进制文件（使用 **--warn-binary** 可收到提示）。除非使用 **-M**/**-C** 将移动或复制的行追溯到原始作者，否则只有当前树中最后一次修改者会得到归属。

# HISTORY

git fame 是 **Casper da Costa-Luis** 用 Python 重写的版本，与早先启发其命名的 Linus Oleander 的 **git-fame-rb** Ruby gem 有所不同。

# INSTALL

```dnf: sudo dnf install git-fame```

```nix: nix profile install nixpkgs#git-fame```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-effort](/man/git-effort)(1), [git-authors](/man/git-authors)(1), [git-shortlog](/man/git-shortlog)(1), [git-blame](/man/git-blame)(1)

# RESOURCES

```[Source code](https://github.com/casperdcl/git-fame)```

```[Homepage](https://pypi.org/project/git-fame/)```

<!-- verified: 2026-07-17 -->
