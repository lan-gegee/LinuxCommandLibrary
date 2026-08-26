# TAGLINE

显示 Git 命令的文档

# TLDR

**获取命令的帮助**

```git help [commit]```

**在网页浏览器中打开**

```git help --web [rebase]```

**显示所有命令**

```git help --all```

**显示指南**

```git help --guides```

**info 格式**

```git help -i [log]```

# SYNOPSIS

**git help** [_options_] [_command_|_guide_]

# PARAMETERS

_COMMAND_
> 要获取帮助的 Git 命令。

_GUIDE_
> Git 指南名称。

**--all**, **-a**
> 列出所有命令。

**--guides**, **-g**
> 列出可用的指南。

**--web**, **-w**
> 在浏览器中打开。

**--man**, **-m**
> 使用 man 格式（默认）。

**--info**, **-i**
> 使用 info 格式。

**--config**, **-c**
> 打印 Git 已知的所有配置变量名。

**--verbose**, **-v**
> 与 **--all** 一起使用时，打印每个命令的单行描述。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git help** 显示 Git 命令和概念性指南的文档。默认打开手册页，也可选择在网页浏览器或 info 格式中显示。

该命令既提供命令文档，也提供涵盖工作流、属性、修订版本规范等主题的概念性指南。Git 内置了丰富的文档，都可以通过这一界面访问。运行 **git** _command_ **--help** 等同于 **git help** _command_。

# CAVEATS

手册页可能需要单独安装。Web 格式需要浏览器。某些指南可能缺失。

# HISTORY

git help 是提供文档访问的 **Git** 核心命令，取代了直接调用 man 页来查看 git 命令的方式。

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

[git](/man/git)(1), [man](/man/man)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-help)```

<!-- verified: 2026-07-17 -->
