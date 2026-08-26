# TAGLINE

基于 DNS 的 IP 地址地理归属查询

# TLDR

输出 IPv4 地址或主机所在的**国家**

```acountry [example.com]```

输出额外的**调试**信息

```acountry -d [example.com]```

输出更**详细**的信息

```acountry -v [example.com]```

# SYNOPSIS

**acountry** [_-d_] [_-v_] _hostname_or_ip_

# DESCRIPTION

**acountry** 输出 IPv4 地址或主机名所在的国家。它通过对国家代码数据库执行基于 DNS 的查询来确定 IP 地址的地理归属。该工具属于 **c-ares** 库的工具集，c-ares 提供异步 DNS 解析能力。

与 GeoIP 数据库工具不同，acountry 依靠对专门服务的 DNS TXT 记录查询来将 IP 段映射到国家代码。这使得它轻量且无依赖，但精度仅限于国家级。

# PARAMETERS

**-d**
> 输出额外的调试信息

**-v**
> 输出更详细的信息

# CAVEATS

IP 地理定位是近似值，可能不反映服务器或用户的实际物理位置。IP 地址可能被重新分配，也可能经其他国家路由。

# HISTORY

属于 **c-ares** 异步 DNS 解析器库的工具集。

# SEE ALSO

[ahost](/man/ahost)(1), [adig](/man/adig)(1), [host](/man/host)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1)
