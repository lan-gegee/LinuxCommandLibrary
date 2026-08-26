# TAGLINE

基于 Git 的 dotfiles 管理器

# TLDR

**初始化一个新的 dotfiles 仓库**

```yadm init```

**克隆一个已有的 dotfiles 仓库**

```yadm clone [https://github.com/user/dotfiles.git]```

**克隆并自动运行引导程序**

```yadm clone --bootstrap [https://github.com/user/dotfiles.git]```

**添加要跟踪的文件**

```yadm add [~/.bashrc]```

**提交更改**

```yadm commit -m "[message]"```

**推送到远程仓库**

```yadm push```

从远程仓库**拉取更新**

```yadm pull```

**列出受管理的文件**

```yadm list -a```

**加密敏感文件**

```yadm encrypt```

**解密文件**

```yadm decrypt```

**列出加密文件**但不解密

```yadm decrypt -l```

**查看状态**：被跟踪的 dotfiles 的当前状态

```yadm status```

# SYNOPSIS

**yadm** _command_ [_options_]

# COMMANDS

**init**
> 初始化一个新的 dotfiles 仓库

**clone** _url_
> 克隆一个远程 dotfiles 仓库

**add** _file_...
> 将文件添加到仓库

**commit**
> 将更改记录到仓库

**push**
> 将更改上传到远程仓库

**pull**
> 从远程仓库下载更改

**list** [**-a**]
> 列出受管理的文件（-a 表示全部）

**encrypt**
> 加密 ~/.config/yadm/encrypt 中匹配模式的文件

**decrypt** [**-l**]
> 从加密归档中解密文件。使用 -l 仅列出。

**alt**
> 为替代文件创建符号链接并处理模板

**enter**
> 在设置了 Git 变量的子 Shell 中运行

**config**
> 管理 yadm 配置（用法类似 git config）

**bootstrap**
> 运行引导脚本（如果存在）

**status**
> 显示仓库状态

**diff**
> 查看被跟踪文件的未提交更改

**remote** [**-v**]
> 显示已配置远程仓库的详细信息

# DESCRIPTION

**yadm**（Yet Another Dotfiles Manager）使用 Git 管理 dotfiles，同时让它们保留在 **$HOME** 中的原始位置。所有 Git 命令都可以配合 yadm 使用，因此 Git 用户很容易上手。

仓库存储在 **~/.local/share/yadm/repo.git**，以 **$HOME** 作为工作树。文件保持原位，yadm 无需符号链接或复制即可跟踪它们。

其主要特性包括**替代文件**（基于主机名、操作系统或用户的系统专属配置）、使用 Jinja2 或 envtpl 实现动态配置的**模板**，以及通过 GPG、OpenSSL、transcrypt 或 git-crypt 对敏感数据进行**加密**。

克隆完成后，**bootstrap** 命令会运行 **~/.config/yadm/bootstrap**，从而实现新机器的自动化设置。

# CAVEATS

yadm 依赖 Git；加密功能需要 GPG 或其他受支持的工具。默认情况下工作树是 $HOME，因此在执行破坏性 Git 操作时要格外小心。替代文件和模板在修改后可能需要手动执行 **yadm alt**。

# HISTORY

**yadm** 由 **Tim Byrne** 创建，是一个直接利用 Git 而不引入复杂抽象的简洁 dotfiles 管理器。它于 **2015 年**前后首次发布，其理念是管理 dotfiles 应当像使用 Git 一样简单，同时又加入了加密和系统专属替代文件等特性，因而广受欢迎。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [stow](/man/stow)(1), [chezmoi](/man/chezmoi)(1), [dotbot](/man/dotbot)(1), [gpg](/man/gpg)(1)
