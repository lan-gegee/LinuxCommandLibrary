# TAGLINE

创建远程数据库仓库的本地副本

# TLDR

**从 DoltHub 克隆**

```dolt clone [owner/repo]```

**克隆到指定**目录

```dolt clone [owner/repo] [directory]```

使用指定的 remote 名称**克隆**

```dolt clone --remote [name] [owner/repo]```

**克隆指定分支**

```dolt clone -b [branch] [owner/repo]```

限制历史深度的**浅克隆**

```dolt clone --depth [1] [owner/repo]```

带身份验证**克隆私有**仓库

```dolt clone --user [username] [owner/repo]```

# SYNOPSIS

**dolt clone** [_options_] _repository_ [_directory_]

# PARAMETERS

_REPOSITORY_
> 远程仓库（DoltHub 上采用 owner/repo 格式）。

_DIRECTORY_
> 本地目录名（默认使用仓库名）。

**-b**, **--branch** _BRANCH_
> 克隆指定分支。

**--remote** _NAME_
> remote 的名称（默认：origin）。

**--depth** _N_
> 执行浅克隆，历史限制为 N 个提交。

**--single-branch**
> 只克隆一个分支。

**--user** _USERNAME_
> 用于向远程进行身份验证的用户名。密码从 DOLT_REMOTE_PASSWORD 环境变量读取。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dolt clone** 创建远程 Dolt 仓库的本地副本。它会从 DoltHub 或其他 Dolt 远程下载整个数据库，包括所有表、提交历史和分支。

克隆出的仓库保持与 origin 的连接，因而可以执行 push 和 pull 操作。默认获取所有分支，出于效率考虑也可以选择单分支克隆。

这通常是协作开发 Dolt 数据库的第一步：把共享的数据集带到本地环境中进行查询和修改。

# CAVEATS

大型仓库的克隆可能耗时较长。需要网络连接。完整历史需要相应的存储空间。私有仓库可能需要身份验证。

# HISTORY

dolt clone 是 **Dolt** 的组成部分，为数据库仓库实现了 Git 的 clone 语义。借助 DoltHub 和其他远程，它可以对版本化数据库开展分布式协作。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-fetch](/man/dolt-fetch)(1), [dolt-branch](/man/dolt-branch)(1), [git-clone](/man/git-clone)(1)
