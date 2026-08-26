# TAGLINE

在终端中管理 Obsidian 仓库和笔记的 TUI

# TLDR

**启动 basalt** 以选择并打开一个 Obsidian 仓库

```basalt```

**通过 Cargo 安装**

```cargo install basalt-tui```

# SYNOPSIS

**basalt**

# DESCRIPTION

**basalt** 是一款跨平台终端用户界面（TUI），可直接在命令行中管理 Obsidian 仓库和笔记。它提供极简界面，带有渲染后的 markdown 预览、受 vim 启发的导航以及实验性的内置编辑器。

界面由三个主窗格组成：左侧用于浏览笔记和文件夹的 **Explorer** 窗格、中间以渲染 markdown 阅读笔记的 **Note Editor** 窗格，以及右侧用于在笔记内导航标题的 **Outline** 窗格。同一时间只有一个窗格获得焦点，以更粗的边框表示。

basalt 渲染 CommonMark 和 GitHub Flavored Markdown，包括标题、列表、任务列表、代码块、引用块、Obsidian 风格的 callout、wiki 链接和行内代码。导航采用 vim 风格按键绑定：**j**/**k** 或方向键移动，**Tab**/**Shift+Tab** 切换窗格，**Enter** 打开笔记，**t** 切换资源管理器，**Ctrl+O** 切换大纲，**Ctrl+U**/**Ctrl+D** 半页滚动，**s** 切换排序方式，**r** 重命名笔记或文件夹。重命名笔记时，仓库中所有引用该笔记的 wiki 链接都会自动更新。

全局快捷键包括：**q** 退出，**?** 打开帮助弹窗，**Ctrl+G** 打开仓库选择器以便在不同 Obsidian 仓库间切换。可以配置自定义命令来启动外部编辑器或应用，使用 **exec:** 和 **spawn:** 前缀及动态变量 **%vault**、**%note**、**%note_path**。

使用 Rust 构建，以 ratatui 进行终端渲染，pulldown-cmark 解析 markdown。项目分为三个 crate：负责领域逻辑的 **basalt-core**、可复用 TUI 组件库 **basalt-widgets**，以及主应用 **basalt-tui**。

# CONFIGURATION

配置使用 TOML 文件。按发现顺序，第一个文件优先生效：

**macOS/Linux:**
> **$HOME/.basalt.toml** 或 **$XDG_CONFIG_HOME/basalt/config.toml**

**Windows:**
> **%USERPROFILE%\\.basalt.toml** 或 **%APPDATA%\\basalt\\config.toml**

**顶层设置：**
> **experimental_editor** = true/false -- 启用实验性内置编辑器（默认：false）
> **vim_mode** = true/false -- 激活类 vim 按键绑定预设（默认：false）

**区段：**
> **[global]** -- 应用于整个应用的通用按键绑定
> **[explorer]** -- Explorer 窗格的按键绑定与行为
> **[outline]** -- Outline 窗格的按键绑定
> **[note_editor]** -- Note Editor 窗格的按键绑定
> **[input_modal]** -- 输入弹窗的按键绑定
> **[help_modal]** -- 帮助弹窗的按键绑定
> **[vault_selector_modal]** -- 仓库选择器的按键绑定

每个键映射遵循格式：**{ key = "binding", command = "action" }**。自定义命令使用 **exec:** 同步执行，或使用 **spawn:** 异步启动。

# CAVEATS

该应用仍在积极开发中。图片、表格、水平分割线、脚注和 HTML 内容不会被渲染。外部链接不可点击。代码块不支持语法高亮。行内文本样式（粗体、斜体、删除线）会被解析，但在终端中不会进行视觉渲染。

文件操作有限：不支持创建、删除、移动、复制和搜索笔记。仅提供重命名和排序功能。

实验性编辑器有较大局限：无撤销/重做、无剪贴板支持、无文本选择、无法多行删除，且编辑模式的按键绑定不可自定义。它以单个块而非完整文档为单位进行操作。

自定义命令不支持管道、重定向和命令替换等 Shell 特性。Obsidian 插件、关系图谱和反向链接面板均不可用。

# HISTORY

**basalt** 由 **Erik Juhani Nylund** 创建，仓库建立于 **2023 年 9 月**。首个公开发布版（v0.3.7）发布于 **2025 年 5 月**。项目用 Rust 编写，采用 MIT 许可证。截至 2026 年初，已有超过 30 个发行版本和约 1000 个 GitHub 星标。

# INSTALL

```aur: yay -S basalt```

```nix: nix profile install nixpkgs#basalt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[obsidian](/man/obsidian)(1), [glow](/man/glow)(1), [vim](/man/vim)(1), [nvim](/man/nvim)(1)
