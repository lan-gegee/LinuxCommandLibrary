# TAGLINE

无需重新构建即可修改镜像元数据

# TLDR

**为镜像添加标签**（label）

```crane mutate [image] --label [key=value] -t [new:tag]```

**设置入口点**

```crane mutate [image] --entrypoint [/app/start] -t [new:tag]```

**添加环境变量**

```crane mutate [image] --env [KEY=value] -t [new:tag]```

# SYNOPSIS

**crane** **mutate** [_options_] _image_

# PARAMETERS

**-t**, **--tag** _tag_
> 修改后镜像的标签。

**--label** _key=value_
> 添加或覆盖一个标签（label）。

**--entrypoint** _cmd_
> 设置入口点。

**--cmd** _cmd_
> 设置命令。

**--env** _key=value_
> 添加环境变量。

**--user** _user_
> 设置用户。

**--workdir** _dir_
> 设置工作目录。

# DESCRIPTION

**crane mutate** 无需重新构建即可修改容器镜像的配置。它可以更改标签（label）、入口点、环境变量及其他元数据。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-append](/man/crane-append)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md)```

<!-- verified: 2026-06-26 -->
