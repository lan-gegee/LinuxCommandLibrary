# TAGLINE

切换 SELinux 布尔值

# TLDR

**切换** SELinux 布尔值

```sudo togglesebool virt_use_samba```

切换**多个**布尔值

```sudo togglesebool httpd_enable_homedirs ftpd_full_access```

# SYNOPSIS

**togglesebool** _boolean_...

# DESCRIPTION

**togglesebool** 反转 SELinux 布尔值的当前（非持久化）取值。如果布尔值当前为开则关闭，反之亦然。更改不会在重启后保留。

# PARAMETERS

**boolean**
> 一个或多个要切换的 SELinux 布尔值名称

# CAVEATS

此工具已被弃用，通常已被移除，由 setsebool 取代。用 togglesebool 所做的更改不是持久化的，重启后会丢失。如需持久化更改请使用 setsebool -P。

# HISTORY

**togglesebool** 是早期管理布尔值的 SELinux 工具之一。它已被 **setsebool** 取代，后者对持久性提供了更多控制。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getsebool](/man/getsebool)(8), [setsebool](/man/setsebool)(8), [semanage-boolean](/man/semanage-boolean)(8)
