# TAGLINE

基于终端的打字速度测试

# TLDR

**开始打字测试**，默认 50 个单词

```tt```

**以自定义单词数开始测试**

```tt -n [100]```

**以限时模式开始测试**（秒）

```tt -t [60]```

**使用引语模式**并选用英语引语

```tt -quotes en```

**将单词分组**为多个片段

```tt -n [50] -g [10]```

**应用自定义主题**

```tt -theme [gruvbox]```

**使用自定义词表**

```tt -words [english1000]```

**将结果记录到 CSV**

```tt -csv >> [~/wpm.csv]```

# SYNOPSIS

**tt** [_options_] [_file_]

# PARAMETERS

**-n** _number_
> 测试的单词数量（默认：50）

**-t** _seconds_
> 测试的时间限制（秒）

**-g** _number_
> 将单词按指定大小分组

**-quotes** _name_
> 启用引语模式，使用指定的引语列表

**-words** _name_
> 使用自定义或内置词表

**-theme** _name_
> 应用自定义或内置主题

**-csv**
> 以 CSV 格式输出结果

**-raw**
> 面向脚本的原始输出模式

**-showwpm**
> 打字时实时显示 WPM

**-help**
> 显示帮助信息

# DESCRIPTION

**tt** 是一个用 Go 编写的终端打字测试工具。它从随机选择的单词生成测试内容，并测量打字速度和准确率。默认使用最常见的 1000 个英文单词。

给定文件路径时，tt 会以该文件作为输入，将每个段落视为一个独立的测试片段。这样可以用自定义文本或代码示例进行练习。

每次测试结束后，tt 会显示统计数据，包括每分钟字符数（CPM）、每分钟单词数（WPM）、准确率百分比以及具体的错误。结果可以记录到 CSV 中，便于长期跟踪进度。

自定义主题和词表可放在 **~/.tt/themes** 和 **~/.tt/words** 目录中。该工具设计上支持脚本化，便于与其他 Unix 工具集成。

# KEY BINDINGS

**Escape**
> 重启当前测试

**Ctrl+C**
> 退出

**Right Arrow**
> 下一题

**Left Arrow**
> 上一题

# CAVEATS

tt 需要正确支持 Unicode 的终端才能准确显示字符。过窄的终端可能影响换行和显示效果。默认词表侧重常见英文单词；程序员可能需要包含符号的自定义词表。

# HISTORY

**tt** 由 **lemnos** 创建，托管在 GitHub 上。它用 **Go** 编写，设计目标是一个极简、可脚本化的打字测试工具，面向那些偏好命令行工具而非 monkeytype 或 typeracer 等网页应用的终端用户。

# INSTALL

```brew: brew install tt```

```nix: nix profile install nixpkgs#tt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyper](/man/ttyper)(1), [gtypist](/man/gtypist)(1), [typespeed](/man/typespeed)(1)
