# TAGLINE

通过 HTTP/WebDAV 推送对象

# TLDR

**通过 HTTP/DAV 向远程推送分支**

```git http-push [url] [refs]```

**通过 HTTP 向远程推送所有引用**

```git http-push --all [url]```

**试运行以查看将推送的内容**

```git http-push --dry-run [url] [refs]```

**通过 HTTP 强制推送**，覆盖远程引用

```git http-push --force [url] [refs]```

**带详细输出的推送**，显示对象细节

```git http-push --verbose [url] [refs]```

# SYNOPSIS

**git http-push** [_options_] _url_ _refs_

# PARAMETERS

_URL_
> 远程仓库 URL。

_REFS_
> 要推送的引用。

**--all**
> 推送所有引用。会验证整个本地引用历史中的所有对象都存在于远程仓库中，而不是假设其完整。

**--force**
> 允许更新并非本地引用祖先的远程引用（禁用快进检查）。

**--dry-run**
> 执行除实际发送更新之外的一切操作。

**--verbose**
> 报告本地遍历的对象列表以及成功发送到远程仓库的对象列表。

**-d**, **-D**
> 从远程仓库移除引用而不是向其推送。

# DESCRIPTION

**git http-push** 通过 HTTP/WebDAV 向远程仓库推送对象并更新引用。它是一个底层 plumbing 命令，当远程使用较旧的基于 DAV 的 HTTP 协议时，会被 **git push** 在内部使用。

该命令很少被直接使用。现代 HTTP Git 服务器使用智能 HTTP 协议，由 **git push** 自动处理。基于 DAV 的推送要求远程服务器启用 WebDAV 写访问权限，已被视为遗留方案。

# CAVEATS

遗留协议。现代服务器使用智能 HTTP。很少需要直接使用。远程 HTTP 服务器必须支持具有写权限的 WebDAV。身份验证通过标准 HTTP 凭据处理。

# HISTORY

git http-push 是 **Git** 早期的远程协议之一，在智能 HTTP 协议出现之前使用 WebDAV 进行 HTTP 推送。

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

[git-push](/man/git-push)(1), [git-remote](/man/git-remote)(1), [git-fetch](/man/git-fetch)(1)
