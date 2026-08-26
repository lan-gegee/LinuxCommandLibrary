# TAGLINE

为 R 提供支持 shebang 的脚本接口

# TLDR

**执行 R 表达式**

```r -e "print('Hello')"```

**运行 R 脚本**

```r [script.R]```

**安装软件包**

```r -e "install.packages('[package]')"```

**向 R 管道输入数据**

```echo "[1,2,3]" | r -e "sum(scan())"```

**带参数运行**

```r [script.R] [arg1] [arg2]```

# SYNOPSIS

**r** [_options_] [_script_] [_args_...]

# PARAMETERS

**-e** _expr_
> 求值表达式。

**-p**
> 打印结果。

**-l** _package_
> 加载软件包。

**-i**
> 交互模式。

**-n**
> 不隐式打印。

**-t**
> 使用临时目录。

**-v**
> 详细输出。

# DESCRIPTION

**littler**（r）为 R 提供了支持 shebang 的脚本接口。它允许从命令行和脚本中运行 R 代码，让 R 更便于 shell 脚本编写和自动化。

littler 通过避免 R 的完整初始化过程，比 R --vanilla 启动更快。

# SHEBANG USAGE

```r
#!/usr/bin/env r

args <- commandArgs(TRUE)
print(paste("Hello", args[1]))
```

# CAVEATS

必须与 R 分开安装。命令 'r' 可能与其他工具冲突。加载软件包会增加启动时间。

# HISTORY

littler 由 **Dirk Eddelbuettel** 和 **Jeff Horner** 于 **2006 年**创建，旨在为 R 提供正式的脚本接口。

# INSTALL

```aur: yay -S littler```

<!-- packages: 2026-07-22 -->

# SEE ALSO
