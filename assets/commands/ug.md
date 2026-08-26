# TAGLINE

支持配置文件、美观输出和排序结果的 ugrep

# TLDR

**在文件中搜索模式**

```ug "[pattern]" [file]```

**在当前目录递归搜索**

```ug -r "[pattern]"```

**忽略大小写搜索**

```ug -i "[pattern]" [file]```

**显示行号**

```ug -n "[pattern]" [file]```

**交互式 TUI 查询模式**

```ug -Q```

**统计每个文件的匹配数**

```ug -c "[pattern]" [file]```

**只列出包含匹配的文件名**

```ug -l "[pattern]"```

**只匹配完整单词**

```ug -w "[pattern]" [file]```

# SYNOPSIS

**ug** [_options_] [_pattern_] [_file_...]

# PARAMETERS

**-i**
> 忽略大小写匹配。

**-r**, **-R**
> 递归搜索（-R 会跟随符号链接）。

**-n**
> 显示行号。

**-Q**
> 启动交互式 TUI 查询模式。

**-c**
> 统计每个文件中匹配的行数。

**-l**
> 只打印包含匹配内容的文件名。

**-w**
> 只匹配完整单词。

**-e** _pattern_
> 指定一个模式（多次使用表示取并集）。

**--no-config**
> 不加载 .ugrep 配置文件。

# DESCRIPTION

**ug** 是 **ugrep** 的用户友好前端。它等价于运行 `ugrep --config --pretty --sort`：自动从工作目录或主目录加载 `.ugrep` 配置文件、启用美化的彩色输出，并按文件名排序结果。这些默认设置使 ug 适合在终端中交互使用。

与普通 **ugrep** 不同（后者面向脚本化和批处理场景，为性能考虑不排序），ug 为探索式搜索做了调优。它支持所有 ugrep 选项，包括布尔查询、模糊匹配、十六进制转储以及在归档和压缩文件内部搜索。

交互式 TUI 模式（`-Q`）让你输入查询的同时实时看到结果更新。

# INSTALL

```apt: sudo apt install ugrep```

```dnf: sudo dnf install ugrep```

```pacman: sudo pacman -S ugrep```

```apk: sudo apk add ugrep```

```zypper: sudo zypper install ugrep```

```brew: brew install ugrep```

```nix: nix profile install nixpkgs#ugrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ugrep](/man/ugrep)(1), [grep](/man/grep)(1), [rg](/man/rg)(1)
