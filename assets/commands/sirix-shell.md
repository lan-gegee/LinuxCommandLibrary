# TAGLINE

SirixDB 的交互式 JSONiq/XQuery shell

# TLDR

**启动**交互式 shell

```sirix-shell```

通过**查询**存储文档（会话示例）

```jn:store('mydb','resource','{"key": "value"}')```

读取已存储的值

```jn:doc('mydb','resource').key```

# SYNOPSIS

**sirix-shell**

# DESCRIPTION

**sirix-shell** 是用于 **SirixDB** 查询的交互式 REPL。它接受多行 JSONiq/XQuery 输入；空行执行语句，Control-D 退出。你可以用它存储和打开文档、运行时态和双时态查询以及探索版本历史，而不必把每个表达式包装成一次性的 **sirix-cli** 调用。

SirixDB 通过 Brackit 扩展了 JSONiq/XQuery，增加了按编号或时间戳打开版本、导航节点历史以及在版本之间计算结构化差异的函数。该 shell 由 **sirix-query** 模块构建，也可以产出 GraalVM 原生二进制以加快启动速度。

# CAVEATS

需要配置好的 SirixDB 环境和 Java 运行时（或原生镜像）。多行输入以空行结束；误输入的空行会执行不完整的语句。脚本化自动化场景请优先使用 **sirix-cli** 而非交互式 shell。

# HISTORY

**sirix-shell** 是开源 **SirixDB** 项目的一部分，使用 Brackit 查询引擎处理 JSONiq/XQuery。

# SEE ALSO

[sirix-cli](/man/sirix-cli)(1), [java](/man/java)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/sirixdb/sirix)```

```[Homepage](https://sirix.io)```

```[Documentation](https://sirix.io/docs/)```

<!-- verified: 2026-07-16 -->
