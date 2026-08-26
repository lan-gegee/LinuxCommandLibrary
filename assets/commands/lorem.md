# TAGLINE

生成 Lorem Ipsum 占位文本

# TLDR

**生成段落**

```lorem [5]```

**生成句子**

```lorem -s [10]```

**生成单词**

```lorem -w [50]```

**生成字节**

```lorem -b [500]```

**复制到剪贴板**

```lorem [3] | pbcopy```

# SYNOPSIS

**lorem** [_options_] [_count_]

# PARAMETERS

_COUNT_
> 要生成的单位数量。

**-s**
> 生成句子。

**-w**
> 生成单词。

**-b**
> 生成字节。

**-p**
> 生成段落（默认）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lorem** 生成 Lorem Ipsum 占位文本，为设计和开发提供假文本。

该工具可生成标准 Lorem Ipsum 文本的段落、句子或单词。

# CAVEATS

存在多种实现，输出格式各不相同。适用于开发/设计场景。

# HISTORY

Lorem Ipsum 文本源自**西塞罗的《De finibus bonorum et malorum》（论善恶之极）**（公元前 45 年），自 16 世纪起就被用作占位文本。

# INSTALL

```pacman: sudo pacman -S lorem```

```brew: brew install lorem```

```nix: nix profile install nixpkgs#lorem```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shuf](/man/shuf)(1), [fortune](/man/fortune)(1)
