# TAGLINE

更新辅助信息文件，让哑 Git 服务器能够提供仓库服务

# TLDR

为当前仓库**重新生成**服务器信息文件

```git update-server-info```

从头开始**强制完整重建**信息文件

```git update-server-info --force```

**在裸仓库内运行**（常见的服务器端场景）

```git -C [path/to/repo.git] update-server-info```

通过 post-update 钩子在每次推送后**自动刷新**信息

```cp [path/to/repo.git]/hooks/post-update.sample [path/to/repo.git]/hooks/post-update```

# SYNOPSIS

**git** **update-server-info** [_-f_ | _--force_]

# DESCRIPTION

**git update-server-info** 写入辅助索引文件，使"哑"HTTP、FTP 或 rsync 服务器无需运行任何具备 Git 感知能力的服务即可提供 Git 仓库。哑服务器只是从磁盘上直接发送原始文件，因此无法枚举引用或即时生成包。辅助文件向客户端提供了足够的元数据，让它们知道存在哪些引用和包文件。

该命令会重新生成 **objects/info/packs**——列出对象库中的每个包文件——以及 **info/refs**——列出每个引用及其目标对象名。通过哑传输协议获取数据的客户端会读取这些文件来规划需要下载哪些对象。

对于由 **git-daemon**、**git-http-backend** 或任何其他"智能"传输协议提供服务的仓库，这一步并非必需，因为这些服务会按需计算相同的信息。只有普通文件服务器才需要它，例如未启用智能 Git CGI 的 Apache、通过 HTTP 暴露的 S3 存储桶，或静态托管服务商。

Git 自带的 **post-update** 钩子会调用该命令，因此在服务器上启用这个钩子通常就是所需的全部设置。每次推送之后，钩子都会刷新信息文件，让后续的哑客户端看到最新状态。

# PARAMETERS

**-f**, **--force**

> 从头更新信息文件，忽略任何缓存或不完整的中间状态。适用于手动重新打包之后、包文件在 Git 正常流程之外被增删之后，或者信息文件看起来与仓库内容不同步的情况。

# OUTPUT FILES

**objects/info/packs**

> 对象库中每个包文件对应一行 **P pack-_xxx_.pack**。哑客户端读取它来了解可能需要下载哪些包文件。

**info/refs**

> 每个松散和打包的引用对应一行 _sha1_ TAB _refname_。它相当于智能传输协议所发送引用通告的哑传输版本。

# CAVEATS

忘记在哑服务器上运行该命令会让客户端看到过期视图：新推送的提交、新分支和新建的包文件都会一直不可见，直到信息文件被刷新。Git 附带的 **post-update** 示例钩子可以解决这个问题，但必须将其设为可执行——Git 以 **.sample** 后缀发布它，只有重命名后的版本才会被执行。

在工作树上运行该命令无害但几乎没有用处，因为本地访问直接使用对象数据库，从不查询这些信息文件。

# CONFIGURATION

在服务器端的裸仓库上启用自动更新钩子：

```
mv hooks/post-update.sample hooks/post-update
chmod +x hooks/post-update
```

附带的钩子只有一行，调用 **exec git update-server-info**，因此每次推送都会触发刷新。

# HISTORY

哑 HTTP 传输协议及其辅助命令出现在 Git 的早期版本中，那时基于 HTTP 的智能传输尚不存在，许多站点只能使用普通的静态 Web 服务器。如今 **git update-server-info** 主要是一个遗留兼容工具，之所以仍在维护，是因为某些托管环境（对象存储、受严格管控的企业代理、归档镜像）无法运行智能 Git 服务。

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

[git](/man/git)(1), [git-daemon](/man/git-daemon)(1), [git-repack](/man/git-repack)(1)
