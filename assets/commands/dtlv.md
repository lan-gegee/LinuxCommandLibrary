# TAGLINE

Datalevin 数据库的 CLI、REPL 与服务器

# TLDR

**启动**交互式 Datalevin REPL

```dtlv```

**显示**所有命令的帮助

```dtlv help```

**作为网络服务器运行**

```dtlv serv```

**复制**（备份）数据库目录，并压缩使用中的页

```dtlv -d [source_db_dir] -c copy [dest_db_dir]```

**转储** Datalog 数据库到文件

```dtlv -d [db_dir] -g -f [dump_file] dump```

**在脚本中对数据库执行** Clojure 代码

```dtlv exec '(def conn (get-conn "/tmp/db")) (q (quote [:find ?e :where [?e :name _]]) @conn) (close conn)'```

**通过 stdio 运行**本地 MCP 服务器

```dtlv mcp```

# SYNOPSIS

**dtlv** [_options_] [_command_] [_arguments_]

# DESCRIPTION

**dtlv** 是 **Datalevin** 的原生命令行工具。Datalevin 是一个构建在 LMDB 之上的持久化 Datalog 数据库。这一个二进制文件就涵盖了交互式 Clojure REPL、面向 shell 的数据库维护、查询/事务执行、可选的网络服务器，以及面向 AI 客户端的 stdio MCP 服务器。

不带参数（或带 **repl**）时，**dtlv** 会启动一个基于 SCI 的交互式控制台，Datalevin 的公开函数无需引入命名空间即可直接使用——与库中使用的 Clojure API 相同。**exec** 从参数或标准输入执行代码，适合脚本化。维护命令包括 **copy**（支持热备份的复制，可选压缩）、**dump**/**load**（文本或 nippy 格式的导出/导入）、**drop** 和 **stat**。**serv** 监听客户端连接（默认 **127.0.0.1:8898**，POSIX 上数据根目录为 **/var/lib/datalevin**）。**mcp** 通过 Model Context Protocol（模型上下文协议）对外提供 Datalevin 服务。

可通过 Homebrew（**huahaiy/brew/datalevin**）、发布版二进制文件、Docker（**huahaiy/datalevin**）或 JVM uberjar 安装。同一个可执行文件还可以作为 Babashka pod 加载。

# PARAMETERS

**repl**
> 进入交互式 shell（未给出命令时的默认行为）。

**exec** [_code_]
> 从参数或标准输入执行 Datalevin/Clojure 代码。

**copy**
> 复制数据库目录。需要用 **-d** 指定源路径；目标路径作为参数传入。**-c**/**--compact** 只复制使用中的页。

**dump**
> 将数据库内容转储到标准输出或 **-f** 指定的文件。**-g** 仅 Datalog；**-n** nippy 二进制格式；**-a** 所有子数据库；**-l** 列出子数据库名称。

**load**
> 从标准输入或 **-f** 指定的文件加载数据到 **-d** 指定的数据库。

**drop**
> 清空或（**-D**）删除子数据库。

**stat**
> 显示数据库统计信息。

**serv**
> 作为服务器运行。**--host**、**-p**/**--port**、**-r**/**--root**、**-v** 详细输出。

**mcp**
> 通过 stdio 运行 MCP 服务器。**-w**/**--allow-writes** 启用写入工具（默认关闭）。

**help** [_command_]
> 显示用法。

**-d**, **--dir** _PATH_
> 数据库目录路径。

**-f**, **--file** _PATH_
> dump/load 及相关操作的输入/输出文件。

**-V**, **--version**
> 显示 Datalevin 版本并退出。

# CAVEATS

原生 **dtlv** 使用 GraalVM SerialGC 构建，对于长期运行的高并发服务器可能不如 JVM uberjar 合适。将 **serv** 绑定到非环回地址需要设置 **DATALEVIN_DEFAULT_PASSWORD**。任何对外暴露的部署都必须更改默认服务器账户凭据。在启用 **--allow-writes** 之前，**mcp** 的写入工具始终保持禁用。

# HISTORY

Datalevin 是由 Huahai Yang 及贡献者开发的开源 Datalog 存储（Eclipse 公共许可证），致力于以有竞争力的查询性能提供简单持久的 Datalog。**dtlv** 原生镜像和服务器模式在项目路线图早期就已落地，至今仍是主要的运维接口。

# SEE ALSO

[bb](/man/bb)(1), [sqlite3](/man/sqlite3)(1), [java](/man/java)(1)

# RESOURCES

```[Source code](https://github.com/datalevin/datalevin)```

```[Homepage](https://datalevin.org)```

```[Documentation](https://github.com/datalevin/datalevin/blob/master/doc/dtlv.md)```

<!-- verified: 2026-07-22 -->
