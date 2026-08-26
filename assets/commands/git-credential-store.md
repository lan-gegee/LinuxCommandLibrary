# TAGLINE

将凭据存储在纯文本文件中

# TLDR

**将凭据存储到文件**

```git config credential.helper store```

**存储到指定文件**

```git config credential.helper 'store --file ~/.git-credentials'```

# SYNOPSIS

**git** **credential-store** [_options_]

# PARAMETERS

**--file** _path_
> 凭据文件的路径。

# DESCRIPTION

**git credential-store** 是一个凭据助手，将身份验证凭据永久存储在磁盘上的纯文本文件中。默认存储于 ~/.git-credentials，也可以用 --file 选项指定自定义路径。

配置之后，它会在首次成功验证后保存凭据，并为后续操作自动提供。文件格式很简单：每行包含一条内嵌凭据的 URL，形式为 https://username:password@hostname/path。

这种方式可以永久消除密码提示，非常方便，但有重大的安全隐患。凭据以未加密形式存储，任何能访问文件系统的人都可以读取。为了更好的安全性，请考虑平台专属的替代方案，如 macOS 钥匙串（Keychain）、Windows 凭据管理器，或仅存内存的临时方案 git-credential-cache。

# CONFIGURATION

**~/.git-credentials**
> 默认的纯文本凭据存储文件，每行一条 URL。

**$XDG_CONFIG_HOME/git/credentials**
> 第二查找位置，仅在 ~/.git-credentials 不存在时使用。

# CAVEATS

凭据以纯文本存储。为了更好的安全性，建议改用凭据管理器或 git-credential-cache。

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

[git-credential-cache](/man/git-credential-cache)(1), [git-credential](/man/git-credential)(1)
