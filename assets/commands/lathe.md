# TAGLINE

在本地生成并阅读动手实践式技术教程

# TLDR

在本地 Web UI 中**呈现**教程

```lathe serve```

**列出**内置的 LLM 技能

```lathe skills list```

向当前项目**安装**技能

```lathe skills install```

为所有项目**安装**技能

```lathe skills install --user```

从内置技能**安装** Cursor 斜杠命令

```lathe skills install --agent cursor```

**显示**可用的写作风格（voice）

```lathe voice list```

**设置**默认的教程 voice

```lathe voice set-default [plainspoken|companion]```

# SYNOPSIS

**lathe** **serve** [_options_]

**lathe** **skills** **install** [_options_]

**lathe** **skills** **list**

**lathe** **voice** **list**

**lathe** **voice** **show** _name_

**lathe** **voice** **set-default** _name_

**lathe** **voice** **add** _name_ **--file** -

# PARAMETERS

**--port** _N_
> **serve** 使用的 HTTP 端口（默认 **4242**）。

**--user**
> 将技能安装到 **~/.claude/skills/**（Claude Code）或 **~/.agents/skills/**（Codex），而不是当前目录。

**--agent** _target_
> 技能安装目标：**cursor**（写入 **.cursor/commands/**）、**codex** 或 **all**。

# DESCRIPTION

**lathe** 是一个 Go 编写的 CLI，附带一组内置的 LLM 技能，可以为自主学习生成分章节的动手实践式技术教程。你在智能体会话中用 **/lathe** 发出提示（例如 **/lathe build a 3D slicer in Erlang**）；技能会写出 Markdown 各章节和元数据，然后由 **lathe serve** 在专用的本地浏览器 UI（**http://localhost:4242**）中渲染出来。

CLI 本身从不调用 LLM。它把教程存储在 **~/.lathe/tutorials/** 目录下（每个 slug 对应一个目录，内有 **metadata.json** 和 **part-NN.md** 文件），对外提供浏览服务，并暴露一组确定性的命令供技能调用（**store**、**verify-result**、**extend-start**、**voice add** 等）。配套技能 **/lathe-extend**、**/lathe-verify**、**/lathe-ask** 和 **/lathe-voice** 则分别用于扩写、验证、提问以及创作自定义的教程 voice。

**lathe skills install** 把内置的 **SKILL.md** 文件复制到 Claude Code、Cursor 或 Codex 中，让斜杠命令可以被发现。voice（**plainspoken**、**companion** 或自定义）决定行文风格；每个教程都会在其元数据和作者署名中记录所用的 voice 以及来源模型。

# CONFIGURATION

教程存储位置：**~/.lathe/tutorials/<slug>/**，其中包含 **metadata.json**（标题、主题、标签、工具、来源、voice、模型、状态）。自定义 voice 通过 **lathe voice add** 保存在 **~/.lathe/voices/** 目录下。默认 HTTP 端口是 **4242**；可在 **serve** 时用 **--port** 覆盖。

# CAVEATS

教程生成的质量取决于你的智能体会话所用的前沿模型。这些技能针对 macOS 上的 Claude Code 进行了调优；Linux 安装请使用 **install.sh** 脚本或 **go install**。Homebrew cask 仅限 macOS。

# SEE ALSO

[go](/man/go)(1), [curl](/man/curl)(1)
