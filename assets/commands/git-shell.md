# TAGLINE

仅允许 Git SSH 访问的受限登录 Shell

# TLDR

**将用户 shell 设为 git-shell**

```chsh -s $(which git-shell) [git-user]```

**执行被允许的命令**

```git-shell -c "git-receive-pack '/repo.git'"```

# SYNOPSIS

**git-shell** [**-c** _command_]

# PARAMETERS

**-c** _COMMAND_
> 执行 git 命令。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git-shell** 是一个受限登录 Shell，只允许通过 SSH 进行 Git 操作（push、pull、fetch），同时禁止一般的 shell 访问。将它设为用户的登录 shell 后，用户无法交互式登录，但仍可进行 Git 协议操作。

这是创建只能通过 Git 命令交互的安全 Git 托管账户的标准方式。

# CONFIGURATION

**~/git-shell-commands/**
> 可选目录，存放被允许的交互式命令。如果该目录存在，git-shell 会提供一个受限的交互模式并列出这些命令。若此目录中（或 PATH 上的任何位置）存在名为 `no-interactive-login` 的文件，则会完全禁用交互式登录，改为打印该文件的内容。

# CAVEATS

是登录 shell，不是命令。只允许 git 命令。用于 git 服务器账户。

# HISTORY

git-shell 的诞生是为了实现**安全的 git 托管**：它提供了一个只允许 git 操作的受限 shell。

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

[git](/man/git)(1), [ssh](/man/ssh)(1), [chsh](/man/chsh)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-shell)```

<!-- verified: 2026-07-17 -->
