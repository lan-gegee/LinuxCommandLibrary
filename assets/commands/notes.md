# TAGLINE

简单的命令行笔记应用

# TLDR

**创建新笔记**

```notes new "[note title]"```

**列出所有笔记**

```notes ls```

**搜索笔记**

```notes search "[query]"```

**编辑笔记**

```notes edit "[note title]"```

**删除笔记**

```notes rm "[note title]"```

**同步笔记**

```notes sync```

# SYNOPSIS

**notes** _command_ [_options_]

# PARAMETERS

**new** _title_
> 创建新笔记。

**ls**
> 列出笔记。

**search** _query_
> 搜索笔记。

**edit** _title_
> 编辑笔记。

**rm** _title_
> 删除笔记。

**sync**
> 与远程同步。

**cat** _title_
> 显示笔记。

# DESCRIPTION

**notes** 是一个简单的命令行笔记应用。它将笔记存储为纯文本文件，便于管理、搜索和同步。

笔记通常保存在 ~/.notes 或配置的目录中。

# EXAMPLE WORKFLOW

```bash
# Create a note
notes new "meeting-notes"
# Opens editor, save and exit

# List notes
notes ls

# Find notes
notes search "project"

# View note
notes cat "meeting-notes"
```

# CAVEATS

实现各不相同（存在多个名为 "notes" 的工具）。纯文本存储。通过 $EDITOR 配置编辑器。

# HISTORY

存在多种命令行笔记工具；实现者包括 **Nick Nisi** 等，遵循 Unix 哲学——用简单的文本文件进行管理。

# INSTALL

```nix: nix profile install nixpkgs#notes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nb](/man/nb)(1), [jrnl](/man/jrnl)(1), [vim](/man/vim)(1)
