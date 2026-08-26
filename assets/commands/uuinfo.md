# TAGLINE

调试和检查唯一标识符（UUID、ULID 等）

# TLDR

**检查一个 UUID**

```uuinfo [01941f29-7c00-7aaa-aaaa-aaaaaaaaaaaa]```

**通过管道从标准输入传入 UUID**

```echo "[some-uuid]" | uuinfo -```

**以 JSON 格式输出**

```uuinfo -o json [id]```

# SYNOPSIS

**uuinfo** [_options_] _ID_

# DESCRIPTION

**uuinfo** 解析并显示复合唯一标识符的详细信息，包括 UUID 版本 1-8、ULID、Snowflake 等。它会显示带颜色标记的位分解、时间戳、熵以及版本信息。支持自动检测和强制指定格式解析。

# HISTORY

**uuinfo** 由 **Ronaldo Ferreira**（Racum）创建，使用 **Rust** 编写。

# SEE ALSO

[uuidgen](/man/uuidgen)(1)
