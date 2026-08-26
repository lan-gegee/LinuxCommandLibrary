# TAGLINE

GitHub Copilot CLI 自定义智能体调用

# TLDR

以自定义智能体**启动交互式 Copilot CLI 会话**

```gh copilot --agent [agent_name]```

以自定义智能体配合提示词非交互式运行

```gh copilot --agent [security-auditor] --prompt "[Check /src/app/validator.go]"```

通过斜杠命令交互式调用智能体

```/agent [agent_name]```

**把任务委派给 Copilot 编码智能体**

```/delegate [task description]```

# SYNOPSIS

**gh** **copilot** **--agent** _name_ [**--prompt** _text_] [_options_]

# PARAMETERS

**--agent** _name_
> 指定要使用的自定义智能体（与 .agent.md 文件名匹配）。

**--prompt** _text_
> 为程序化（非交互式）用法提供提示词。

**--allow-tool** _tool_
> 指定智能体可以使用的工具（shell、write、url、MCP 服务器工具）。

# DESCRIPTION

**gh agent** 功能由 GitHub Copilot CLI 的自定义智能体系统提供，可通过 `gh copilot --agent` 或交互式会话中的 `/agent` 斜杠命令访问。智能体由扩展名为 `.agent.md` 的 Markdown 文件定义，其中规定了智能体的名称、描述、提示指令和可用工具。

自定义智能体可在用户级（~/.copilot/agents/）、仓库级（.github/agents/）或组织级（{org}/.github/agents/）定义。命名冲突时，用户级智能体优先于仓库级，仓库级又优先于组织级。

`/delegate` 斜杠命令会把未暂存的更改提交到新分支，并将任务委派给 Copilot 编码智能体；后者会打开一个草稿 pull request 并在后台开展工作。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-copilot](/man/gh-copilot)(1), [gh](/man/gh)(1)
