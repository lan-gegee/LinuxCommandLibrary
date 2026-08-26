# TAGLINE

Go 开发的实时重载工具

# TLDR

**监视并重载当前目录中的应用**

```goreload```

**监视并构建指定的入口文件**

```goreload [main.go]```

**监视指定路径**

```goreload -t [./cmd/server]```

**将某个目录排除在监视之外**

```goreload -x [vendor]```

**任何文件变化都触发重载，而不限于 .go 文件**

```goreload --all```

**向 go build 传递额外参数**

```goreload --buildArgs "[-ldflags=-s -w]"```

# SYNOPSIS

**goreload** [_options_] [_path_]

# PARAMETERS

**-t**, **--path** _DIR_
> 监视变化的目录（默认：当前目录）。

**-d**, **--build** _DIR_
> 构建源文件的路径（默认：与 **--path** 相同）。

**-b**, **--bin** _NAME_
> 生成的二进制文件名（默认：.goreload）。

**-x**, **--excludeDir** _DIR_
> 不参与监视的相对目录（可重复指定）。

**--all**
> 任何文件变化都触发重载，而不只是 **.go** 文件。

**--buildArgs** _ARGS_
> 透传给 **go build** 的额外参数。

**--logPrefix** _PREFIX_
> 日志输出的自定义前缀。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 打印版本并退出。

# DESCRIPTION

**goreload** 是一款面向 Go 开发的实时重载工具，从 **codegangsta/gin** 分叉而来。它监视源文件，检测到变化时自动重新构建并重启应用，省去了手动重建的循环。

该工具支持配置监视目录、排除模式和自定义构建命令。

# CAVEATS

仅用于开发环境。部分文件事件可能被遗漏。请合理配置排除模式。

# HISTORY

goreload 从 **codegangsta/gin** 分叉而来，精简了未使用的功能；此后它又被多位维护者再次分叉（如 acoshift、oxycoder），成为众多 Go 实时重载工具中的一员。

# SEE ALSO

[air](/man/air)(1), [nodemon](/man/nodemon)(1)

# RESOURCES

```[Source code](https://github.com/acoshift/goreload)```

<!-- verified: 2026-07-17 -->
