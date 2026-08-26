# TAGLINE

记录日常所想的简易命令行日志应用

# TLDR

**快速写一条日志**

```jrnl [Today was a good day.]```

**以指定日期写入日志**

```jrnl [yesterday]: [Had a great meeting.]```

**打开编辑器**撰写更长的内容

```jrnl```

**列出最近的日志**

```jrnl -n [10]```

**搜索**包含指定文本的日志

```jrnl -contains "[search term]"```

**显示带有特定标签的日志**

```jrnl @[tag]```

**显示日期范围内的日志**

```jrnl -from "[2024-01-01]" -to "[2024-01-31]"```

**编辑最后一条日志**

```jrnl --edit -1```

# SYNOPSIS

**jrnl** [_entry_] | [_-n count_] [_-from date_] [_-to date_] [_-contains text_] [_@tag_] [_--edit_] [_--export format_]

# PARAMETERS

**-n**, **--limit** _count_
> 仅显示最近 n 条日志。

**-from** _date_
> 显示此日期之后的日志。

**-to** _date_
> 显示截至此日期的日志。

**-on** _date_
> 显示特定日期的日志。

**-contains** _text_
> 显示包含指定文本的日志。

**-and**
> 要求满足全部过滤条件（默认为任一即可）。

**-starred**
> 仅显示加了星标的日志。

**--edit**
> 在编辑器中打开日志。

**--delete**
> 删除匹配的日志。

**--export** _format_
> 导出日志（json、markdown、text、xml、yaml、tags）。

**--import** _file_
> 从文件导入日志。

**--format** _format_
> 显示用的输出格式。

**--tags**
> 列出所有标签。

**--short**
> 仅显示日志标题。

**--config-override** _key value_
> 覆盖某项配置设置。

**-ls**
> 列出可用的日志库。

# DESCRIPTION

**jrnl** 是一款简单的命令行日志应用，用于记录日常想法、笔记和灵感。它将条目存储为纯文本，因此具有良好的可移植性和持久性。

每条日志由日期、可选标题（第一句）和正文组成。在单词前加 @ 即可创建标签（如 @work、@idea）。第一行或句号前的句子会成为日志标题，并在列表中显示。

快速条目可以直接在命令行输入。不带参数运行 jrnl 则会打开你配置的编辑器，方便撰写较长的内容。日期解析支持自然语言："yesterday"、"last friday"、"2 days ago" 都能被正确识别。

配置保存在 **~/.config/jrnl/jrnl.yaml** 中，定义了日志文件位置、编辑器、加密设置以及多个日志库。你可以维护多个独立的日志库（工作、个人等）并在其间切换。

对于敏感日志，可使用 AES-256 加密，读取和写入都需要密码。日志可以导出为多种格式，便于备份或迁移。

# CAVEATS

纯文本存储意味着不借助 jrnl 也能直接阅读这些条目。加密后每次访问都需输入密码。复杂的日期偶尔可能被错误解析。多日志库需显式选择。没有内置同步——多设备场景请使用文件同步工具。

# HISTORY

**jrnl** 由 Manuel Ebert 于 **2012 年**前后创建，是一款简洁的命令行日志工具。它的灵感来自 Day One 日记应用，但专为偏爱纯文本的终端用户设计。该项目由开源社区维护至今，凭借简洁的设计和对 Unix 哲学的坚持而广受欢迎。

# INSTALL

```dnf: sudo dnf install jrnl```

```pacman: sudo pacman -S jrnl```

```zypper: sudo zypper install jrnl```

```brew: brew install jrnl```

```nix: nix profile install nixpkgs#jrnl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1), [vim](/man/vim)(1), [nano](/man/nano)(1)
