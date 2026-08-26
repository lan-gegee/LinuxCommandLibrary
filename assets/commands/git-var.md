# TAGLINE

显示 Git 的逻辑变量

# TLDR

**显示 Git 变量**

```git var -l```

**显示编辑器**

```git var GIT_EDITOR```

**显示作者身份**

```git var GIT_AUTHOR_IDENT```

**显示提交者身份**

```git var GIT_COMMITTER_IDENT```

**显示配置的分页器**

```git var GIT_PAGER```

# SYNOPSIS

**git** **var** [_variable_]

# PARAMETERS

**-l**
> 列出所有变量。

# DESCRIPTION

**git var** 显示 Git 的逻辑变量，例如配置的编辑器、分页器以及作者/提交者身份。这些值从环境变量和 Git 配置中解析而来，遵循 Git 自身的查找顺序（例如 `$GIT_EDITOR` 会回退到 `core.editor`，再回退到 `$VISUAL`，然后是 `$EDITOR`）。

其他可识别的变量包括 `GIT_SEQUENCE_EDITOR`（`git rebase -i` 使用的编辑器）、`GIT_DEFAULT_BRANCH`、`GIT_SHELL_PATH`、`GIT_ATTR_SYSTEM`/`GIT_ATTR_GLOBAL` 以及 `GIT_CONFIG_SYSTEM`/`GIT_CONFIG_GLOBAL`。

在需要查询 Git 已解析设置的脚本中，该命令很有用，无需直接解析配置文件。

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

[git-config](/man/git-config)(1), [git-commit](/man/git-commit)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-var)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
