# TAGLINE

生成用于报告 Git 缺陷的诊断信息

# TLDR

**生成缺陷报告**

```git bugreport```

**指定输出目录**

```git bugreport --output-directory [path]```

**指定文件名后缀**

```git bugreport --suffix [description]```

# SYNOPSIS

**git bugreport** [_options_]

# PARAMETERS

**--output-directory** _DIR_
> 报告文件所在的目录。

**--suffix** _SUFFIX_
> 文件名的后缀。

**-s** _SUFFIX_
> --suffix 的简写形式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git bugreport** 会生成一个用于向 Git 项目报告缺陷的模板。它收集调试所需的系统信息、git 版本和配置细节。

报告中包含环境信息、已安装的钩子，以及用于描述问题的空间。输出为一个文本文件，可直接提交到 git 邮件列表或 issue 跟踪器。

生成的报告包含 Git 版本、操作系统细节、shell 信息，以及提示你填写问题重现步骤、预期行为和实际行为的模板。

# CAVEATS

用于报告 git 本身的缺陷，而非项目缺陷。可能包含敏感的配置信息，提交前请先检查。

# HISTORY

git bugreport 被加入 **Git** 是为了规范缺陷报告流程，确保包含必要的诊断信息。

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

[git](/man/git)(1)
