리눅스(서울진흥원 풀스택개발자 교육과정)

1991, Linus Torvalds(Finn) from Unix
Linux Distro
 - Debian : Debian, Ubuntu, KNOPPIX(CD Linux)
 - Red Hat : Fedora, RedHat Enterprise, CentOS, Vine Linux(Jp)
 - Slackware: openSUSE(Novell), SUSE Linux Enterprise
Kernel
  - Management the Memory, File System, CPU, Device, etc.



Manipulate Linux Kernel
# Linux Shell Types
 - sh (Bourne shell) : By Unix Shell, Super shell
 - bash (Bourne-agin shell) : Super shell in Linux
 - csh (C shell) : C like syntax
 - tcsh (Enhanced-C shell): c
 - ksh (korn shell) : by David Korn, Powerful Script Language
 - zch (Z shell) : Unix/GNU shell script, Powerful Script Language
sh 유닉스에서 사용하는 수퍼쉘
bash 리눅스에서 사용하는데 sh쉘에 있는 기능이 거의 포함되어 있다.



****************** 다른 계정 수도계정 권한 주기 ******************************* 
ncloud 접속후 , 다른계정으로 로그인해서 sudo bash하면 권한이 없어서 지정해줘야한다.
/etc/hosts 같은거 수정할 때 고치는 권한이 없다. 팀원user한테 주고 싶을 때 사용.
root계정에서.
root>visudo
	%wheel  ALL=(ALL)       ALL
	%wheel  ALL=(ALL)       NOPASSWD: ALL
    % 부분 제거
$> usermod -aG wheel <user>
$> exit
하고 다시 접속하면 권한 생김

$user> sudo bash
$user> sudo vi /etc/hosts
************************************************************************



파일 압축
$> gzip x.log         # x.log → x.log.gz
$> gzip x.log.gz -d   # x.log.gz → x.log
$> gzip x.log.gz -l   # compress status & list
cf. xz(xz, J), bzip2(bz2, j)
# windows 호환 zip (원본파일은 그대로 남김)
$> zip x.log.zip x.log      <->   unzip x.log.zip
$> zip -P "암호" x.zip x/*
$> tar cvfz xxx.tar.gz *.log
$> tar xvfz xxx.tar.gz


Linux File System Directories  Filesystem Hierarchy Standard
/bin : 기본 명령어있음
/boot : for booting
/dev : device file, cd-rom  #디바이스 마운팅
/etc : config, passwd, rc.d #환경설정 비번파일
/home : user home dir
/lib : shared library
/media : ssd
/opt : application software package
/proc : process info # 보통 프로세스가 실행되면 관련 디렉토리가 생긴다.
/root : root home dir
/sbin : 관리자용, ifconfig
/srv : system data
/tmp : temporary dir
/usr : source or programs
/usr/local
/var : logs, ftp, spool, mail
/lost+found
$>cwd #현재 홈디렉토리 보기
$>cat cpuinfo #cpu 몇개 붙어 있는지 볼 수 있다.  



Linux Ports  IANA (Internet Assigned Numbers Authority)
20  FTP (data) # 보안 쓰렉
21  FTP (Control)
22  SSH / rsync / rcp
23  Telnet
25  SMTP (Simple Mail Transfer)
465 SMTPS 보안 메일 요청하는 포트
43  whois
53  DNS
80   HTTP
443  HTTPS
110  POP3
995  POP3S 보안 메일 받는 포트
123  NTP (Network Time Protocol)
143  IMAP2/4
993  IMAPS
514  SysLog



Command Line Tips
$>man ls  # 매뉴얼 도우미
$>touch  # 작업시간대 변경됨 reload개념.
$>head 5  # 상단만 5줄만 보기
$>ls -il # 디렉토리 트리구조잔아. 그러니까 디렉토리보다 인덱스 값이 있는데 그걸 볼수 있음.
$>tail -f # 마지막 꺼 지속적으로 표시해줘 == more.less
$>clear
$>cat /etc/passwd # 유저목록 보기
*************************************************************************
# claer 안될때 설치
$>yum install ncurses
*************************************************************************

