# TAGLINE

PostgreSQL 嵌入式 SQL 预处理器

# TLDR

**预处理嵌入式 SQL 文件**

```ecpg [file.pgc]```

**指定输出文件**

```ecpg -o [output.c] [input.pgc]```

**设置头文件搜索路径**

```ecpg -I [/include/path] [file.pgc]```

**启用兼容模式**

```ecpg -C [INFORMIX] [file.pgc]```

**处理包含嵌入式 SQL 声明的头文件**

```ecpg -h [header.pgh]```

**使用问号**作为参数占位符（Informix 风格）

```ecpg -r [questionmarks] [file.pgc]```

# SYNOPSIS

**ecpg** [_options_] _file_...

# PARAMETERS

**-o** _file_
> 将输出写入文件。

**-I** _directory_
> 头文件搜索路径。

**-c**
> 从 SQL 代码自动生成 C 代码，目前用于 EXEC SQL TYPE 声明。

**-C** _mode_
> 兼容模式：INFORMIX、INFORMIX_SE 或 ORACLE。

**-D** _symbol_[**=**_value_]
> 定义一个 C 预处理器符号。

**-h**
> 处理头文件。隐含 **-c**，并输出 .h 文件而非 .c 文件。

**-i**
> 同时解析系统头文件。

**-r** _option_
> 设置运行时行为：no_indicator、prepare、questionmarks。

**-t**
> 开启事务自动提交。

**-v**
> 打印版本、包含路径及其他构建信息。

**--version**
> 打印版本并退出。

# DESCRIPTION

**ecpg** 是 PostgreSQL 的嵌入式 SQL 预处理器。它将带有嵌入式 SQL 语句的 C 程序转换为调用 ECPG 运行时库的普通 C 代码，后者再通过 libpq 与服务器通信。

该工具读取包含嵌入在 C 代码中的 EXEC SQL 语句的 .pgc 文件，并生成标准 C 文件。默认情况下，`prog.pgc` 的输出会写入 `prog.c`。生成的代码必须针对 **libecpg** 编译和链接（例如 `gcc prog.c -lecpg`），通常还需要 `pg_config --includedir` 给出的包含路径。

# CAVEATS

生成的 C 文件链接的是 libecpg 而非 libpq，因此必须安装 PostgreSQL 客户端开发包。兼容模式会改变 SQL 解析和空值处理方式以匹配 Informix 或 Oracle，为一种模式编写的代码通常无法移植到另一种模式。

# INSTALL

```apt: sudo apt install libecpg-dev```

```apk: sudo apk add libecpg-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [pg_config](/man/pg_config)(1), [postgres](/man/postgres)(1)

# RESOURCES

```[Source code](https://github.com/postgres/postgres)```

```[Homepage](https://www.postgresql.org/)```

```[Documentation](https://www.postgresql.org/docs/current/app-ecpg.html)```

<!-- verified: 2026-07-14 -->
