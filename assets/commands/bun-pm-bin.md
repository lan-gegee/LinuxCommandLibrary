# TAGLINE

输出 bin 目录路径

# TLDR

**输出本地 bin 目录**路径

```bun pm bin```

**输出全局 bin 目录**路径

```bun pm bin -g```

# SYNOPSIS

**bun** **pm** **bin** [**-g**]

# PARAMETERS

**-g**, **--global**
> 输出全局 bin 目录而不是本地目录。

# DESCRIPTION

**bun pm bin** 输出软件包可执行文件所在目录的路径。默认显示本地项目的 node_modules/.bin 目录。使用 **-g** 时，则显示全局 bin 目录。

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
