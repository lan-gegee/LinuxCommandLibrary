# TAGLINE

从 registry 中移除软件包

# TLDR

**撤销发布软件包的某个版本**

```npm unpublish [package]@[version]```

**撤销发布整个软件包**

```npm unpublish [package] --force```

**试运行**

```npm unpublish [package]@[version] --dry-run```

# SYNOPSIS

**npm** **unpublish** [_package_] [_options_]

# PARAMETERS

_PACKAGE_
> 软件包名称及可选的版本号。

**--force**
> 撤销发布整个软件包（所有版本）而非单个版本时必须使用。

**--dry-run**
> 显示将要移除的内容，但不实际撤销发布。

**--workspace** _NAME_
> 在指定工作区（workspace）的上下文中运行命令。

**--workspaces**
> 在所有已配置的工作区中运行命令。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm unpublish** 从 npm registry 中移除已发布的软件包或版本。由于移除软件包可能破坏依赖图中任何位置的下游使用者，registry 对移除的内容和时机做了限制。

在发布的 **72 小时**内，你可以自由撤销某个版本或整个软件包的发布。此后，只有当没有其他软件包依赖它、且软件包所有者是唯一维护者时，registry 才允许撤销发布；否则请联系 npm 支持团队。撤销发布整个软件包后，同名软件包在 **24 小时**内不能重新发布，且任何被撤销发布的 _name@version_ 组合永远不能再使用。

# CAVEATS

可能破坏依赖被移除版本的使用者。如果只是想劝阻使用而不删除制品，请改用 **npm deprecate**。

# HISTORY

npm unpublish 提供**软件包移除**功能，并附带限制以防止生态系统受损。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-deprecate](/man/npm-deprecate)(1)
