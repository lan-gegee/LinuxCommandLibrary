# TAGLINE

为 Pulumi 生成 shell 补全脚本

# TLDR

**生成 bash 补全**

```pulumi gen-completion bash```

**生成 zsh 补全**

```pulumi gen-completion zsh```

**生成 fish 补全**

```pulumi gen-completion fish```

**生成 PowerShell 补全**

```pulumi gen-completion powershell```

**安装 bash 补全**

```pulumi gen-completion bash > /etc/bash_completion.d/pulumi```

将 **zsh 补全**安装到 fpath 目录

```pulumi gen-completion zsh > "${fpath[1]}/_pulumi"```

# SYNOPSIS

**pulumi** **gen-completion** _shell_

# PARAMETERS

**bash**
> 生成 bash 补全。

**zsh**
> 生成 zsh 补全。

**fish**
> 生成 fish 补全。

**powershell**
> 生成 PowerShell 补全。

# DESCRIPTION

**pulumi gen-completion** 为 Pulumi 命令生成 shell 补全脚本。将补全代码输出到标准输出，供安装到 shell 配置中使用。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1)
