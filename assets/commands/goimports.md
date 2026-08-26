# TAGLINE

Go 导入行的管理与格式化

# TLDR

**格式化文件并修复其中的导入**

```goimports [file.go]```

**修复导入并写回文件**

```goimports -w [file.go]```

**显示更改的差异**

```goimports -d [file.go]```

**列出存在导入问题的文件**

```goimports -l [file.go]```

**分离本地包的导入**

```goimports -local [github.com/myorg] [file.go]```

**格式化目录中的所有文件**

```goimports -w .```

# SYNOPSIS

**goimports** [_flags_] [_path_ ...]

# PARAMETERS

**-d**
> 显示差异而不重写。

**-l**
> 列出导入有差异的文件。

**-w**
> 将结果写回源文件。

**-local** _prefix_
> 以逗号分隔的本地包前缀列表。

**-e**
> 报告所有错误（而不是不同行上只报前 10 个）。

**-format-only**
> 不修复导入，仅格式化代码。在此模式下，goimports 实际上就是带分组导入的 gofmt。

**-v**
> 详细日志输出。

**-srcdir** _dir_
> 在选择导入时，假定源码位于指定目录中。

# DESCRIPTION

**goimports** 更新 Go 导入行：添加缺失的导入，移除未被引用的导入。它还会按照与 gofmt 相同的风格格式化代码，因此可以作为 gofmt 的直接替代品。

导入会被分组：标准库在最前，随后是第三方包，组内按字母顺序排序。**-local** 标志可以把项目自身的导入单独分成一组。

# INSTALL

```apt: sudo apt install golang-golang-x-tools```

```brew: brew install goimports```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gofmt](/man/gofmt)(1), [go-fmt](/man/go-fmt)(1), [gofumpt](/man/gofumpt)(1)
