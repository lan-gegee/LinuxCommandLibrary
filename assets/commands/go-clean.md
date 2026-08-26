# TAGLINE

删除 Go 构建产物和缓存数据

# TLDR

**清理构建缓存**

```go clean```

**清理测试缓存**

```go clean -testcache```

**清理模块缓存**

```go clean -modcache```

**清理全部缓存**

```go clean -cache -testcache -modcache```

**清理模糊测试缓存**

```go clean -fuzzcache```

**演练模式，显示将要删除的内容**

```go clean -n [package]```

**详细清理并显示删除命令**

```go clean -x -cache```

# SYNOPSIS

**go clean** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要清理的软件包。

**-cache**
> 删除整个构建缓存。

**-testcache**
> 使构建缓存中的所有测试结果过期。

**-modcache**
> 删除整个模块下载缓存。

**-fuzzcache**
> 删除构建缓存中为模糊测试保存的文件。

**-i**
> 删除对应的已安装归档或二进制文件。

**-r**
> 递归应用到指定软件包的所有依赖。

**-n**
> 打印将要执行的删除命令，但不执行。

**-x**
> 在删除命令执行时打印出来。

# DESCRIPTION

**go clean** 删除目标文件和缓存数据。它清理构建产物、测试结果和已下载的模块，以释放磁盘空间或强制重新构建。

该命令可以针对特定的缓存或软件包。清理模块缓存会移除所有已下载的依赖，下次构建时需要重新下载。

# CAVEATS

模块缓存清理会影响所有项目。测试缓存清理会强制重新运行测试。可能需要重新下载依赖。

# HISTORY

go clean 是 **Go** 工具链的一部分，提供缓存和构建产物管理。

# SEE ALSO

[go](/man/go)(1), [go-build](/man/go-build)(1), [go-mod](/man/go-mod)(1), [go-test](/man/go-test)(1)
