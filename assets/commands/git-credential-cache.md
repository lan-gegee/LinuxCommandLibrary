# TAGLINE

将凭据临时缓存在内存中

# TLDR

**缓存凭据 15 分钟**

```git config credential.helper cache```

**按指定时长缓存**

```git config credential.helper 'cache --timeout=[3600]'```

**使用自定义套接字路径缓存**

```git config credential.helper 'cache --socket=[~/.git-credential-cache/socket]'```

**退出**缓存守护进程（清除所有已缓存的凭据）

```git credential-cache exit```

# SYNOPSIS

**git** **credential-cache** [_options_]

# PARAMETERS

**--timeout** _seconds_
> 缓存凭据的秒数（默认：900，即 15 分钟）。

**--socket** _path_
> 用于与缓存守护进程通信的 Unix 套接字路径（默认：~/.cache/git/credential/socket）。

**exit**
> 让缓存守护进程退出，丢弃所有已缓存的凭据。

**get**, **store**, **erase**
> 标准的凭据助手操作（通常由 git 自身调用，而非手动调用）。

# DESCRIPTION

**git credential-cache** 是一个凭据助手，通过守护进程将身份验证凭据临时存储在内存中。它避免了反复输入密码，又不把凭据永久存到磁盘上，在安全性和便利性之间取得平衡。

配置为凭据助手后，它会在首次身份验证时自动捕获凭据，并在超时期限内为后续操作复用。默认超时为 15 分钟（900 秒），可用 --timeout 选项调整。

守护进程将凭据存储在只有当前用户可访问的 Unix 域套接字中。凭据超时后自动过期，且从不写入磁盘，因此比 git-credential-store 更安全。可以用 git credential-cache exit 手动清空缓存。

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

[git-credential-store](/man/git-credential-store)(1), [git-credential](/man/git-credential)(1)
