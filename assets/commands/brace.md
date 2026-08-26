# TAGLINE

用于分组与展开的 Shell 语法

# TLDR

**命令分组（当前 Shell）**

```{ [command1]; [command2]; }```

**花括号展开**

```echo {a,b,c}```

**序列展开**

```echo {1..10}```

**带步长的序列展开**

```echo {0..20..5}```

**参数展开**

```echo ${var}```

**创建多个文件**

```touch file{1,2,3}.txt```

# SYNOPSIS

**{** _commands_**;** **}**

**{**_a_**,**_b_**,**_c_**}**

**{**_start_**..**_end_**}**

**${**_parameter_**}**

# DESCRIPTION

**{ }**（花括号）在 shell 中有多种用途：

**命令分组**：**{ cmd1; cmd2; }** 将命令组合起来在当前 shell 中运行（不同于会启用子 shell 的 **(...)**）。要求 **{** 后有空格，且 **}** 前有分号。

**花括号展开**：**{a,b,c}** 展开为 **a b c**。适合生成列表：
- **file{1,2,3}** → **file1 file2 file3**
- **{a..z}** → 字母表
- **{1..10}** → 数字 1 到 10
- **{01..10}** → 零填充形式：01 02 ... 10
- **{0..20..5}** → 步长/增量（bash 4.0+）：0 5 10 15 20

**参数展开**：**${var}** 访问变量，以下场景必须使用：
- 数组访问：**${array[0]}**
- 修饰符：**${var:-default}**
- 消除歧义：**${var}text**

# EXAMPLES

```bash
# Group with redirect
{ echo "line1"; echo "line2"; } > file.txt

# Brace expansion for backups
cp config.{txt,bak}

# Generate sequences
mkdir dir{01..12}
echo {A..Z}

# Nested expansion
echo {a,b}{1,2}  # a1 a2 b1 b2
```

# CAVEATS

命令分组要求 **{** 后有空格且 **}** 前有分号：应写成 **{ cmd; }** 而不是 **{cmd}**。

花括号展开不是通配符展开——它发生在其他展开之前，并且不会检查文件是否存在。

find 命令中的 **{}** 是替换字符串，不是花括号展开。

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [zsh](/man/zsh)(1)
