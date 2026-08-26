# TAGLINE

为 rustup 生成 shell 补全脚本

# TLDR

**生成 bash 补全**

```rustup completions bash```

**生成 zsh 补全**

```rustup completions zsh```

**生成 fish 补全**

```rustup completions fish```

**生成 cargo 补全**

```rustup completions bash cargo```

# SYNOPSIS

**rustup** **completions** _shell_ [_command_]

# PARAMETERS

**bash**
> Bash 补全。

**zsh**
> Zsh 补全。

**fish**
> Fish 补全。

**powershell**
> PowerShell 补全。

**cargo**
> 改为为 cargo 生成补全。

# DESCRIPTION

**rustup completions** 生成 shell 补全脚本。输出 rustup 或 cargo 命令的补全代码。请安装到相应的 shell 配置中。

# SEE ALSO

[rustup](/man/rustup)(1), [cargo](/man/cargo)(1)
