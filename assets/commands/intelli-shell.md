# TAGLINE

Shell 的 IntelliSense 风格命令模板管理器

# TLDR

**交互式搜索已保存的命令（shell 快捷键）**

```# Press Ctrl+Space in your shell```

**收藏最近执行的命令（shell 快捷键）**

```# Press Ctrl+B in your shell```

**用 AI 修复当前命令（shell 快捷键）**

```# Press Ctrl+X in your shell```

**从 CLI 添加命令模板**

```intelli-shell new "[command_template]" -d "[description]"```

**从 CLI 搜索命令**

```intelli-shell search "[query]"```

**从文件或 URL 导入命令**

```intelli-shell import [path_or_url]```

**导出你的命令库**

```intelli-shell export [path]```

# SYNOPSIS

**intelli-shell** _subcommand_ [_options_]

# SUBCOMMANDS

**new**
> 创建新的命令模板。

**search**
> 搜索存储的命令（可选交互式）。

**replace**
> 替换给定命令中的变量。

**import**
> 从文件、URL 或 Gist 导入命令。

**export**
> 将命令导出到文件。

**fix**
> 使用 LLM 为命令建议修复方案。

**completions**
> 生成 Shell 补全脚本。

# DESCRIPTION

**intelli-shell** 是一个用 **Rust** 编写的跨平台命令模板和代码片段管理器。它把你的终端变成一个可搜索的命令库，可通过快捷键调出，并以参数化变量展开。

它与 **Bash**、**Zsh**、**Fish**、**Nushell** 和 **PowerShell** 集成。安装 shell 钩子后，**Ctrl+Space** 打开交互式模糊搜索来查找已存的命令，**Ctrl+B** 收藏最近执行的命令行，**Ctrl+X** 让配置好的 LLM 修复当前命令行。

模板支持动态变量（如 `{{file}}`）及可选的建议生成器，还支持工作区本地命令集和基于标签的分类。

# CAVEATS

Shell 集成需要在 shell 的 rc 文件中 source **intelli-shell init** 提供的钩子脚本。AI 修复功能需要在 **~/.config/intelli-shell/config.toml** 中配置 API 密钥（OpenAI、Gemini、Anthropic 等）。工作区感知依赖项目目录中的 **.intellishell** 文件。

# HISTORY

**intelli-shell** 由 **lasantosr** 维护，用 **Rust** 编写。它的目标是把 IDE 式的自动补全和命令管理带到终端。

# INSTALL

```pacman: sudo pacman -S intelli-shell```

```brew: brew install intelli-shell```

```nix: nix profile install nixpkgs#intelli-shell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [navi](/man/navi)(1), [atuin](/man/atuin)(1), [mcfly](/man/mcfly)(1)
