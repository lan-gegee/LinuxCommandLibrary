# TAGLINE

人性化的 cut 和 awk 替代品

# TLDR

**选取第一个字段**

```echo "one two three" | choose 0```

**选取第三个字段**

```echo "a b c d e" | choose 2```

**选取字段范围**

```echo "a b c d e" | choose 1:3```

**从末尾选取（最后一个字段）**

```echo "a b c d e" | choose -1```

**选取最后三个字段**

```echo "a b c d e" | choose -3:```

**自定义字段分隔符**

```echo "a,b,c" | choose -f ',' 1```

**正则字段分隔符**

```echo "a1b2c" | choose -f '[0-9]' 0:```

**选取排他范围**

```echo "a b c d e" | choose 1:4 --exclusive```

# SYNOPSIS

**choose** [_options_] _field_[_:end_]

# DESCRIPTION

**choose** 是一个人性化且快速的文本字段选取工具，可替代 **cut** 和 **awk**。它采用类 Python 的切片语法：从零开始索引、负数索引表示从末尾计数，默认范围为闭区间。

与需要精确指定分隔符且从 1 开始索引的 **cut** 不同，choose 会自动处理空白分割，还支持基于正则表达式的字段分隔符。它用 Rust 编写，在简单的字段选取任务上比 awk 快得多。

# PARAMETERS

**-f**, **--field-separator** _sep_
> 字段分隔符（支持正则表达式）

**-o**, **--output-field-separator** _sep_
> 输出分隔符（默认：空格）

**-x**, **--exclusive**
> 从范围中排除结束索引

**-c**, **--character-wise**
> 按字符而非字段选取

**-n**, **--non-greedy**
> 使用非贪婪的字段分割

# FIELD SYNTAX

**N**
> 单个字段（从 0 开始索引）

**N:M**
> 从 N 到 M 的范围（含端点）

**N:**
> 从 N 到末尾

**:M**
> 从开头到 M

**-N**
> 倒数第 N 个字段

# CAVEATS

从零开始索引（第一个字段为 0）。处理长输入时比 cut 快，比 awk 快得多。可通过 cargo 或 brew install choose-rust 安装。

# INSTALL

```pacman: sudo pacman -S choose```

```apk: sudo apk add choose```

```zypper: sudo zypper install choose```

```nix: nix profile install nixpkgs#choose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cut](/man/cut)(1), [awk](/man/awk)(1), [sed](/man/sed)(1)

# RESOURCES

```[Source code](https://github.com/theryangeary/choose)```

<!-- verified: 2026-06-22 -->
