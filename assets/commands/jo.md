# TAGLINE

从 shell 参数创建 JSON

# TLDR

**创建 JSON 对象**

```jo name=[value] count:=[42]```

**创建 JSON 数组**

```jo -a [item1] [item2] [item3]```

**嵌套对象**

```jo name=[test] config=$(jo debug:=[true])```

**从 stdin 读取**

```echo "[value]" | jo name=@-```

**从文件读取**

```jo content=@[file.txt]```

**格式化输出**

```jo -p name=[value]```

# SYNOPSIS

**jo** [_options_] [_key=value_...]

# PARAMETERS

_KEY=VALUE_
> 字符串值赋值。

_KEY:=VALUE_
> 非字符串值（数字、布尔值、null）。

**-a**
> 创建数组而非对象。

**-p**
> 格式化输出。

**@**_FILE_
> 从文件读取值。

**@-**
> 从 stdin 读取值。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jo** 从 shell 参数创建 JSON。它根据命令行键值对构建对象和数组。

该工具让 shell 脚本也能轻松生成 JSON。类型提示可区分字符串与数字、布尔值。

# CAVEATS

注意 shell 引号转义。非字符串请使用 :=。嵌套结构可通过子 shell 实现。

# HISTORY

jo 由 **Jan-Piet Mens** 开发，旨在简化 shell 脚本中的 JSON 创建，免去复杂的引号处理。

# INSTALL

```apt: sudo apt install jo```

```dnf: sudo dnf install jo```

```pacman: sudo pacman -S jo```

```apk: sudo apk add jo```

```zypper: sudo zypper install jo```

```brew: brew install jo```

```nix: nix profile install nixpkgs#jo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jc](/man/jc)(1), [gron](/man/gron)(1)
