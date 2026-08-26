# TAGLINE

管理 SELinux 文件上下文标签规则

# TLDR

**列出所有文件标签规则**

```sudo semanage fcontext -l```

不带标题地**列出所有用户自定义的文件标签规则**

```sudo semanage fcontext -l -C -n```

**添加**一条为匹配正则的路径设置标签的规则

```sudo semanage fcontext -a -t [samba_share_t] '/mnt/share(/.*)?'```

为特定文件类型添加规则（f=文件，d=目录）

```sudo semanage fcontext -a -f [d] -t [httpd_sys_content_t] '/srv/www(/.*)?'```

在路径之间创建标签等价关系

```sudo semanage fcontext -a -e /[path/to/ref] /[path/to/target]```

**修改**现有规则以更改类型

```sudo semanage fcontext -m -t [httpd_sys_rw_content_t] '/srv/www(/.*)?'```

使用其正则**删除**用户自定义规则

```sudo semanage fcontext -d '/mnt/share(/.*)?'```

**删除**所有本地自定义项

```sudo semanage fcontext -D```

# SYNOPSIS

**semanage fcontext** [**-l**|**-a**|**-d**|**-m**|**-D**] [_options_] _file_spec_

# PARAMETERS

**-l**, **--list**
> 列出所有文件上下文规则。

**-a**, **--add**
> 添加新的文件上下文规则。

**-d**, **--delete**
> 删除文件上下文规则。

**-m**, **--modify**
> 修改现有规则。

**-D**, **--deleteall**
> 移除所有本地自定义项。

**-t** _TYPE_, **--type** _TYPE_
> 分配给匹配文件的 SELinux 类型。

**-f** _TYPE_, **--ftype** _TYPE_
> 要匹配的文件类型：f（普通文件）、d（目录）、c（字符设备）、b（块设备）、s（套接字）、l（符号链接）、p（命名管道）。默认匹配所有文件类型。

**-s** _SEUSER_, **--seuser** _SEUSER_
> 上下文的 SELinux 用户名。

**-r** _RANGE_, **--range** _RANGE_
> MLS/MCS 安全范围（仅限 MLS/MCS 系统）。

**-e** _PATH_, **--equal** _PATH_
> 创建等价规则：生成默认标签时用给定的参考路径替换目标路径。

**-C**, **--locallist**
> 仅显示本地自定义的规则。

**-n**, **--noheading**
> 输出中省略列标题。

**-N**, **--noreload**
> 提交后不重新加载策略。

**-E**, **--extract**
> 提取可自定义的命令以便在事务中使用。

**-S** _STORE_, **--store** _STORE_
> 选择备用的 SELinux 策略存储。

# DESCRIPTION

**semanage fcontext** 管理 SELinux 中持久的文件上下文标签规则。文件上下文决定文件获得什么 SELinux 类型标签，从而控制受限域可以访问哪些文件。

规则使用 PCRE 正则表达式匹配文件路径。添加或修改规则后，需要对受影响的目录运行 **restorecon** 以应用新标签。

# CAVEATS

需要 root 权限。规则是持久的，但不会自动应用；请使用 **restorecon -Rv** 应用。当一个目录应具有与参考路径相同的上下文时，等价规则（**-e**）很有用。未指定时，**-f** 文件类型选项默认适用于所有文件。

# SEE ALSO

[semanage](/man/semanage)(8), [restorecon](/man/restorecon)(8), [matchpathcon](/man/matchpathcon)(8), [chcon](/man/chcon)(1), [semanage-boolean](/man/semanage-boolean)(8), [semanage-port](/man/semanage-port)(8)
