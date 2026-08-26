# TAGLINE

从模板创建新的 Pulumi 项目

# TLDR

**以交互方式创建新项目**

```pulumi new```

**从模板创建**

```pulumi new [template]```

**创建 TypeScript 项目**

```pulumi new typescript```

**创建 AWS Python 项目**

```pulumi new aws-python```

**指定项目名称创建**

```pulumi new [template] --name [project_name]```

# SYNOPSIS

**pulumi** **new** [_options_] [_template_]

# PARAMETERS

**--name** _name_
> 项目名称。

**--description** _desc_
> 项目描述。

**-s**, **--stack** _name_
> 初始堆栈名称。

**-d**, **--dir** _dir_
> 目标目录。

**-y**, **--yes**
> 使用默认值跳过提示。

**--force**
> 覆盖已有文件。

**-g**, **--generate-only**
> 仅生成而不创建堆栈。

# DESCRIPTION

**pulumi new** 从模板创建新的 Pulumi 项目。模板包含语言运行时（typescript、python、go、csharp）和云提供商（aws、azure、gcp）。它会初始化项目结构和依赖。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-stack](/man/pulumi-stack)(1)
