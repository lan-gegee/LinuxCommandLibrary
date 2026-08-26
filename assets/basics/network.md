# 网络

## 接口与 IP 地址
**ip** 是处理一切接口相关操作的现代工具；**ifconfig** 是它已弃用的前身。**a** 是 **addr** 的缩写。
```[ip](/man/ip) a```
```[ip](/man/ip) link show```
```[nmcli](/man/nmcli) device status```
```[ifconfig](/man/ifconfig) -a```

确认接口背后的网络硬件。
```[lspci](/man/lspci) | [grep](/man/grep) -i 'network\|ethernet'```
```[lshw](/man/lshw) -class network```
```[ethtool](/man/ethtool) eth0```

## 配置接口
启用或停用接口并手动分配地址（需要 root 权限）。用 **ip** 所做的修改重启后会丢失；要永久生效，请在你的网络管理器中设置。
```[ip](/man/ip) link set eth0 up```
```[ip](/man/ip) link set eth0 down```
```[ip](/man/ip) addr add 192.168.1.50/24 dev eth0```

释放 DHCP 租约并申请新的租约。
```[dhclient](/man/dhclient) -r eth0```
```[dhclient](/man/dhclient) eth0```

## Wi-Fi
配合 NetworkManager，**nmcli** 能扫描、连接 Wi-Fi，甚至显示当前网络的密码。
```[nmcli](/man/nmcli) device wifi list```
```[nmcli](/man/nmcli) device wifi connect [SSID] password [password]```
```[nmcli](/man/nmcli) device wifi show-password```

已保存的 Wi-Fi 密码存放在 NetworkManager 的连接配置文件里（需要 root 权限）。
```sudo [grep](/man/grep) -r "psk=" /etc/NetworkManager/system-connections/```

在使用 iwd 替代 NetworkManager 的系统上，请使用 **iwctl**。
```[iwctl](/man/iwctl) station wlan0 get-networks```
```[iwctl](/man/iwctl) station wlan0 connect [SSID]```

## 外部 IP
通过 HTTP 或 DNS 获取互联网视角下你的公网地址。
```[curl](/man/curl) ifconfig.me```
```[dig](/man/dig) +short myip.opendns.com @resolver1.opendns.com```

## 测试连通性
**ping** 检查主机是否有响应；**traceroute** 显示数据包经过的路径；**mtr** 把两者合成为一个实时视图。
```[ping](/man/ping) [host]```
```[ping](/man/ping) -c 4 [host]```
```[traceroute](/man/traceroute) [host]```
```[tracepath](/man/tracepath) [host]```
```[mtr](/man/mtr) [host]```

检查指定的 TCP 端口是否可达。
```[nc](/man/nc) -zv [host] [port]```
```[telnet](/man/telnet) [host] [port]```

测量两台机器之间的原始吞吐量（一台运行 **iperf3 -s**，另一台运行 **-c**）。
```[iperf3](/man/iperf3) -s```
```[iperf3](/man/iperf3) -c [serverIp]```

## DNS 查询
在域名与地址之间双向解析。**dig +short** 只输出答案；**-x** 对 IP 进行反向查询。
```[dig](/man/dig) [domain]```
```[dig](/man/dig) +short [domain]```
```[dig](/man/dig) -x [ip]```
```[dig](/man/dig) MX [domain]```
```[host](/man/host) [domain]```
```[nslookup](/man/nslookup) [domain]```
```[resolvectl](/man/resolvectl) query [domain]```

查询某个域名或 IP 段归谁所有。
```[whois](/man/whois) [domain]```

## 下载文件
**wget** 可下载并断点续传；**curl -O** 按远端原名保存（**-L** 跟随重定向）；**aria2c** 和 **axel** 将下载拆分到多个并行连接。
```[wget](/man/wget) [url]```
```[wget](/man/wget) -c [url]```
```[curl](/man/curl) -LO [url]```
```[aria2c](/man/aria2c) [url]```
```[axel](/man/axel) [url]```

## 开放端口与套接字
**ss** 已取代 netstat：**-t** 表示 TCP，**-u** 表示 UDP，**-l** 表示监听状态，**-n** 表示以数字显示，**-p** 显示所属进程（查看全部进程需要 root）。
```[ss](/man/ss) -tulpn```
```[netstat](/man/netstat) -tuln```
```[lsof](/man/lsof) -i```
```[lsof](/man/lsof) -i :80```

## 路由
显示路由表，并可查询到达某个目的地时会采用哪条路由（以及哪个源地址）。
```[ip](/man/ip) route```
```[ip](/man/ip) route get 1.1.1.1```
```[route](/man/route) -n```

## 带宽占用
实时流量：按连接查看用 **iftop**，按进程查看用 **nethogs**，按接口查看用 **nload** 和 **bmon**，长期统计则用 **vnstat**。
```[iftop](/man/iftop)```
```[nethogs](/man/nethogs)```
```[nload](/man/nload)```
```[bmon](/man/bmon)```
```[vnstat](/man/vnstat)```

## 主机名
```[hostname](/man/hostname)```
```[hostnamectl](/man/hostnamectl)```
```[hostnamectl](/man/hostnamectl) set-hostname [newName]```
