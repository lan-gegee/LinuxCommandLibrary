# TAGLINE

支持 Markdown 的开源笔记应用

# TLDR

**启动 Joplin 终端应用**

```joplin```

**创建新笔记**

```joplin mknote "[Note Title]"```

**创建新笔记本**

```joplin mkbook "[Notebook Name]"```

**列出所有笔记本**

```joplin ls /```

**列出笔记本中的笔记**

```joplin ls [notebook]```

**在文本编辑器中编辑笔记**

```joplin edit "[note title]"```

**搜索笔记**

```joplin search "[query]"```

**与云端存储同步**

```joplin sync```

**为笔记添加标签**

```joplin tag add "[tag]" "[note title]"```

# SYNOPSIS

**joplin** [_command_] [_options_]

# PARAMETERS

**mknote** _title_
> 创建新笔记。

**mkbook** _name_
> 创建新笔记本。

**ls** [_path_]
> 列出笔记本或笔记。

**edit** _note_
> 在编辑器中编辑笔记。

**cat** _note_
> 显示笔记内容。

**rmnote** _note_
> 删除笔记。

**mv** _note_ _notebook_
> 移动笔记。

**sync**
> 与云端同步。

**tag** _command_ [_tag_] [_note_]
> 管理标签（add、remove、list、notetags）。

**search** _query_
> 搜索笔记。

**import** _path_ [_notebook_]
> 导入数据（支持 md、jex、enex 格式）。

**export** _path_
> 导出数据（支持 jex、md、raw、md_frontmatter 格式）。

**ren** _item_ _name_
> 重命名笔记或笔记本。

**cp** _note_ [_notebook_]
> 将笔记复制到某个笔记本。

**mktodo** _title_
> 创建新的待办事项。

**done** _note_
> 将待办标记为已完成。

**undone** _note_
> 将待办标记为未完成。

**config** _key_ [_value_]
> 获取/设置配置。

**status**
> 显示笔记和笔记本的概要信息。

**use** _notebook_
> 选择默认笔记本。

# DESCRIPTION

**Joplin** 是一款支持 Markdown 的开源笔记应用。终端版通过命令行访问笔记，与桌面端和移动端应用互为补充。

Joplin 支持端到端加密，可通过 Nextcloud/Dropbox/OneDrive/Joplin Cloud 同步，并支持从 Evernote 导入。笔记以 Markdown 格式存储，可以打标签并组织到各个笔记本中。

# SYNC CONFIGURATION

```bash
joplin config sync.target 2  # Nextcloud
joplin config sync.2.path "https://..."
joplin config sync.2.username "user"
```

# CAVEATS

终端版缺少部分图形界面功能。使用同步前需先配置。首次同步可能耗时较久。同时编辑可能出现冲突。

# HISTORY

Joplin 由 **Laurent Cozic** 于 **2017 年**开发，是一款开源的 Evernote 替代品。它强调隐私保护，采用端到端加密和本地优先存储。

# INSTALL

```aur: yay -S joplin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [notable](/man/notable)(1)
