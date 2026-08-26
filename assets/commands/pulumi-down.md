# TAGLINE

pulumi destroy 的别名

# TLDR

**销毁所有资源（别名）**

```pulumi down```

**自动确认并销毁**

```pulumi down --yes```

**销毁指定堆栈**

```pulumi down --stack [name]```

**跳过预览直接销毁**

```pulumi down --skip-preview --yes```

**销毁并移除堆栈**

```pulumi down --remove --yes```

**仅预览而不销毁**

```pulumi down --preview-only```

# SYNOPSIS

**pulumi** **down** [_options_]

# DESCRIPTION

**pulumi down** 是 **pulumi destroy** 的别名。移除当前堆栈管理的所有资源。为 **pulumi up** 提供了更直观的对应操作。

# PARAMETERS

**-y**, **--yes**
> 预览后自动确认并执行销毁。

**-s**, **--stack** _name_
> 要操作的堆栈名称。默认为当前堆栈。

**-f**, **--skip-preview**
> 执行销毁前不计算预览。

**--preview-only**
> 仅显示销毁的预览，但不执行销毁。

**--target** _urn_
> 仅销毁指定的资源 URN（及其依赖项）。

**-x**, **--exclude** _urn_
> 在销毁中排除指定的资源 URN。

**--exclude-protected**
> 不销毁受保护的资源，销毁其他所有资源。

**--remove**
> 所有资源删除后，移除该堆栈及其配置文件。

**-p**, **--parallel** _N_
> 允许 N 个资源操作同时并行运行（默认 16）。

**-j**, **--json**
> 将销毁的差异、操作和整体输出序列化为 JSON。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-destroy](/man/pulumi-destroy)(1), [pulumi-up](/man/pulumi-up)(1)
