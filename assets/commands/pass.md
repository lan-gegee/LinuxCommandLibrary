# TAGLINE

以目录结构组织、将密码存储于 GPG 加密文件中的简单密码管理器

# TLDR

使用 GPG 密钥**初始化密码库**

```pass init [gpg-id]```

**列出所有密码**

```pass```

**显示某个密码**

```pass [folder/name]```

**复制密码**到剪贴板

```pass -c [folder/name]```

**生成新密码**

```pass generate [folder/name] [20]```

生成不含符号的密码

```pass generate -n [folder/name] [20]```

**插入一个密码**

```pass insert [folder/name]```

**编辑一个密码**

```pass edit [folder/name]```

**删除一个密码**

```pass rm [folder/name]```

**搜索密码**

```pass grep [search_term]```

与 git **同步**

```pass git push```

# SYNOPSIS

**pass** [_command_] [_args_...]

# DESCRIPTION

**pass**（password-store）是一个简单的密码管理器，它将密码存储在按目录层级组织的 GPG 加密文件中。每个密码保存在单独的文件里，用一个或多个 GPG 密钥加密。

密码库是位于 ~/.password-store 的目录树，每个文件包含一个密码以及可选的附加数据。Git 集成提供版本控制和同步能力。

pass 以 Unix 哲学提供简单直接的密码管理方式，复用现有工具（GPG、git、tree）而非自建数据库。

# PARAMETERS

**init** _gpg-id_
> 初始化密码库。

**ls** [_subfolder_]
> 列出密码。

**show** _name_
> 解密并显示密码。

**insert** _name_
> 插入新密码。

**edit** _name_
> 用编辑器编辑密码。

**generate** _name_ [_length_]
> 生成新密码。

**rm** _name_
> 删除密码。

**mv** _old_ _new_
> 移动/重命名密码。

**cp** _old_ _new_
> 复制密码。

**find** _pass-names_...
> 查找与给定名称匹配的密码（别名：**search**）。

**grep** _pattern_
> 在解密后的文件中搜索。

**git** _args_
> 执行 git 命令。

**help**
> 显示用法信息。

**version**
> 显示版本信息。

**-c**, **--clip**
> 复制到剪贴板而不是显示。

**-m**, **--multiline**
> 插入多行密码（配合 **insert**）。

**-f**, **--force**
> 覆盖前不提示。

**-n**, **--no-symbols**
> 生成不含符号的密码。

# CAVEATS

加密需要 GPG 密钥。文件名（密码路径）不加密。剪贴板内容可能被记录。除非重写历史，否则 git 历史会保留旧密码。

# HISTORY

**pass** 由 **Jason Donenfeld**（zx2c4）于 **2012 年**创建，是一个遵循 Unix 哲学的极简密码管理器。它凭借简洁性和对标准工具的使用而广受欢迎。该项目衍生出许多兼容客户端以及面向浏览器和移动设备的扩展。

# INSTALL

```dnf: sudo dnf install pass```

```pacman: sudo pacman -S pass```

```apk: sudo apk add pass```

```brew: brew install pass```

```nix: nix profile install nixpkgs#pass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [git](/man/git)(1), [pwgen](/man/pwgen)(1), [gopass](/man/gopass)(1)
