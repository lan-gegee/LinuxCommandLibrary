# TAGLINE

Git 的文件描述符传输辅助程序

# TLDR

**使用文件描述符**进行输入和输出地克隆

```git clone "fd::[fd-in],[fd-out]"```

**使用预先打开的文件描述符连接抓取**

```git fetch "fd::17,18"```

**对输入和输出使用单个文件描述符**

```git fetch "fd::17"```

# SYNOPSIS

**git-remote-fd** _url_

# PARAMETERS

_URL_
> fd::in[,out] 格式的 fd:: URL。

**in**
> 用于从远程读取的文件描述符编号。若省略 out，则该描述符同时用于双向通信。

**out**
> 用于向远程写入的文件描述符编号。

# DESCRIPTION

**git-remote-fd** 是一个 Git 远程辅助程序，它使用预先打开的文件描述符进行通信，而不是自行建立连接。当使用 `fd::in[,out]` 形式的 URL 时，Git 会调用该辅助程序在指定的文件描述符上传输数据。

若只提供一个文件描述符，则读写共用。若以逗号分隔提供两个，则第一个用于从远程读取，第二个用于写入。

这使得与外部管理连接的连接代理、进程监督器或自定义传输层集成成为可能。这些文件描述符必须在调用 Git 之前已经打开。

# CAVEATS

这是一个高级底层特性。文件描述符必须由调用进程预先打开。不适合日常 Git 工作流；主要用于把 Git 嵌入到自行管理连接的应用中。

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

[git-remote](/man/git-remote)(1), [git-remote-ext](/man/git-remote-ext)(1)
