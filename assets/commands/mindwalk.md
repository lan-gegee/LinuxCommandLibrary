# TAGLINE

在你的代码库 3D 地图上回放编码智能体会话

# TLDR

**安装并启动**（扫描 Claude Code 和 Codex 会话目录）

```mindwalk```

**在固定端口提供 UI 服务**而不打开浏览器

```mindwalk serve --port [8765] --no-open```

**打开**一个会话文件

```mindwalk open [path/to/session.jsonl]```

**构建**仓库城市地图 JSON

```mindwalk build [path/to/repo] -o [out.json]```

**将会话规范化**为 trace

```mindwalk trace [session] -o [out.json]```

用本地智能体 CLI 作为评审来**评估**会话

```mindwalk analyze [session] --judge [claude|codex]```

# SYNOPSIS

**mindwalk** [_command_] [_options_] [_args_]

# DESCRIPTION

**mindwalk** 可视化编码智能体探索仓库的过程。它读取本地 Claude Code 和 Codex 会话日志，构建仓库的确定性布局（"城市地图"），并将文件读取、编辑和搜索操作以光的形式回放到浏览器的 3D 地图上。

不带参数运行时，它会扫描默认的会话目录，在随机端口上提供本地 UI，并打开浏览器。查看完全在本地进行；可选的 **mindwalk analyze**（或 Evaluate 面板）可以将会话摘要发送给你自己的 **claude** 或 **codex** CLI 进行评审。

# PARAMETERS

**serve**
> 启动本地服务器（**--port**、**--no-open**、**--claude-dir**、**--codex-dir**）

**open** _session.jsonl_
> 打开特定会话（**--no-open** 跳过打开浏览器）

**build** _repo_
> 写出城市地图 JSON（**-o** 输出路径）

**trace** _session_
> 写出规范化的 trace JSON

**analyze** _session_
> LLM 评审评估（**--judge**、**--model**）

# CAVEATS

会话评估为可选项，使用你本地的智能体 CLI，可能会将该会话的摘要发送到你账户背后的模型。报告缓存在 **~/.mindwalk/reports** 下。

# SEE ALSO

[claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/cosmtrek/mindwalk)```

<!-- verified: 2026-07-14 -->
