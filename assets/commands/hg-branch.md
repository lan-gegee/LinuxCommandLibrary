# TAGLINE

管理 Mercurial 中的命名分支

# TLDR

**显示当前分支**

```hg branch```

**创建新分支**

```hg branch [branch-name]```

**列出所有分支**

```hg branches```

**切换到某个分支**

```hg update [branch-name]```

**关闭当前分支**

```hg commit --close-branch -m "[message]"```

# SYNOPSIS

**hg** **branch** [_name_]

# PARAMETERS

**-f**, **--force**
> 即使分支名与现有分支重名也强制设置。

**-C**, **--clean**
> 将分支名重置为父分支的名称。

# DESCRIPTION

**hg branch** 管理 Mercurial 中的命名分支。不带参数时，它显示当前分支的名称。带有名称参数时，它将工作目录标记为新分支，此标记在下一次提交时生效。命名分支是变更集历史的永久组成部分。如需 Git 风格的轻量级分支，请改用 **hg bookmark**。

# SEE ALSO

[hg](/man/hg)(1), [hg-update](/man/hg-update)(1), [hg-commit](/man/hg-commit)(1)
