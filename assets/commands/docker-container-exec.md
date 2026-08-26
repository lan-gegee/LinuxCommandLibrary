# TAGLINE

在运行中的容器内执行命令

# TLDR

**在容器中执行命令**

```docker container exec [container] [command]```

**在容器中启动交互式 shell**

```docker container exec -it [container] /bin/bash```

**以指定用户身份运行命令**

```docker container exec -u [user] [container] [command]```

**设置环境变量并执行命令**

```docker container exec -e [VAR=value] [container] [command]```

**在指定工作目录中执行命令**

```docker container exec -w [/path] [container] [command]```

**在后台（分离模式）运行命令**

```docker container exec -d [container] [command]```

**从文件加载环境变量**

```docker container exec --env-file [env.list] [container] [command]```

# SYNOPSIS

**docker** **container** **exec** [_options_] _container_ _command_ [_args..._]

# PARAMETERS

**-i**, **--interactive**
> 即使未附着也保持 STDIN 打开。

**-t**, **--tty**
> 分配一个伪终端。

**-u**, **--user** _user_
> 用户名或 UID（格式：user、user:group、uid、uid:gid）。

**-w**, **--workdir** _dir_
> 容器内的工作目录。

**-e**, **--env** _list_
> 设置环境变量。

**--env-file** _file_
> 从文件读取环境变量。

**-d**, **--detach**
> 在后台运行命令。

**--detach-keys** _string_
> 覆盖分离容器所用的按键序列。

**--privileged**
> 为该命令赋予扩展权限。

# DESCRIPTION

**docker container exec** 在运行中的容器内执行新命令。命令在容器的默认工作目录或用 **--workdir** 指定的目录中运行。命令必须是可执行文件；串联或加引号的 shell 命令无法直接使用。

这是 **docker exec** 的长格式，行为完全一致。

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

[docker-exec](/man/docker-exec)(1), [docker-container](/man/docker-container)(1), [docker-container-run](/man/docker-container-run)(1), [docker-run](/man/docker-run)(1), [podman-exec](/man/podman-exec)(1)
