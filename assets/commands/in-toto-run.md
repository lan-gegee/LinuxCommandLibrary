# TAGLINE

执行命令的同时记录供应链元数据

# TLDR

**运行并记录命令**

```in-toto-run -n [step_name] -k [key.pem] -- [command]```

**记录输入物和产物**

```in-toto-run -n [build] -k [key] -m [src/] -p [dist/] -- make```

**排除模式**

```in-toto-run -n [step] -k [key] --exclude [*.log] -- ./build.sh```

**只记录不执行**

```in-toto-run -n [step] -k [key] -m [files] -p [files]```

# SYNOPSIS

**in-toto-run** [_options_] [-- _command_]

# PARAMETERS

**-n** _NAME_
> 链接元数据中的步骤名称。

**-k** _KEY_
> 用于签名的私钥。

**-m** _MATERIALS_
> 要记录的输入物。

**-p** _PRODUCTS_
> 要记录的产物（输出）。

**--exclude** _PATTERN_
> 排除匹配模式的文件。

**-c** _COMMAND_
> 要运行的命令（-- 的替代方式）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**in-toto-run** 执行一条命令并同时记录供应链元数据。它在执行前捕获输入物、执行后捕获产物，并创建一个经过签名的链接文件。

该工具是 in-toto 供应链安全的核心。每个链接都以加密方式证明了某个构建步骤拥有哪些输入和输出。

# CAVEATS

需要签名密钥。链接必须与布局匹配。基于 Python 的工具。

# HISTORY

in-toto-run 是 **in-toto** 中主要的记录工具，该框架由 **纽约大学** 开发，用于保护软件供应链完整性。

# SEE ALSO

[in-toto-record](/man/in-toto-record)(1), [in-toto-sign](/man/in-toto-sign)(1)
