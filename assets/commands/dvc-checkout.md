# TAGLINE

将 DVC 跟踪的文件恢复到工作区

# TLDR

**检出所有被跟踪的**文件

```dvc checkout```

**检出特定文件**

```dvc checkout [data/file.csv.dvc]```

**检出并显示摘要**

```dvc checkout --summary```

**强制检出**，覆盖本地文件

```dvc checkout --force```

# SYNOPSIS

**dvc checkout** [_options_] [_targets_...]

# PARAMETERS

_TARGETS_
> 要检出的 DVC 文件。

**-f**, **--force**
> 覆盖本地更改。

**--summary**
> 显示更改摘要。

**-d**, **--with-deps**
> 包含依赖项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dvc checkout** 将工作区中 DVC 跟踪的文件与 .dvc 文件中指定的版本同步。它通常在 git checkout 之后使用，用于恢复与当前 Git 提交相匹配的数据文件。

在切换 Git 分支或提交时，dvc checkout 会更新数据文件以匹配 .dvc 元数据。文件从 DVC 缓存中获取；如果本地缓存中没有，则需要使用 dvc pull 拉取。

这使得在不同分支间处理不同版本的数据集成为可能。

# CAVEATS

需要数据存在于本地缓存或远程存储中。大文件可能耗时较长。强制模式会覆盖本地更改。按每个 .dvc 文件逐一工作。

# HISTORY

dvc checkout 是 **DVC** 的一部分，为机器学习项目中的版本化数据文件提供类似 Git 的检出语义。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [git-checkout](/man/git-checkout)(1)
