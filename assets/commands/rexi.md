# TAGLINE

用于正则表达式测试的终端 UI

# TLDR

**管道传入文本并交互式测试正则表达式**

```echo "hello world 123" | rexi```

**对文件测试正则模式**

```cat [logfile.txt] | rexi```

**对命令输出测试正则模式**

```ls -la | rexi```

通过 pip **安装**

```pip install rexi```

# SYNOPSIS

_command_ | **rexi**

# DESCRIPTION

**rexi** 是一个用于测试正则表达式的交互式终端 UI。它从 stdin 读取输入，让你实时评估正则表达式，并在匹配项高亮时提供即时视觉反馈。

它支持两种求值模式：

- **match**：使用 Python 的 `re.match` / `re.search` 语义。
- **finditer**：使用 `re.finditer` 迭代所有不重叠的匹配。

# CAVEATS

**rexi** 需要从标准输入获取数据；不接受文件参数。其正则语法遵循 **Python `re`** 模块，而不是 PCRE 或 POSIX。

# HISTORY

**rexi** 由 **Roy Reznik**（royreznik）创建，使用基于 Textual TUI 框架的 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#rexi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [ripgrep](/man/ripgrep)(1)
