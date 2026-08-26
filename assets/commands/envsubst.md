# TAGLINE

替换文本中的环境变量

# TLDR

**替换文件中的环境变量**

```envsubst < [template.txt]```

**替换并保存**到新文件

```envsubst < [template.txt] > [output.txt]```

只**替换特定变量**

```envsubst '$USER $HOME' < [template.txt]```

**从管道输入替换**

```echo 'Hello $USER' | envsubst```

**列出模板中引用的所有变量**

```envsubst --variables < [template.txt]```

**在配置模板中替换**

```cat [nginx.conf.template] | envsubst '$SERVER_NAME $PORT' > [nginx.conf]```

# SYNOPSIS

**envsubst** [_OPTION_] [_SHELL-FORMAT_]

# PARAMETERS

**-v**, **--variables**
> 输出 SHELL-FORMAT 或标准输入中出现的变量。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

_SHELL-FORMAT_
> 要替换的变量列表，以空格分隔。指定后只替换这些变量，其余保持字面文本不变。

# DESCRIPTION

**envsubst** 替换 shell 格式字符串中的环境变量引用。它从标准输入读取文本，将 **$VAR** 和 **${VAR}** 模式替换为环境中的对应值，并把结果写到标准输出。

该工具是在部署流水线和容器化环境中从模板生成配置文件的必备手段。模板中可以包含 **${DATABASE_HOST}**，部署时会被替换为实际值。

不带变量列表调用时，envsubst 替换所有环境变量引用。若只想替换特定变量（其余保留为字面文本），请提供列出所需变量的 SHELL-FORMAT 参数。

该工具同时支持 **$VAR** 和 **${VAR}** 两种语法。缺失的变量会被替换为空字符串。不支持用于默认值的 **${VAR:-default}** 语法；envsubst 只做简单替换。

常见用途包括：Docker 入口脚本在运行时配置服务、CI/CD 流水线生成配置，以及任何需要让配置适应运行环境的场景。

# CAVEATS

不支持 **${VAR:-default}**、**${VAR:+value}** 之类的 shell 参数展开特性。所有变量都必须存在于环境中；缺失的变量会变成空字符串。需要保持字面含义的美元符号要用 **$$** 转义。属于 gettext 软件包的一部分。

# HISTORY

**envsubst** 是国际化工具包 GNU **gettext** 的一部分。虽然 gettext 主要面向软件翻译，envsubst 却被广泛用作通用模板工具，尤其在 DevOps 社区中用于配置管理。它随 gettext-base 包发布，几乎所有类 Unix 系统上都可用。

# INSTALL

```apt: sudo apt install gettext-base```

```dnf: sudo dnf install gettext-envsubst```

```apk: sudo apk add gettext-envsubst```

```zypper: sudo zypper install envsubst```

```nix: nix profile install nixpkgs#envsubst```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gettext](/man/gettext)(1), [sed](/man/sed)(1), [awk](/man/awk)(1), [env](/man/env)(1), [export](/man/export)(1)
