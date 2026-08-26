# TAGLINE

显示 Terraform 输出值

# TLDR

**显示所有输出**

```terraform output```

**显示特定输出**

```terraform output [name]```

**以 JSON 输出**

```terraform output -json```

**获取原始值**

```terraform output -raw [name]```

# SYNOPSIS

**terraform** **output** [_options_] [_name_]

# PARAMETERS

**-json**
> 以 JSON 格式输出。

**-raw**
> 输出原始字符串值。

**-state** _path_
> 从状态文件读取。

**-no-color**
> 禁用彩色输出。

# DESCRIPTION

**terraform output** 从 Terraform 状态文件读取输出值。它显示根模块 `output` 块中定义的值。适用于脚本编写、在配置之间传递值，以及提取 IP 地址、URL 或资源 ID 等基础设施细节。

使用 **-raw** 获取适合 shell 脚本使用的纯字符串（无引号和格式）。使用 **-json** 获取包含类型信息的机器可读输出。不带名称调用时，显示所有输出。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-apply](/man/terraform-apply)(1), [terraform-plan](/man/terraform-plan)(1)
