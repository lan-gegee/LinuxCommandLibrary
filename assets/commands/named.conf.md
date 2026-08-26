# TAGLINE

BIND（使用最广泛的 DNS 服务器软件）的主配置文件

# TLDR

**基本 options 块**

```options { directory "/var/named"; };```

**定义区域**

```zone "example.com" { type master; file "example.com.zone"; };```

**纯转发解析器**

```options { forwarders { 8.8.8.8; }; forward only; };```

**允许来自网络的查询**

```options { allow-query { 192.168.1.0/24; }; };```

# SYNOPSIS

**/etc/named.conf** or **/etc/bind/named.conf**

# PARAMETERS

**options**
> 全局服务器选项。

**zone**
> 区域定义块。

**acl**
> 访问控制列表。

**logging**
> 日志配置。

**view**
> 视图定义。

**include**
> 包含外部文件。

# DESCRIPTION

**named.conf** 是 BIND（Berkeley Internet Name Domain）的主配置文件，BIND 是使用最广泛的 DNS 服务器软件。该文件定义区域、选项和访问控制。

配置采用类 C 的语法，由块和语句组成。

# EXAMPLE CONFIG

```
acl internal { 192.168.0.0/16; localhost; };

options {
    directory "/var/named";
    allow-query { internal; };
    recursion yes;
    forwarders { 8.8.8.8; 8.8.4.4; };
};

zone "example.com" {
    type master;
    file "zones/example.com.zone";
};
```

# CAVEATS

语法错误会导致 BIND 无法启动。请使用 named-checkconf 进行验证。区域文件的权限也很重要。

# SEE ALSO

[named](/man/named)(8), [rndc](/man/rndc)(8), [dig](/man/dig)(1)
