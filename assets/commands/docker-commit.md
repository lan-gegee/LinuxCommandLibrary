# TAGLINE

根据容器的更改创建镜像

# TLDR

**从容器创建镜像**

```docker commit [container_id] [image_name:tag]```

**附带作者信息**提交

```docker commit --author "[name]" [container_id] [image:tag]```

**附带说明**提交

```docker commit -m "[Added config files]" [container_id] [image:tag]```

**以修改后的 CMD** 提交

```docker commit --change "CMD ['/app/start.sh']" [container_id] [image:tag]```

# SYNOPSIS

**docker** **commit** [_options_] _container_ [_repository[:tag]_]

# PARAMETERS

**-a**, **--author** _string_
> 镜像的作者。

**-c**, **--change** _list_
> 对镜像应用 Dockerfile 指令。

**-m**, **--message** _string_
> 提交说明。

**-p**, **--pause**
> 提交期间暂停容器（默认为 true）。

# DESCRIPTION

**docker commit** 根据容器的更改创建新镜像。它通过检查容器自创建以来的所有修改，将容器文件系统的当前状态捕获为一个新的镜像层。

虽然它在调试、实验或保存工作状态时很有用，但不推荐在生产工作流中使用这种方式。Dockerfile 能提供更好的可复现性、版本控制和构建过程文档。commit 得到的镜像缺少 Dockerfile 那样透明的层历史，因此更难维护和审计。

# CAVEATS

不包含挂载进容器的卷中的数据。得到的镜像缺乏有意义的构建历史，无法从源码复现。默认情况下，容器会在整个提交期间被暂停（**--pause=true**）；传入 **--pause=false** 可保持其运行，但若仍有写入正在进行，就有捕获到不一致的文件系统快照的风险。

# HISTORY

**docker commit** 自 **2013 年** Docker 项目首次公开发布起就存在于 Docker CLI 中。它早于 Dockerfile，是最初构建镜像的方式；现代工作流更倾向于用 **docker build** 保证可复现性，而只在临时调试快照时使用 **docker commit**。

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

[docker](/man/docker)(1), [docker-build](/man/docker-build)(1), [docker-save](/man/docker-save)(1), [docker-diff](/man/docker-diff)(1)
