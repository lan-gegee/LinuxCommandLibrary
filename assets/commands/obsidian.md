# TAGLINE

基于 Markdown 的知识库和笔记应用

# TLDR

**启动 Obsidian**

```obsidian```

**按名称打开特定仓库**

```obsidian "obsidian://open?vault=[vault_name]"```

**打开仓库中的特定文件**

```obsidian "obsidian://open?vault=[vault_name]&file=[path/to/note]"```

**在仓库中新建笔记**

```obsidian "obsidian://new?vault=[vault_name]&name=[note_name]"```

**创建带内容的笔记**

```obsidian "obsidian://new?vault=[vault_name]&name=[note_name]&content=[Hello world]"```

**在仓库内搜索**

```obsidian "obsidian://search?vault=[vault_name]&query=[search_term]"```

# SYNOPSIS

**obsidian** [_options_] [_URI_]

# PARAMETERS

**--version**
> 打印版本信息并退出。

**--help**
> 显示帮助信息。

**--disable-gpu**
> 禁用 GPU 硬件加速。

**--enable-logging**
> 启用输出到控制台的日志。

# URI ACTIONS

**obsidian://open**
> 打开仓库或文件。参数：**vault**（名称或 ID）、**file**（相对于仓库根目录的路径）、**path**（绝对文件系统路径）。

**obsidian://new**
> 创建新笔记。参数：**vault**、**name**（笔记名称）、**content**（笔记正文）、**overwrite**（设为 true 时覆盖已有笔记）、**append**（设为 true 时若已存在则追加）。

**obsidian://search**
> 打开带查询的搜索面板。参数：**vault**、**query**（搜索字符串）。

**obsidian://hook-get-address**
> 获取当前笔记的名称和 URI，供基于链接的自动化工具使用。

# DESCRIPTION

**Obsidian** 是一款知识管理和笔记应用，直接操作本地的纯 Markdown 文件文件夹。它强调笔记之间的链接，以构建个人知识图谱，并以交互式图谱视图呈现。所有数据都以明文形式存储在本地，使笔记不会过时，且可以用任何文本编辑器访问。

该应用拥有丰富的插件生态，包括反链、标签、模板、每日笔记和 Canvas 白板等核心插件，还有社区插件市场。仓库（vault）是基本的组织单位，每个仓库对应文件系统上的一个目录。

Obsidian 使用 URI 协议（**obsidian://**）实现应用间通信和自动化，允许外部脚本和工具打开仓库、创建笔记并执行搜索。

# CAVEATS

Obsidian 是**专有软件**，个人使用免费；商业使用需要付费许可。该应用基于 Electron 构建，内存占用高于原生替代品。社区插件拥有完整的本地文件系统访问权限，安装前应加以审查。设备间同步需要使用 Obsidian Sync（付费）或 Git、Syncthing 等第三方方案。

# HISTORY

Obsidian 由 **Shida Li** 和 **Erica Xu** 创建，两人此前开发了 Dynalist（一款大纲工具）。首个公开发布版本于 **2020 年 3 月**推出。凭借本地优先的设计和可扩展的插件系统，它迅速积累了庞大的社区。Obsidian **1.0** 于 **2022 年 10 月**发布，加入了许多重要功能，包括 Canvas 视图。iOS 和 Android 移动版于 **2021 年 7 月**发布。

# INSTALL

```pacman: sudo pacman -S obsidian```

```nix: nix profile install nixpkgs#obsidian```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [joplin](/man/joplin)(1)
