# TAGLINE

Go 源代码格式化工具

# TLDR

**格式化 Go 文件**并打印到标准输出

```gofmt [file.go]```

**格式化并覆盖**原文件

```gofmt -w [file.go]```

递归**格式化一个目录中的所有 Go 文件**

```gofmt -w [path/to/directory]```

显示格式化**更改的差异**

```gofmt -d [file.go]```

**列出将被修改**的文件

```gofmt -l [path/to/directory]```

在格式化的同时**简化代码**

```gofmt -s [file.go]```

就地**格式化并简化**

```gofmt -s -w [file.go]```

# SYNOPSIS

**gofmt** [_FLAGS_] [_PATH_...]

# PARAMETERS

**-w**
> 将结果写回源文件而不是打印到标准输出。

**-d**
> 显示差异而不重写文件。

**-l**
> 列出格式与 gofmt 输出不一致的文件。

**-s**
> 简化代码（应用简化规则）。

**-e**
> 报告所有错误（而不是每个文件只报前 10 个）。

**-r** _RULE_
> 应用重写规则（例如 'a[b:len(a)] -> a[b:]'）。

# DESCRIPTION

**gofmt** 按照 Go 标准风格规范格式化 Go 源码。它使用制表符缩进、空格对齐，确保所有 Go 代码库的格式保持一致。

不带路径调用时，它从标准输入读取。给定文件或目录参数时，它会递归处理这些路径。**-s** 标志会应用简化转换，例如删除多余的类型声明。**-r** 标志支持通过自定义重写规则对代码进行变换。

# CAVEATS

gofmt 强制执行 Go 的官方风格，不提供花括号位置、制表符宽度等风格偏好方面的配置选项。文件必须是语法有效的 Go 代码。需要整理导入（import）时，请改用同样能处理导入的 **goimports**。

# HISTORY

gofmt 作为 Go 编程语言的一部分问世，由 Google 于 **2009 年**首次发布。随语言附带你无法调整风格的官方格式化工具是刻意为之的设计，目的是终结 Go 项目中关于代码风格的争论。这种"唯一风格"的思路得到了广泛采纳，并影响了其他语言创建类似的工具（rustfmt、prettier、black）。

# INSTALL

```apt: sudo apt install gccgo-go```

```dnf: sudo dnf install gcc-go```

```pacman: sudo pacman -S gcc-go```

```apk: sudo apk add gcc-go```

```zypper: sudo zypper install gcc-go```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[goimports](/man/goimports)(1), [go](/man/go)(1), [golint](/man/golint)(1), [staticcheck](/man/staticcheck)(1)
