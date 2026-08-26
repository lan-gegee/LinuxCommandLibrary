# TAGLINE

显示 OpenTofu 状态的输出值

# TLDR

**显示所有输出值**

```tofu output```

**显示特定输出值**

```tofu output [name]```

**以 JSON 输出**

```tofu output -json```

**获取原始值**

```tofu output -raw [name]```

# SYNOPSIS

**tofu** **output** [_options_] [_name_]

# PARAMETERS

**-json**
> 以 JSON 输出。敏感值将以明文显示。

**-raw**
> 输出原始字符串值。仅适用于可自动转换为字符串的值。

**-state** _path_
> 从指定的状态文件读取而不是默认文件。

**-no-color**
> 禁用彩色输出。

# DESCRIPTION

**tofu output** 显示 OpenTofu 状态中的输出值。OpenTofu 是 Terraform 的开源分支。它显示在 output 块中定义的值。不带名称参数调用时显示所有输出值。默认的人类可读格式可能在版本间变化；脚本中请使用 -json 以获得稳定的机器可读输出。使用 -json 或 -raw 时，敏感值将以明文显示。

# INSTALL

```dnf: sudo dnf install opentofu```

```pacman: sudo pacman -S opentofu```

```apk: sudo apk add opentofu```

```zypper: sudo zypper install opentofu```

```brew: brew install opentofu```

```nix: nix profile install nixpkgs#opentofu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tofu](/man/tofu)(1), [tofu-plan](/man/tofu-plan)(1), [terraform-output](/man/terraform-output)(1)
