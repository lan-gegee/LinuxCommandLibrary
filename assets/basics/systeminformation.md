# 系统信息

## 操作系统与内核
用的是哪个发行版、哪个内核，已经运行了多久？
```[uname](/man/uname) -a```
```[hostnamectl](/man/hostnamectl)```
```[lsb_release](/man/lsb_release) -a```
```[cat](/man/cat) /etc/os-release```
```[uptime](/man/uptime)```

适合截图和快速了解系统的美观概览。
```[fastfetch](/man/fastfetch)```
```[neofetch](/man/neofetch)```
```[inxi](/man/inxi) -Fz```

## CPU
**lscpu** 汇总型号、核心数和特性；/proc/cpuinfo 提供每个核心的原始详细信息。
```[lscpu](/man/lscpu)```
```[cat](/man/cat) /proc/cpuinfo```

当前 CPU 负载：**top** 批处理模式可获取一次性数值，**mpstat** 提供每核心统计，**vmstat** 提供持续滚动的视图。
```[top](/man/top) -bn1 | [grep](/man/grep) "Cpu(s)"```
```[mpstat](/man/mpstat) 1 5```
```[vmstat](/man/vmstat) 1```

## 内存
**free -h** 能回答常见问题；/proc/meminfo 则包含所有细节。
```[free](/man/free) -h```
```[cat](/man/cat) /proc/meminfo```
```[vmstat](/man/vmstat)```

在 **free** 中应看 "available" 列而非 "free" 列：Linux 会把空闲内存用作磁盘缓存，并在程序需要时释放。

## 进程
用 **ps** 获取快照，用 **top** 或其更友好的后继工具实时查看。
```[ps](/man/ps) aux```
```[ps](/man/ps) aux --sort=-%mem | [head](/man/head)```
```[top](/man/top)```
```[htop](/man/htop)```
```[btop](/man/btop)```
```[atop](/man/atop)```

## 磁盘与分区
各文件系统的剩余空间、树状显示的块设备以及分区表（fdisk/parted 需要 root 权限）。
```[df](/man/df) -h```
```[duf](/man/duf)```
```[lsblk](/man/lsblk) -f```
```[fdisk](/man/fdisk) -l```
```[parted](/man/parted) -l```

## 硬件
按总线列出设备，或获取包含型号在内的完整清单。
```[lspci](/man/lspci)```
```[lsusb](/man/lsusb)```
```[lshw](/man/lshw) -short```
```[dmidecode](/man/dmidecode) -t memory```

温度和风扇转速（先运行一次 **sensors-detect**）。
```[sensors](/man/sensors)```

## 电池
**upower** 报告详细的电池状态；**acpi** 给出一行式答案。原始值存放在 /sys 中。
```[acpi](/man/acpi) -b```
```[upower](/man/upower) -i $([upower](/man/upower) -e | [grep](/man/grep) BAT)```
```[cat](/man/cat) /sys/class/power_supply/BAT*/capacity```

## 蓝牙
**bluetoothctl** 是现行的工具；**hciconfig** 已被弃用，但在较旧的系统上仍能见到。
```[bluetoothctl](/man/bluetoothctl) show```
```[bluetoothctl](/man/bluetoothctl) devices```
```[hciconfig](/man/hciconfig) -a```

## 网络接口
```[ip](/man/ip) a```
```[ifconfig](/man/ifconfig) -a```

## 内核与启动消息
**dmesg** 输出内核环形缓冲区（在多数发行版上需要 root）；**journalctl -b** 显示本次启动以来的所有日志。
```[dmesg](/man/dmesg)```
```[dmesg](/man/dmesg) -w```
```[journalctl](/man/journalctl) -b```
```[lsmod](/man/lsmod)```
