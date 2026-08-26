# TAGLINE

在 Zsh 和 tcsh 中管理 shell 按键绑定

# TLDR

**列出当前所有按键绑定**

```bindkey```

**以适合写入 .zshrc 的格式列出绑定**

```bindkey -L```

**使用 Emacs 按键绑定**

```bindkey -e```

**使用 Vi 按键绑定**

```bindkey -v```

**将按键序列绑定到 ZLE widget**

```bindkey '^[[H' beginning-of-line```

**将按键序列绑定到字符串**

```bindkey -s '^T' 'uptime\n'```

**移除一个按键绑定**

```bindkey -r '^l'```

# SYNOPSIS

**bindkey** [_options_] [**-m** _keymap_] [_key_ [_widget_]]

# DESCRIPTION

**bindkey** 是 Zsh 和 tcsh 中用于管理按键绑定的内建命令。在 Zsh 中，它控制 Zsh 行编辑器（ZLE），允许用户将按键序列映射到编辑器 widget 或宏。在 tcsh 中，它提供类似的功能来自定义键盘行为。

按键绑定决定了命令行编辑期间 Shell 对键盘输入的响应方式。默认情况下 Shell 通常使用 Emacs 风格的绑定，但也提供 Vi 风格绑定。

要查看某个键的转义序列，可在命令行先按 **Ctrl+v** 再按该键。

# PARAMETERS

**-e**
> 选择 Emacs 按键绑定（默认 keymap）

**-v**
> 选择 Vi 按键绑定，从插入模式开始

**-L**
> 以适合写入 .zshrc 的 bindkey 命令形式列出绑定

**-l**
> 列出可用的 keymap 名称

**-M** _keymap_
> 为绑定操作指定 keymap（emacs、viins、vicmd）

**-s**
> 将键绑定到字符串而不是 widget

**-r** _key_
> 移除指定键的绑定

**-p**
> 列出前缀键的绑定

**-N** _newkeymap_ [_oldkeymap_]
> 创建新的 keymap，可选择复制现有的一个

**-A** _oldkeymap_ _newkeymap_
> 创建指向 _oldkeymap_ 的别名 _newkeymap_

# CAVEATS

按键序列因终端模拟器而异。请在你的具体终端环境中测试绑定。功能键和 Home/End 等特殊键可能因终端不同而具有不同的转义序列。

在 Zsh 中，**bindkey** 作用于各个 keymap。活动 keymap 取决于当前的编辑模式（Emacs 还是 Vi）。对一个 keymap 的修改不会影响其他 keymap。

# HISTORY

bindkey 命令起源于 **tcsh**（TENEX C Shell），后来被 **Zsh** 借鉴并借助 Zsh 行编辑器增强了功能。Zsh 的实现提供了更丰富的自定义选项，包括多个 keymap 和用户自定义 widget。

# SEE ALSO

[zsh](/man/zsh)(1), [tcsh](/man/tcsh)(1), [bash](/man/bash)(1)

# RESOURCES

```[Homepage](https://www.zsh.org/)```

```[Documentation](https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html)```

<!-- verified: 2026-06-19 -->
