# TAGLINE

显示输出格式化文档

# TLDR

**查看格式化帮助**

```gh formatting```

# SYNOPSIS

**gh** **formatting**

# DESCRIPTION

**gh formatting** 显示关于 GitHub CLI 输出格式化功能的完整帮助。其中介绍了用于自定义输出的模板语法、输出机器可读数据的 JSON 输出模式，以及字段选择选项。

许多 gh 命令支持 --json 标志，输出可供 jq 等工具处理的结构化数据。模板格式化使用 Go template 语法来创建自定义输出布局。--jq 标志提供与 jq 的直接集成，用于 JSON 过滤。

理解格式化选项对于将 gh 集成到脚本和自动化工作流中至关重要。

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

[gh](/man/gh)(1), [gh-help](/man/gh-help)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_help_formatting)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
