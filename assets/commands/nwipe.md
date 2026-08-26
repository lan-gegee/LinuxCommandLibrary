# TAGLINE

使用多次覆写方法安全擦除磁盘

# TLDR

**启动已检测磁盘的交互式擦除**（ncurses 界面）

```sudo nwipe```

**用交互式界面擦除指定设备**

```sudo nwipe /dev/sdb /dev/sdc```

**自动擦除列出的设备**（无界面，无人值守）

```sudo nwipe --autonuke --nogui /dev/sdb```

**快速零填充**磁盘（单次全零覆写）

```sudo nwipe --method=zero /dev/sdb```

**DoD 三遍擦除**并校验最后一遍

```sudo nwipe --method=dodshort --verify=last /dev/sdb```

**排除系统盘**并立即擦除其余所有设备

```sudo nwipe --autonuke --exclude=/dev/sda```

**将擦除进度记录**到文件

```sudo nwipe --logfile=/var/log/nwipe.log /dev/sdb```

**使用 PRNG 流**方法并进行多轮覆写

```sudo nwipe --method=prng --rounds=2 /dev/sdb```

# SYNOPSIS

**nwipe** [*options*] [*device1*] [*device2*] ...

# PARAMETERS

**-V**, **--version**
> 打印版本号

**-h**, **--help**
> 打印帮助摘要

**-v**, **--verbose**
> 记录更多消息（调试用）

**-q**, **--quiet**
> 在图形界面和日志中匿名化序列号

**-m**, **--method**=*METHOD*
> 擦除方法（默认：**prng**）。常用取值：**prng** / **random** / **stream**、**zero** / **quick**、**one**、**dodshort** / **dod3pass**、**dod522022m** / **dod**、**gutmann**、**ops2**、**is5enh**、**bruce7**、**bmb**、**verify_zero**、**verify_one**

**-r**, **--rounds**=*NUM*
> 运行所选方法的次数（默认：1）

**-p**, **--prng**=*METHOD*
> 用于随机方法的 PRNG：**mersenne**、**twister**、**isaac**、**isaac64**、**xoroshiro256_prng**、**aes_ctr_prng**、**chacha20** 等；**auto** 会进行基准测试并选择最快的（默认）

**--prng-benchmark**
> 运行仅内存的 PRNG 吞吐量基准测试后退出（不执行擦除）

**--verify**=*TYPE*
> 校验模式：**off**、**last**（默认）或 **all**

**--autonuke**
> 立即开始擦除（若未列出设备则针对所有检测到的设备，否则仅针对列出的设备）

**--nogui**
> 无交互界面；必须与 **--autonuke** 同用。隐含 **--nowait**

**--nowait**
> 退出前不等待按键

**--noblank**
> 跳过擦除完成后的最终清空步骤

**--nousb**
> 不显示也不擦除 USB 设备

**--force**
> 允许擦除看起来正在使用（已挂载）的设备。危险；默认禁用

**-e**, **--exclude**=*DEVICES*
> 以逗号分隔的要排除的设备（最多十个）

**-l**, **--logfile**=*FILE*
> 日志文件路径（默认：STDOUT）

**-P**, **--PDFreportpath**=*DIR*
> PDF 擦除证书的存放目录（默认：**.**）；设为 **noPDF** 可禁用

**--sync**=*NUM*
> 缓存 I/O 期间执行 **fdatasync** 的频率（每次同步之间处理的设备块数；默认 100000）

**--directio** / **--cachedio** / **--io-mode**=*MODE*
> I/O 路径：直接（**O_DIRECT**）、缓存，或 **auto** / **cached** / **direct**

**--autopoweroff**
> 擦除成功一分钟后关机（可用 **shutdown -c** 中止）

**--nosignals**
> 不允许信号中断擦除过程

**--reverse**
> 从设备末尾向开头写入（有助于跳过坏块继续）

**--scatter**
> 分散/随机分段顺序（压力测试风格；可能较慢）

# DESCRIPTION

**nwipe** 使用多种公认的多次覆写方法安全擦除块设备的全部内容。它是 Darik's Boot and Nuke（DBAN）中 **dwipe** 引擎的一个持续维护的分叉版本，设计为可在任何 Linux 发行版上运行（也是 **ShredOS** 可引导介质中的擦除引擎）。

不带选项时，nwipe 会呈现一个交互式 ncurses 界面，列出检测到的磁盘，供你选择目标和方法。设备可以以经典节点形式给出（**/dev/sda**、**/dev/nvme0n1**），也可以使用 **/dev/disk/by-id/** 下的稳定路径。多块磁盘可以并行擦除。

方法涵盖从单次全零或全一覆写，到 DoD 5220.22-M 变体和 Gutmann，再到 PRNG 流以及 HMG IS5 enhanced、Schneier（**bruce7**）、BMB21-2019 等标准。基于随机的方法使用经 **getrandom**(2) 播种的 PRNG。可选的校验会在最后一遍之后（或每一遍之后）重新读取数据。可生成 PDF 擦除证书以备审计。

与 **shred** 等面向文件的工具相比，nwipe 面向整盘清理，提供磁盘选择界面、多磁盘操作、日志记录和证书生成。

# CAVEATS

擦除会永久销毁目标设备上的所有数据。使用 **--autonuke** 时务必反复核对设备名，并用 **--exclude** 排除系统盘。**--force** 可以擦除已挂载的文件系统，非常危险。

对于 SSD 和 NVMe 设备，软件多次覆写可能无法像 ATA Secure Erase 或 **nvme format**/sanitize 那样触及重映射单元；在条件允许且符合策略时优先使用硬件安全擦除功能。出现 I/O 错误的故障驱动器可能耗时极长，除非使用 **--no-retry-on-io-errors**。缓存 I/O 会将错误检测推迟到同步时；**--sync=0** 只在每遍结束时同步一次，不推荐。

# HISTORY

**nwipe** 从 DBAN 分叉出 **dwipe**，让同一擦除引擎能够在 DBAN live 环境之外运行于普通 Linux 发行版上，并获得更好的硬件支持。它使用 pthreads 而非 fork，使用 parted 库进行驱动器检测，并逐步增加了更多方法、PRNG、I/O 模式、稳定设备路径和 PDF 证书等功能。该项目由 Martijn van Brummelen 及其协作者维护（包括 Nick Law / PartialVolume 相关的 ShredOS 工作）。

# INSTALL

```apt: sudo apt install nwipe```

```dnf: sudo dnf install nwipe```

```aur: yay -S nwipe```

```apk: sudo apk add nwipe```

```nix: nix profile install nixpkgs#nwipe```

<!-- packages: 2026-07-25 -->

# SEE ALSO

[shred](/man/shred)(1), [dd](/man/dd)(1), [wipe](/man/wipe)(1), [wipefs](/man/wipefs)(8), [badblocks](/man/badblocks)(8)

# RESOURCES

```[Source code](https://github.com/martijnvanbrummelen/nwipe)```

<!-- verified: 2026-07-25 -->
