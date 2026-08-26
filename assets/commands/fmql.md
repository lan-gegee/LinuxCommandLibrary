# TAGLINE

使用类 SQL 语言查询和管理文件

# TLDR

在目录中**查找**所有文本文件

```fmql sql "[SELECT * FROM ~/Documents WHERE extension = 'txt']"```

**递归**进入子目录

```fmql sql "[WITH RECURSIVE SELECT name, size FROM ~/projects WHERE extension = 'rs']"```

**查找**较大且最近修改过的图片

```fmql sql "[SELECT * FROM ~/Pictures WHERE (extension = 'jpg' OR extension = 'png') AND size > 1000000 AND modified > '2026-01-01']"```

按大小**降序排列**结果

```fmql sql "[SELECT name, size FROM ~/Downloads ORDER BY size DESC]"```

用正则表达式**匹配**文件名

```fmql sql "[SELECT * FROM ~/logs WHERE name REGEXP '^app-[0-9]+\\.log$']"```

**更新**目录下每个 Shell 脚本的权限

```fmql sql "[UPDATE ~/scripts SET permissions = '755' WHERE extension = 'sh']"```

# SYNOPSIS

**fmql** **sql** "_QUERY_"

# PARAMETERS

**sql** _QUERY_
> 对文件系统执行类 SQL 查询。

# QUERY LANGUAGE

**SELECT** _columns_ **FROM** _path_ [**WHERE** _condition_] [**ORDER BY** _column_ [ASC|DESC]]
> 匹配 _path_ 中的文件并返回所选属性。

**WITH RECURSIVE SELECT** _columns_ **FROM** _path_ ...
> 与 **SELECT** 相同，但会递归进入子目录。

**UPDATE** _path_ **SET** _attribute_ = _value_ **WHERE** _condition_
> 修改每个匹配文件的属性（目前支持权限及类似的可变元数据）。

# QUERYABLE ATTRIBUTES

**name**
> 文件名，包括扩展名。

**extension**
> 不带点号的文件扩展名。

**size**
> 以字节为单位的大小。

**modified**
> 最后修改时间戳；可与 ISO-8601 日期字符串进行比较。

**permissions**
> Unix 权限位，以八进制或符号形式字符串表示。

**executable**
> 布尔值：文件是否设置了可执行位。

# OPERATORS

```
=    !=    <    >    <=    >=
LIKE        SQL-style wildcard match (% and _)
REGEXP      Regular-expression match
AND   OR   NOT
```

# CAVEATS

**fmql** 是一个小型的 Rust 实验项目——它的 SQL 方言只是"某种程度上的"SQL，并非完整的查询引擎。看起来在真正的 RDBMS 中有效的查询可能被拒绝。操作是在本地文件系统上串行执行的，因此针对超大目录树的递归查询可能较慢。**UPDATE** 会修改真实文件；请先用 **SELECT** 测试，并在批量更改权限之前做好备份。

# HISTORY

**fmql** 由 **Chris Mann**（**chriswmann**）用 **Rust** 编写，发布于 **github.com/chriswmann/fmql**，并以 **fmql** crate 的形式发布在 **crates.io** 上。它是一个围绕 SQL 解析与文件系统操作相结合的学习型练习项目。

# SEE ALSO

[find](/man/find)(1), [fd](/man/fd)(1), [stat](/man/stat)(1), [chmod](/man/chmod)(1), [sqlite3](/man/sqlite3)(1)
