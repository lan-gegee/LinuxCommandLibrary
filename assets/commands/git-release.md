# TAGLINE

创建版本发布标签

# TLDR

**创建发布标签**

```git release [version]```

**带信息创建**

```git release [version] -m "[message]"```

**创建并推送**

```git release [version] --push```

# SYNOPSIS

**git** **release** [_options_] _version_

# PARAMETERS

**-m**, **--message** _text_
> 标签信息。

**--push**
> 打标签后推送。

**-s**, **--sign**
> 对标签签名。

# DESCRIPTION

**git release** 通过用指定版本号为当前提交打标签，并将标签（以及任何待推送的提交）推送到远程来完成发布。它是 **git-extras** 工具套件的一部分，将标签创建、可选签名和发布合并为一个操作，简化了发布工作流。

常见用法遵循语义化版本（例如 `git release 1.2.3`）。该命令创建附注标签，可通过 `-m` 选项附带发布说明，并通过 `-s` 进行加密签名以便验证。

# CAVEATS

需要安装 **git-extras**；该命令不属于 Git 核心。标签会被推送到配置的远程，可能触发 CI/CD 发布流水线。

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

[git](/man/git)(1), [git-tag](/man/git-tag)(1), [git-extras](/man/git-extras)(1)
