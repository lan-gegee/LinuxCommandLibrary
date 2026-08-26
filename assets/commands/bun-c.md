# TAGLINE

通过 Bun 内置 shell 运行 shell 命令字符串

# TLDR

**运行 shell 命令**

```bun -c "[shell command]"```

**运行管道**

```bun -c "cat [file.txt] | grep [pattern]"```

**从 .env 文件加载环境变量后运行**

```bun -c "[command]" --env-file [.env]```

# SYNOPSIS

**bun** **-c** _command_ [_options_]

# PARAMETERS

**-c** _command_
> 使用 Bun 内置 shell 执行给定的命令字符串。

**--env-file** _file_
> 在执行前从指定文件加载环境变量。

# DESCRIPTION

**bun -c** 运行一段 shell 命令字符串，类似 **sh -c**，但使用的是 Bun 内置的跨平台 shell 实现。它支持管道、重定向和环境变量展开等常见 shell 特性。它可以在执行命令前从 **.env** 文件加载环境变量，因此无需额外工具即可运行依赖环境配置的脚本。

# SEE ALSO

[bun](/man/bun)(1), [bun-run](/man/bun-run)(1), [bun-x](/man/bun-x)(1), [sh](/man/sh)(1)
