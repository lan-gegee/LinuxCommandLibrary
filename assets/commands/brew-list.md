# TAGLINE

列出已安装的 Homebrew 软件包

# TLDR

**列出所有已安装的软件包**

```brew list```

**仅列出已安装的 formula**

```brew list --formula```

**仅列出已安装的 cask**

```brew list --cask```

**列出版本信息**

```brew list --versions```

**检查**特定软件包是否已安装

```brew list [package]```

**列出**详细的文件信息

```brew list --verbose [package]```

**列出顶层软件包（非依赖）**

```brew leaves```

# SYNOPSIS

**brew list** [_options_] [_formula|cask_]

# DESCRIPTION

**brew list** 显示所有已安装的 formula 和 cask。不带参数时列出全部软件包；带软件包名时显示该包所安装的文件。

别名：**brew ls**。

# PARAMETERS

**--formula**
> 仅列出已安装的 formula。

**--cask**
> 仅列出已安装的 cask。

**--versions**
> 在软件包旁边显示版本号。

**--verbose**
> 显示每个软件包安装的文件。

**--pinned**
> 仅列出已固定（pin）的 formula。

**--multiple**
> 只显示安装了多个版本的 formula。

**-1**
> 强制每行输出一个条目。

**-l**
> 以长格式列出 formula 和 cask。

**-r**
> 反转排序顺序，最旧的条目排在前面。

**-t**
> 按修改时间排序，最近修改的排在前面。

# RELATED COMMANDS

**brew leaves**
> 显示非依赖的顶层软件包。

**brew deps --tree --installed**
> 显示已安装软件包及其依赖树。

# CAVEATS

输出格式取决于终端能力和标志。使用 --versions 可区分同一软件包的多个已安装版本。

# SEE ALSO

[brew](/man/brew)(1), [brew-info](/man/brew-info)(1), [brew-outdated](/man/brew-outdated)(1), [brew-leaves](/man/brew-leaves)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-19 -->
