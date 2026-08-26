# TAGLINE

面向环境变量的安全加密配置档案

# TLDR

在项目目录中**初始化** envio

```envio init```

**创建**加密档案

```envio create [profile]```

**创建**带变量的档案

```envio create [profile] -e [KEY=value] [OTHER=value]```

**列出**所有档案

```envio list```

**查看**档案中的变量

```envio show [profile]```

**设置**或更新变量

```envio set [profile] [KEY=value]```

**启动一个加载了该档案的** Shell

```envio shell [profile]```

在该档案的环境下**运行一条命令**

```envio run [profile] -- [command]```

# SYNOPSIS

**envio** *command* [*options*] [*args*]

# DESCRIPTION

**envio** 以命名的**档案**（profile）管理环境变量，支持可选的加密方式（无加密、口令、对称密钥或 GPG）。档案可以被列出、查看、编辑、检查过期情况、加载进新的 shell，或应用于单条命令。它面向项目机密和多环境配置，避免提交明文 **.env** 文件。

详细指南见：https://github.com/humblepenguinn/envio/blob/main/docs/usage.md

# PARAMETERS

**init**

> 为当前项目目录初始化 envio。

**create** | **new** *profile* [**-e** *KEY[=value]*...] [**-k** *cipher*] [**-f** *file*] [**-d** *description*] [**-c**] [**-x**]

> 创建档案。**-k** 选择 **none**、**passphrase**、**symmetric** 或 **gpg**。**-e** 添加环境变量；**-f** 从文件导入；**-c**/**-x** 提示输入注释/过期时间。

**list** | **ls** [**--no-pretty-print**]

> 列出所有档案。

**show** *profile* [**-c**] [**-x**] [**--no-pretty-print**]

> 显示键值对（可选注释与过期时间）。

**set** *profile* *KEY[=value]*... [**-c**] [**-x**]

> 添加或更新变量。

**unset** *profile* *KEY*...

> 移除变量。

**edit** *profile*

> 在 **$EDITOR** 中打开解密后的档案（需要设置 **EDITOR**）。

**check** *profile*

> 报告已过期或即将过期的变量。

**shell** *profile*

> 启动注入了档案环境的 shell。

**run** *profile* **--** *command*

> 应用档案后运行单条命令。

档案的加密方法在创建后不可更改。请妥善保管口令/对称密钥。

# CAVEATS

编辑器打开期间，**edit** 会将机密写入临时文件（Unix 上权限为 0600）。对称密钥只在创建时显示一次——请离线保存。生产环境的机密建议优先使用 GPG 或高强度口令。

# INSTALL

```brew: brew install envio```

```nix: nix profile install nixpkgs#envio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[direnv](/man/direnv)(1), [env](/man/env)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/humblepenguinn/envio)```

```[Documentation](https://github.com/humblepenguinn/envio/blob/main/docs/usage.md)```

<!-- verified: 2026-07-19 -->
