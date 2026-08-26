# TAGLINE

管理持久的 SELinux 布尔值设置

# TLDR

**列出**所有布尔值设置

```sudo semanage boolean -l```

不带标题地**列出**所有用户自定义的布尔值设置

```sudo semanage boolean -l -C -n```

持久性地**设置**或取消某个布尔值

```sudo semanage boolean -m --on|--off [haproxy_connect_any]```

# SYNOPSIS

**semanage boolean** [**-l**|**-m**] [_options_] [_boolean_]

# PARAMETERS

**-l, --list**
> 列出所有布尔值及其当前取值

**-m, --modify**
> 修改布尔值的持久化取值

**-C, --locallist**
> 仅显示本地修改过的布尔值

**-n, --noheading**
> 输出中省略列标题

**-1, --on**
> 将布尔值设为 on/true

**-0, --off**
> 将布尔值设为 off/false

# DESCRIPTION

**semanage boolean** 管理持久的 SELinux 布尔值设置。布尔值允许管理员定制 SELinux 策略规则如何影响受限进程，而无需修改策略本身。

与可能只做临时更改的 **setsebool** 不同，semanage boolean 的更改在系统重启后依然生效。**-C** 标志可显示哪些布尔值已从默认值被自定义。

# CAVEATS

需要 root 权限。布尔值更改立即生效，同时也会持久保存。使用 **getsebool -a** 可快速非持久地查看所有布尔值。

# SEE ALSO

[semanage](/man/semanage)(8), [getsebool](/man/getsebool)(8), [setsebool](/man/setsebool)(8), [sestatus](/man/sestatus)(8), [selinuxenabled](/man/selinuxenabled)(8)
