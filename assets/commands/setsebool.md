# TAGLINE

在运行时设置 SELinux 布尔值

# TLDR

临时**设置**一个布尔值

```sudo setsebool [boolean_name] on```

临时**取消**一个布尔值

```sudo setsebool [boolean_name] off```

**设置**布尔值并使其在重启后保持生效

```sudo setsebool -P [boolean_name] on```

**持久设置**多个布尔值

```sudo setsebool -P [bool1]=[on] [bool2]=[off]```

# SYNOPSIS

**setsebool** [_-PNV_] _boolean_ _value_ | _bool1=val1 bool2=val2..._

# PARAMETERS

**-P**
> 使更改在重启后仍然保留

**-N**
> 更改后不重新加载策略

**-V**
> 详细输出

# DESCRIPTION

**setsebool** 将特定 SELinux 布尔值或一组布尔值的当前状态设置为给定值。布尔值允许在运行时自定义 SELinux 策略，无需修改或重新编译策略。

启用可指定为 1、true 或 on，禁用可指定为 0、false 或 off。可以使用 **bool=value** 语法一次设置多个布尔值。

# CAVEATS

需要 root 权限。不带 -P 标志时，更改会在重启后丢失。使用 **getsebool** 查看当前布尔值。必须启用 SELinux 该命令才能工作。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getsebool](/man/getsebool)(8), [semanage-boolean](/man/semanage-boolean)(8), [setenforce](/man/setenforce)(8)
