# TAGLINE

打印和管理 Go 环境变量

# TLDR

**打印所有 Go 环境变量**

```go env```

**打印指定变量**

```go env GOPATH```

**打印多个变量**

```go env GOROOT GOPATH GOBIN```

**持久化设置一个变量**

```go env -w GOBIN=[/path/to/bin]```

**取消设置一个变量**

```go env -u GOBIN```

**以 JSON 格式打印**

```go env -json```

# SYNOPSIS

**go** **env** [**-json**] [**-u** _var_] [**-w** _var_=_value_] [_var_ ...]

# PARAMETERS

**-json**
> 以 JSON 格式打印环境信息。

**-w** _var_=_value_
> 在 go/env 文件中持久化设置变量。

**-u** _var_
> 从 go/env 文件中取消设置变量。

# DESCRIPTION

**go env** 用于打印 Go 环境信息。不带参数时，它会打印所有已知的环境变量；带参数时，则打印指定变量的值。**-w** 标志会将值写入 go/env 文件，使其跨会话持久生效。**-u** 标志则从 go/env 中移除变量。

# CONFIGURATION

**$HOME/.config/go/env**
> 由 go env -w 管理的持久化 Go 环境变量文件。

# CAVEATS

用 -w 设置的变量优先于 shell 环境变量。go/env 文件通常位于 $HOME/.config/go/env。

# SEE ALSO

[go](/man/go)(1), [go-build](/man/go-build)(1), [go-mod](/man/go-mod)(1)
