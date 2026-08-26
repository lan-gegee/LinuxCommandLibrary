# TAGLINE

以 fast-import 流格式导出 Git 历史

# TLDR

**将仓库导出为流**

```git fast-export --all > [repo.txt]```

**导出指定分支**

```git fast-export [branch] > [branch.txt]```

**连同 blob 一起导出**

```git fast-export --all --signed-tags=strip > [export.txt]```

**导出以便重新导入**

```git fast-export --all | git fast-import```

# SYNOPSIS

**git** **fast-export** [_options_] [_revs_]

# PARAMETERS

**--all**
> 导出所有引用。

**--signed-tags** _mode_
> 处理带签名的标签（warn、strip、verbatim）。

**--tag-of-filtered-object** _mode_
> 处理被过滤对象的标签。

**--no-data**
> 跳过 blob 内容。

**--anonymize**
> 对数据进行匿名化。

# DESCRIPTION

**git fast-export** 以专为 git fast-import 消费而设计的格式生成 Git 仓库历史的完整文本表示。这会创建一种可移植的、与版本控制系统无关的表示形式，涵盖提交、树、标签及其相互关系。

它的主要用途是仓库迁移和转换。导出的流可以在重新导入之前被过滤、修改或拆分，从而支持强大的仓库重构操作，例如提取子目录、重写作者信息或在不同的 Git 托管服务商之间转换。

导出格式是面向行的且人类可读。与 git fast-import 结合使用时，这对命令在大规模历史重写方面比 git filter-branch 快得多。--anonymize 选项支持在保护敏感内容的同时共享仓库结构以便调试。

# INSTALL

```nix: nix profile install nixpkgs#git-fast-export```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-filter-branch](/man/git-filter-branch)(1)
