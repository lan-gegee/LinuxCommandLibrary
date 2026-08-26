# TAGLINE

检查容器文件系统上文件或目录的变更

# TLDR

**查看容器内的文件系统变更**

```docker diff [container_name]```

**使用容器 ID 查看变更**

```docker diff [container_id]```

# SYNOPSIS

**docker** **diff** _container_

# OUTPUT FIELDS

**A**
> 文件或目录被新增。

**C**
> 文件或目录被修改（内容或元数据变化）。

**D**
> 文件或目录被删除。

# DESCRIPTION

**docker diff** 检查自容器基于其基础镜像创建以来，文件系统上文件或目录的变更。输出用单字符前缀对每项变更分类：**A** 表示新增、**C** 表示变更/修改、**D** 表示删除。

此命令有助于了解运行中或已停止的容器内部发生了哪些改动，可用于调试、审计变更，或确定哪些内容应通过 **docker commit** 捕获到新镜像中。它只报告容器可写层中的变更；底层的镜像层保持不变。

可以用名称或完整/简写的容器 ID 来引用容器。

# CAVEATS

diff 操作会检查容器的整个文件系统，因此对改动较多的容器可能耗时较长。没有可用的过滤选项；总是显示完整的 diff 结果。

# HISTORY

**docker diff** 从 Docker 早期版本起就可用。它是 **docker container diff** 的别名，在较新的 Docker CLI 版本中推荐使用后者。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-container-diff](/man/docker-container-diff)(1), [docker-commit](/man/docker-commit)(1), [docker-inspect](/man/docker-inspect)(1), [docker-cp](/man/docker-cp)(1)
