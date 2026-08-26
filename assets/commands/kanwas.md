# TAGLINE

Kanwas 协作思考空间的 CLI

# TLDR

在当前目录**初始化**新的 Kanwas 工作区

```kanwas init```

把看板上的 markdown **拉取**到本地仓库

```kanwas pull```

把本地修改**推送**回工作区

```kanwas push```

首次使用时通过浏览器 OAuth 进行**身份验证**

```kanwas init```

# SYNOPSIS

**kanwas** _command_ [_options_]

# DESCRIPTION

**kanwas** 是 **Kanwas** 的命令行客户端。Kanwas 是一个开源思考空间，结合了画布、AI 智能体、实时协作和沙盒环境。该 CLI 让用户可以在 Kanwas 工作区和本地 Git 仓库之间同步内容，使生成的 markdown 可以交给 AI 编码智能体（Claude Code、Codex 等）处理，或与源代码一起进行版本控制。

身份验证采用基于浏览器的 OAuth，因此凭据不会以长期 token 的形式存储在本地机器上。

# COMMANDS

**init**
> 初始化新的本地工作区，将其链接到远程 Kanwas 看板并触发 OAuth。

**pull**
> 将工作区的 markdown 表示下载到当前仓库。

**push**
> 将本地 markdown 修改上传回所链接的 Kanwas 看板。

# CAVEATS

该 CLI 属于一个仍在快速演进的平台；命令集合及其标志可能随版本变化。OAuth 需要运行 **kanwas** 的同一台机器上有浏览器，无头服务器可能需要其他登录流程。

# HISTORY

**Kanwas** 由 **kanwas-ai** 组织开发，是一个开源协作思考平台，让人类用户与 AI 智能体在共享画布上协同工作。CLI 的存在是为了把画布内容整合进现有的开发者工作流。

# SEE ALSO

[git](/man/git)(1), [claude](/man/claude)(1)
