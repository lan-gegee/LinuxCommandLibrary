# TAGLINE

基于 Markdown 的笔记应用

# TLDR

**启动 Notable**

```notable```

**打开指定的数据目录**

```notable --data-dir [~/notes]```

**导入笔记**

```notable --import [notes/]```

# SYNOPSIS

**notable** [_options_]

# PARAMETERS

**--data-dir** _path_
> 笔记目录。

**--import** _path_
> 导入笔记。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**Notable** 是一款基于 Markdown 的笔记应用。它将笔记保存为纯 Markdown 文件，支持标签、附件，并提供简洁的编辑界面。

Notable 提供基于 Electron 构建的桌面应用版本。

# FEATURES

```
- Markdown notes
- Tags and notebooks
- Split editor/preview
- KaTeX math support
- Mermaid diagrams
- Multi-note editor
```

# DATA STRUCTURE

```
notes/
├── Notes/           # Markdown files
├── Attachments/     # Attached files
└── notable.json     # Metadata
```

# CAVEATS

基于 Electron（资源占用较高）。免费版有功能限制。笔记仅存储在本地。

# HISTORY

Notable 由 **Fabio Spampinato** 于 **2018 年**创建，是一款受 Sublime Text 启发、原生使用 Markdown 的笔记应用。

# INSTALL

```nix: nix profile install nixpkgs#notable```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[joplin](/man/joplin)(1), [obsidian](/man/obsidian)(1)
