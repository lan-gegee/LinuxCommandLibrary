# TAGLINE

为 Shell 初始化 Starship 提示符

# TLDR

**为 bash 初始化**

```eval "$(starship init bash)"```

**为 zsh 初始化**

```eval "$(starship init zsh)"```

**为 fish 初始化**

```starship init fish | source```

**为 PowerShell 初始化**

```Invoke-Expression (&starship init powershell)```

# SYNOPSIS

**starship** **init** _shell_

# PARAMETERS

**bash**
> Bash shell。

**zsh**
> Zsh shell。

**fish**
> Fish shell。

**powershell**
> PowerShell。

**--print-full-init**
> 打印完整的初始化脚本。

# DESCRIPTION

**starship init** 为 Starship 提示符生成 shell 初始化脚本，输出的脚本交由 shell 求值执行。将其添加到 shell 配置中即可持久启用提示符定制。

# INSTALL

```apt: sudo apt install starship```

```pacman: sudo pacman -S starship```

```apk: sudo apk add starship```

```zypper: sudo zypper install starship```

```brew: brew install starship```

```nix: nix profile install nixpkgs#starship```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[starship](/man/starship)(1)
