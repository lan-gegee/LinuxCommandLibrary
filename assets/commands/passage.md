# TAGLINE

基于 age 的密码与机密信息管理器（兼容 pass）

# TLDR

为密码库**创建 age 身份**（一次性设置；没有 `init` 命令）

```mkdir -p ~/.passage && age-keygen >> ~/.passage/identities```

**插入新密码**（支持多行）

```passage insert path/to/entry```

**显示某个密码**

```passage path/to/entry```

**复制密码到剪贴板**

```passage -c path/to/entry```

**生成密码**

```passage generate path/to/entry 20```

**列出密码库**

```passage ls```

**编辑或删除条目**

```passage edit path/to/entry```

```passage rm path/to/entry```

# SYNOPSIS

**passage** [_options_] _command_ [_args_]

# DESCRIPTION

**passage** 是经典 `pass`（password-store）工具的一个分支，用 age 加密文件而非 GPG 来存储机密信息。

每条机密信息以独立文件的形式存放在 `~/.passage/store`（或 `$PASSAGE_DIR`）下。该目录可以用 Git 跟踪。passage 通过简单的 CLI 支持插入、生成、编辑、显示、复制、列出和删除操作。

解密时使用 `~/.passage/identities`（或 `$PASSAGE_IDENTITIES_FILE`）中的 age 身份。加密时优先使用最近的 `.age-recipients` 文件；如果找不到，则使用身份文件。

**没有 `init` 命令。** 请自行设置身份（例如用 `age-keygen`），然后开始插入机密信息。移动或复制机密时总是会重新加密。

# PARAMETERS

常用子命令和选项（在适用的地方与 password-store 兼容）：

**-c**, **--clip**
> 将机密信息复制到剪贴板而不是打印。

**insert** [_-m_ | _--multiline_] _name_
> 添加或覆盖条目。`-m` 表示多行。

**generate** _name_ [_length_]
> 生成并存储随机密码。

**edit** _name_
> 在 $EDITOR 中编辑条目。

**ls**, **list**
> 显示密码库树。

**rm**, **remove** _name_
> 删除条目。

**show** _name_（或直接写 _name_）
> 解密并打印条目。

# ENVIRONMENT

**PASSAGE_DIR**
> 密码库位置（默认：`~/.passage/store`）。

**PASSAGE_IDENTITIES_FILE**
> 身份文件位置（默认：`~/.passage/identities`）。

**PASSAGE_AGE**
> 要使用的 age 可执行文件（已在 `age` 和 `rage` 下测试）。

**PASSAGE_RECIPIENTS_FILE** / **PASSAGE_RECIPIENTS**
> 覆盖加密接收者（对应 age 的 `-R` / `-r`）。

其他 password-store 变量（如 `PASSWORD_STORE_CLIP_TIME` 和 `PASSWORD_STORE_GENERATED_LENGTH`）同样被遵循。

# CAVEATS

`init` 命令**不可用**。首次使用前，请用 `age-keygen` 创建 `~/.passage/identities`（或使用带密码保护 / 硬件支持的身份）。也可以将公钥接收者写入 `~/.passage/store/.age-recipients`。

解密时必须能访问 age 身份（私钥）。与 GPG 不同，age 密钥通常不在密钥服务器上；备份由你自行负责。剪贴板支持取决于平台工具（xclip、pbcopy、wl-copy 等）。

# INSTALL

```apk: sudo apk add passage```

```nix: nix profile install nixpkgs#passage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [age](/man/age)(1), [age-keygen](/man/age-keygen)(1)

# RESOURCES

```[Source code](https://github.com/FiloSottile/passage)```

<!-- verified: 2026-07-11 -->
