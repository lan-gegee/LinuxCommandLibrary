# TAGLINE

打造精美 Shell 脚本的工具

# TLDR

**提示用户输入**

```gum input --placeholder "Enter name"```

**从选项中选择**

```gum choose "Option 1" "Option 2" "Option 3"```

**确认操作**

```gum confirm "Delete file?" && rm file```

**美化文本样式**

```gum style --foreground 212 "Styled text"```

**运行命令时显示加载动画**

```gum spin --title "Loading" -- sleep 5```

**输入多行文本**

```gum write --placeholder "Description"```

**用模糊搜索过滤列表**

```cat [flavors.txt] | gum filter```

**渲染 markdown 字符串**

```gum format -- "# Heading" "- item one" "- item two"```

# SYNOPSIS

**gum** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要运行的子命令。

**input**
> 提示输入单行内容。

**write**
> 提示输入长篇多行文本。

**choose**
> 从列表中选择一个或多个选项。

**confirm**
> 请用户确认操作（退出码为 0 或 1）。

**filter**
> 对列表中的条目进行模糊过滤。

**file**
> 从文件夹中选取文件。

**pager**
> 滚动查看文件或文本。

**table**
> 渲染表格数据或从中选择一行。

**style**
> 为文本应用颜色、边框和间距。

**join**
> 将带样式的文本块按垂直或水平方向组合。

**format**
> 渲染 markdown、模板字符串或具名 emoji。

**log**
> 向终端记录分级、结构化的消息。

**spin**
> 运行命令时显示加载动画。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gum** 是一款用于打造精美 Shell 脚本的工具。它提供交互式提示、样式化输出和 TUI 组件，无需编写任何 Go 代码即可构建美观的 CLI 应用程序，底层基于 Charm 的 Bubble Tea、Bubbles 和 Lip Gloss 库。

每个子命令都可以通过命令行标志或 `GUM_<COMMAND>_<OPTION>` 环境变量独立配置，脚本可以按需组合这些组件。

# CAVEATS

需要支持色彩的终端（完整样式效果建议使用真彩色）。属于 Charm 的 TUI 工具套件的一部分。

# HISTORY

**gum** 由 **Charm** 创建，首次发布于 **2022 年**，是其用于构建愉悦命令行工具的 TUI 工具包的一部分。它使用 Go 编写，以 MIT 许可证发布。

# INSTALL

```apt: sudo apt install gum```

```dnf: sudo dnf install gum```

```pacman: sudo pacman -S gum```

```apk: sudo apk add gum```

```zypper: sudo zypper install gum```

```brew: brew install gum```

```nix: nix profile install nixpkgs#gum```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [dialog](/man/dialog)(1), [whiptail](/man/whiptail)(1)

# RESOURCES

```[Homepage](https://charm.land/gum/)```

```[Source code](https://github.com/charmbracelet/gum)```

<!-- verified: 2026-07-17 -->
