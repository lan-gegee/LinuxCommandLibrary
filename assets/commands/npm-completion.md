# TAGLINE

生成 Shell 补全脚本

# TLDR

**输出补全脚本**（bash 和 zsh 输出相同）

```npm completion```

**为当前 bash 会话加载补全**

```source <(npm completion)```

**在 bash 中持久化**

```npm completion >> ~/.bashrc```

**在 zsh 中持久化**（需先加载 `compinit`）

```npm completion >> ~/.zshrc```

# SYNOPSIS

**npm** **completion**

# PARAMETERS

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm completion** 生成 Shell 补全脚本，为 npm 启用 Tab 补全。

该命令将脚本输出到 stdout，可将其追加到 shell 的 rc 文件中。

# CAVEATS

仅支持 **bash** 和 **zsh**。在其他 shell（fish、PowerShell）下脚本不会起任何作用。在 zsh 中使用时必须启用 `bashcompinit`，而 zsh 自带的 `compinit` 在任何现代配置中都会自动处理。追加后需重新加载 shell（或 `source` rc 文件）。

# HISTORY

npm completion 为命令行 Tab 补全提供 **shell 集成**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [bash-completion](/man/bash-completion)(1)
