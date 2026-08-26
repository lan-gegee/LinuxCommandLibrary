# TAGLINE

初始化 git 仓库并添加 GitHub remote

# TLDR

**初始化仓库并在 GitHub 上创建**

```hub init && hub create```

**在指定目录中初始化**

```hub init [directory]```

# SYNOPSIS

**hub** **init** [_options_] [_directory_]

# PARAMETERS

**-g**
> 初始化后，在 GitHub 上创建 "USER/REPO" 仓库并将其添加为 "origin" remote。

**--bare**
> 创建裸仓库。

**-q**, **--quiet**
> 安静模式。

**--template** _dir_
> 使用模板目录。

# DESCRIPTION

**hub init** 会像 git-init(1) 一样创建 git 仓库，并将 remote "origin" 设置为 "git@github.com:USER/REPOSITORY.git"。使用 **-g** 标志时，它还会在 GitHub 上创建对应的仓库。通常与 **hub create** 搭配，在一个工作流中完成本地仓库初始化和对应 GitHub 仓库的创建。

# CAVEATS

Hub 已不再维护。建议改用 **git init** 和 **gh repo create**。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [git-init](/man/git-init)(1), [hub-create](/man/hub-create)(1)
