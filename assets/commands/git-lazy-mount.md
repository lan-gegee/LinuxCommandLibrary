# TAGLINE

无需克隆即可挂载 Git 仓库

# TLDR

**将远程仓库挂载**到本地目录

```git lazy-mount [https://github.com/example/huge-repo] [~/huge-repo]```

**在挂载的目录树中**使用普通 Git 命令工作

```cd [~/huge-repo] && git switch -c [feature]```

**从源码构建**，启用 FUSE 特性

```cargo build --release -p glm-cli --features fuse```

# SYNOPSIS

**git lazy-mount** _repository_url_ _mount_point_

**git-lazy-mount** _repository_url_ _mount_point_

# DESCRIPTION

**git-lazy-mount** 无需先克隆即可将 Git 仓库挂载为本地工作树。它不会预先下载所有对象，而是通过 **FUSE** 文件系统暴露仓库，并在文件被打开、读取或编辑的那一刻按需获取文件内容。从未被触及的文件永远不会被下载，这使得超大型仓库可以在几秒内投入使用，且只占用一小部分磁盘空间。

由于挂载后的目录看起来就像一次普通的检出，常规的 Git 命令在其中都可以正常使用：你可以编辑文件、提交、创建分支和推送。该项目还附带了一个配套工具 `sgrep`，它可以查询远程代码搜索索引并叠加你未提交的修改，因此搜索超大仓库无需先将其实体化。

它以 Git 子命令的形式安装，因此 `git lazy-mount` 与底层的 `git-lazy-mount` 可执行文件是等价的。该工具使用 **Rust** 构建，面向 Linux，依赖内核的 FUSE 接口。

# CAVEATS

git-lazy-mount **仅支持 Linux**；对 macOS 和 Windows 的支持尚在研究中。它需要 **libfuse3** 以及版本不低于 **2.36** 的系统 Git。由于文件内容通过网络延迟获取，首次访问大量文件或离线工作时可能很慢甚至失败，而且挂载依赖于远程仓库保持可达。它最适合以读取为主的工作和对大型仓库的定点编辑，而不适合需要扫描整棵树的操作。

# HISTORY

git-lazy-mount 由 **Mohsen Azimi**（mohsen1）创建，采用 **MIT** 和 **Apache 2.0** 双重许可。根据作者在二十个仓库上的基准测试，它约占用 1.3 GB，而完整克隆需要 23 GB，减少了大约十八倍，同时保留了完整历史。

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

[git](/man/git)(1), [sshfs](/man/sshfs)(1), [mount](/man/mount)(8), [fusermount](/man/fusermount)(1)

# RESOURCES

```[Source code](https://github.com/mohsen1/git-lazy-mount)```

<!-- verified: 2026-06-27 -->
