# TAGLINE

创建空仓库

# TLDR

**初始化仓库**

```git init```

**在目录中初始化**

```git init [path]```

**初始化裸仓库**

```git init --bare```

**以指定分支初始化**

```git init -b [main]```

**使用模板初始化**

```git init --template=[template_dir]```

# SYNOPSIS

**git** **init** [_options_] [_directory_]

# PARAMETERS

**--bare**
> 创建裸仓库。

**-b**, **--initial-branch** _name_
> 初始分支名。

**--template** _dir_
> 模板目录。

**--shared** _permissions_
> 设置仓库权限。

**--separate-git-dir** _dir_
> 将 `.git` 目录存储在 _dir_ 而不是工作树内。

**--object-format** _format_
> 对象的哈希算法：sha1（默认）或 sha256。

**-q**, **--quiet**
> 安静输出。

# DESCRIPTION

**git init** 创建一个空的 Git 仓库，或重新初始化一个现有仓库。它会创建 `.git` 目录结构，包含 objects、refs/heads、refs/tags 等子目录和模板文件，为版本控制奠定基础。

在现有仓库中运行 git init 是安全的，不会覆盖已有历史。它可用于应用新添加的模板，或在给出 `--separate-git-dir` 时将仓库移动到其他位置。该命令既可以创建工作仓库（带工作目录），也可以创建裸仓库（没有工作目录，通常用作中央服务器）。

`--bare` 选项创建为共享而优化的、不带工作目录的仓库。`--initial-branch` 选项设置第一个分支的名称，适合以 "main" 而不是 "master" 开始。模板目录允许自定义初始仓库结构，包括钩子和配置。

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

[git-clone](/man/git-clone)(1), [git-config](/man/git-config)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-init)```

<!-- verified: 2026-07-17 -->
