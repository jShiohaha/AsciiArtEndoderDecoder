file_data = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
               sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
               enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
               aliquip ex ea commodo consequat.'''

encoded_file_data = b'\x01\xd7\xde\x00\x19\xa1L\xa801010101\xa1o\xa40111\xa1r\xa511010\xa1e\xa41100\xa1m\xa40010\xa1 \xa210\xa1i\xa41111\xa1p\xa6010111\xa1s\xa511101\xa1u\xa40000\xa1d\xa511100\xa1l\xa501101\xa1t\xa40100\xa1a\xa40011\xa1,\xa71101110\xa1c\xa501100\xa1n\xa40001\xa1g\xa71101101\xa1\n\xa6010100\xa1b\xa71101100\xa1q\xa6010110\xa1.\xa70101011\xa1U\xa811011110\xa1v\xa801010100\xa1x\xa811011111U\xbf\\\x96\xfd\x7fa-\xe5\xed\xbf[\xdf\xd3N\\\xa7v\xb2\xf1\xf7\x96S\x94\x87Z~~\xbf\xfd\xb3\xf1\xed\xdc\xb7\xf4\xee\xd50\x7fy\xe6\xf2\xfb\x9f\x87\xb2\xbf\x9a\x9c\x95{\xf5\xbf\x1b?\xe7\xfc\x84i\xa1Ml\xfb/\xd77)\xbc\xbd\xb7\xeb\x9aS\xed\x8c\xf4\xed\xfdhN\xafw\xa9\xaa`\xfc\x8f\xe5\xa7\xe6\x97\xe3\xf9j\xa7#\xf9\xcb\xbbV\x87\xfd\xd1\xbf\xb4\xea\x1enw\xf9\xd5\x9f\xa4\xe9\xfb\xc7B\xdbg+/\xad\x9fe\xfa\xff\xba?\xf7\xfa\x14\xd50y\xdb\xfa\xd0\xfd}\xce\xfe\xe4\xf5\x97\x94\xaf\xe5\xf5\x97\x8f\xbc\xad\t\xd2\xae'

file_data_big = """.......................'....''.',,..,,,,,;;;:;'','..''.,,'''''....';:c:''::;,;:::ll::ccc;;lddlcclool
...................''......'','.'''',''',,,;::;';;'....'''',''...,::;,,,,;;;:ccloooolcc:::codl::;:cx
............................''...,,,,,,,,',;,,,,,'..'','''.''...':lc,.',,,;:llcldlcoolcllclxxdolccod
....................''...........','',,,,,,;,',,,,''..'.....'....';:;,;,',::cccodlllllclllllolccldxd
.....................''''......''....''',,,'..',;;;;,'..''........';::;;',;,;ccc::clol:cllcoxxxoldxx
.......................''.....'''''.'''','''..';;,;;;,''',;;,,;'.'',;cc;,,,,;;:c;;;;cc:clccldkOdxxod
.................'.............''''..','''''..',,''''''''',:;:ll;',;;:c::loc:;::,;;;:ccclc:ldxkddlok
................'......'.......''''',,,,;;,,:lxkxxxdl;:c::;,;;lOkl:;::cok00Kkdl:;;::;::ccdddxocldddx
..................''.''...,,'.''',';cldkOOkkKXXXXXNNKOkddOklokKNWKdlccldkkkKXKkc:::::ccclddoxxdxxkkx
..................'''''',lO0kxxdolldO0XXNNNNNNNNNWWWWWNXXWNO0WMMKdolccloxxokNN0xl:;;:ccclddlokkkkkOx
..................''',:okKXXXXXXXXKKKXXXXXXXNNNNNNNNNWWWWWWMMMMMN0KKOkkkO00XXKK0xlc:clc::clodkkkOkkx
...........''...'',;cdOKXXXXXXXXXNNXNNXXXXXXXXNNNNNNNNNWWWWWMMMMMMMMWWWWWMWWWWXOxkkdc::::::loxxxkkxo
.............,,cdkO0KXXXNNNNNNNNNXXXXXXXXKXXXXXNNNNNNNWWWWWWWWMMMMMMMMMMMMMMMMMWNXK0xocccccldkkkOOkk
.........',cok0KXXXXXXNNNNXXXXXKKKKKKKKXXKKKKKXXXNNNNNWWWWWWWWWMMMMMMMMMMMMMMMMMMWWWNKOxolodxk0XXXNW
..'....,lkKNWWNNNNNNNNNNNNXXK0OOOOOOO000OO0KKKKKXXXXNNWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMWXK00KXNWWMMM
.....';xXWWWWWNNNXNNNXXXXXXK00OOkkkxxxkkkxO0KKKKXXXXNNNWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
.....;kXNWWWWNNXKOkxxxxxxxkkkkkkkkkkxxxkxkOO00KXXXXNNNNWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW
....;kXNNXXX0koc:;;;;;::;:loddxkkxxxxxxxxkkkO0KXXXXXNNNNNNWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
....,oO0KK0o;...',,;;;;,,;::coxkkxddddxxxxkkO0KKXXXXXNNNNNNNNNNNWWWWWWWWWWWWWWWWWMMWWWWWWWMMMMMMMWWW
....'',:cl:'..'''''',;;,,;;:lodxkkkdoodddxxkO0KXXXXXXXKXXXXXXXNNNNNNNNWNWWWWWWWWWWWWWWWMMMMMMMWWWWNN
..............'''''',;,',,,;clodkOkxoloddddxkO0KKKKKK00KKKKKKXXXXXXXXXXXXXXXXXNNNNNNNNNWWWWWWNNNXXK0
................','',,;;;;;;,:ox0KOxollddoodk00000000O00000000000000O000000000OOOO00O000KKKKK00OOOkk
..................',,;;,,;:;:cod0KOxollodoodkOOOOOOOOOOOOOOOOkkxxxxddddddxddoddoooddooddxxkkOOkkkkOO
..........'.......,;',,',;lc:coccdxkolllooddkOOOOOOOOOOOOOOkxddoodollldxxkkkxxxolcllllddoddxxxxkkkkO
.......''..'''''.',,....';::;:cccclddlooodxxkOkkkkkkkOOkkOkkdooloooxkOKXXXXXKOdl:,;:cldxxxxxdooodxdd
...........'''...,,'.....',,;::lolooooddddxkkkkxxkkkkkkkxdddxxxkO00XNNNNNNXXOl,,,..':ccldxdddooooooo
..........'.','.',;,''....',,;;lddocclloodxxxkkkkxxxxkkxddoxk0XXXNNNWWWWNNNXOc''...,;::::cc:coxxdddd
........''..,;,''..'''..',,.',;coxo;,;:::ldxxxkkxxdddxkxxk0XXNNNNWWWWWWWNNNXOc''''.',,,;;'''':lxxxdd
.......'''.',:;'.....'''',,,'',;:ll:;:c::clooxxxdooooxO0KXNNNWWWWWWWWWWWWWWNXd,';,',;,.''...',:odxxx
..'.....'..,,,,.......''',,'',;:ccc;,;::cc::clllloodxOKXNNWWWWWWWWWWWWWWWWWWWNkdxxdoc,.....',;lloxdl
....''...'''''.........''','',;c:::::;;;cc:cllllodxO0KKKXNNWWWWWWWWWWWWMMWMMWWMMWNKkl,'';,',:lolx00O
.''''',,......',,''....'''''',,;:;col::::::llllxOKXXXNNNNNWWWWWWWWWWWWWMWWNXNWWWNKdlc,',loooxxxxkOO0
...',,,''....''',,''..',;;,,,,;cloodo::c::lllox0XXNNNNNNWWWWWWWWWWNWWWNWWXKOXWWXkocld:':x0KXNNXKK00O
...',;;'....','',;,;;;:::;;;,;:oxxoc::::ccllokKNNNNNNNNNWWWWWWWWWWWWWWNWWWWWWWWKdclolccldkKNNNNKO0Od
..'''''''',,''.,;;;:::;;;;;::clool:;;:::cclokKNNNNXXXNNNNWWWWWWWWWWWWWWMMWNWWWXko:;codlloxKNNNWNK0Ox
..'''...',;:;,,;;;;;;;::ccccccll:;;:::c::cokKXNNNNNXXXNNNNNWWWWWWWWWWWMWNKK0kxdlc:;:ldxxxk0KKKXNNWNN
..'''',,,;;:::::ccccccc:ccc::cc:;,;:clllcokKXNNNNNNNXXXXXNNNNNNWWWWWWWXOl:::,,;:c::cccoddxO00kkO000K
;;;:::cccccccllolclllccccccccc:;;;;::cllokXXNNNNNNNNNNXXXXXXNNNNNNNNWWXk:,;,,;;;:coodoloodxxoloodxxk
:cclolllloooooooooollclcccllcc;;:::;;clod0XXNNNNNNNNNNXXXXXXXXXNNNNNNWXx:,',,,::;:okOkxxxxxxddcclodx
lodddooodddddddddooooooolloolc::::::clookXNNNXNNNNNNNNXXXXKKKXXXXNNNXNKo,,'',,;;;:lollllloodxdoclodk
ooddddxxxkxxxxxdoddoddxxxdol::::;:ccclodONNXNNNNNNNNNXXXXXKKKKKKXXXXXXXx;'',,;,;::;;;;;;::::lllokKXX
ddddddxxxkxdxxxdddddxxxxkxolc:::;:clllod0NNNNNXXXNNNNXXXXXXKKKKKKKKKKKKx;''',,,;;,,,,,,,;::cllk0KNNK"""

encoded_big_file_data = b'\x01\x90\xde\x00\x13\xa1.\xa3110\xa1\'\xa41011\xa1,\xa40110\xa1;\xa40011\xa1:\xa40101\xa1c\xa40000\xa1l\xa40001\xa1d\xa511111\xa1o\xa511110\xa1\n\xa6101000\xa1x\xa40010\xa1k\xa510101\xa1O\xa501110\xa10\xa6101001\xa1K\xa501111\xa1X\xa41000\xa1N\xa41110\xa1W\xa41001\xa1M\xa40100\xc2\xf7\xc0\x97\xbe\xdd\xad\xdd`S\x03Y\xefv\xdfv\xf7\xd6\xb6\xc1p%\xce\xb0\xae\xf7Z\xce\xd3\xa8\x18\xc6\xb5\x80\x19\xce?\xff\x18B?}\x1d\x1c\'{\xe0k\xdd\xb7\xdb\x04m\x81\xb0\x19\xd6\xb3\xdc\xe7\xbe\x04\xb0F\xde\xf8\r\xabY\xd8\x10\xc0\xd6\x10\x8f\xc0\x83\x08T\x0c>\xfe5\xac\xeb\th\xe1\xcb\xdf\x01\xb0E\xdav\x05\xbe\xed\xee\xdb\x03\xdb\xdf\x01\xddc\x0bv\xec\x06u\x8ca\x1f\xe3\x0f\xbe\x8c#\x18FR\xff\xe8\xc2\x1f\x7f\xa3\x85/|\x17v\xde\xec\x0cv\xdd\x81/}\xdb\xe0[\xe0K\x9dgi\xdbv\xad`\x07\xef\xe2\n\x11\x05\xf4a\x08\xff/\xf4p\xad\x82`k\xdf\x02X\x1b\x01\xdfv\xed0F\xdfv\xf7\xc1\x17:\xd6s\xdd\xa7i\xc0\rk\x08\xfd\x1a\xc21\x87\xd2\x03\xf4\x7f\x94\xb4p\xbd\xef\x81l\x17l\x11\xb6\x07\xbbs\x9d\xa6\x06\xdb\x03i\xce\xd6\x9e\xfb{\xb4\xe1\t\xd8\x10\xe7XL\x10!XF\x10\x8f\xfa\xdd\xfc\xa5\xf7\xfa8F\xf86\xc17n\xdb\x05\xdd\xbb[a-Y\xd61\x9e\xed9\xd6\x15\xac~\x85gZ\xda`k\x001\x85c\xfc\xb5\xff\xf8\xfd\xae\x8e\x10\xbe\x06\xbe\x07\xb0V\x049\xda\xd5\x8c\xb5\x90\x1f\xe3:\xc2\xb5\x9d\xa78\xdd\xack:\xd6\x1fk\xa7M\xfa\xff\x1a\xceu\xac\xebXC\xf02\xfa\x11\xfc\x0c\xb4p\x95\xef\xb7\xbe\x03ko\xb6\x06\xdb\x9c#\xfe\xb7]\xae\xb7\xe0\x17\xbd}\xda\xff\xfd\xda\xc7\xedo\xf6o\xfe0\x84\x7f\xd4\r\xf8\xbfXT\x14\x00\xc7\xff\xfe\x94\xbf\x94\xb5\xd6Z8J\xc1\x9a7i\xd6R\xff\xe8\xc7\xfb\xb4\xe3\x1e\t\x90^\xc63\xeb\xb4\xe6\x94\xbf\xff\xa3\x08G\xe9K\xed}\xed2\x8dg:\xc0\x0c\x7f\xfe?j\n\xe9h\xe1+\x03j\xfd\xad\xf8\x08x\x1c\x03\xf0L\x83 /i\xbe\xfb\xb5\x03v\x9d8\xc5\xf7\xe9\x94aXF\x15\xac#\xf7\xfa\x81\xbb]e\xa3\x82\xef|\x07{\xb4\xe1\xfd\xd7\xe0\'\xbd\x8f{\x01\x1c\x13 \xa8\x11 \xa9\x90H\xbaZ\xeb\xfc*\x0c?H\x0e\xba\xcb\xed\x1c\x1a\xd6\x87\xfa\xdd\xa6\xfc\x01\xf0L\x04?\x00\xbc\x0f!\x08#>\xc5\xfae\xf4\x01G\xfd@\xddv\xba\xe8\xe0\x9b\xb4>\xd7M\xf8\x06\xe0H\x05xDb\xf0X\x03\xe0Y\tA)\x03\xeb\xee\x97\xd1\xfb\xf9k\xa7\x00}\x9d\x1d\xdb\xe0F\x8e\xb7\xfb9\xf0db\xfd7\x03\xd2\x06\xeb\xb4\xde\x0b\x00\x9d\xec\x84 \xcc\xe2\xfd:o\xc7\xb3\x9a\x01\xd1\xc0\xb79c \xbc\x07\x1e\x03\x80g\xe9\xd3u\xda\x81\x90\x1d@\xca\xed7\x82@\'\x01\xc8J\x12Q\xc0\xa7\xae=\x90N\xf6/\xbbY\x03\xd4(\x80\xeb-n\xbbN\x9b\xf0\t\xc0\x92\x10\x84\x93\xa3\x81\x0f\\{\xd8\x03\xa7_\xa1Y\x82\xadgX\xfd\xff\xf2\xd7Y\x04T\r\xdao\xc0/\x03H:\x11\xd1\xc0\x8d\xf5\xdao\xbfO\xd3\xe0;\xb5\xa6\x08\xd6\x9dk\x0f\xa5\xae\xb2\xfc\x10\x81+\xad\xdao\xbf\x00\xbc\x17")L\x83\xa0<\x81\xd1\xc0\x97\xbbV\x11\xae\xfb\xb6\x0c\xd3\x9d\xad9\xd6?\x7f-@\xff\xf7\xdf\x81\x94\xb5\xbbM\xf8\x07~\x01\xf8"}\x90\xf4\x07\x90N\xf6\x8e\x0e\xb0f\x9d\xb7`3\x84~\xff[\xb5\x97\xd1\xfb\xf0B\xd6\xed7\x83S\xa6\xf0h\x11\xe0\x99\x06\xe08\xc5\xfatp\x85\xdb{\xb5\xa6\x0c\xd5\xfaZo\xba_F?\xff\xf7\xdf\xeb\xa4!\xdaC\x9d\xa4%\xc0\x94\xe9\xbbH\x1b\xc1i\xd3p\x1du\xd1\xc2WkNv\xb4\xeb:\xc3\xef\xf4\xdft\xbe\x8c~\xff\xef\xbf\xd6\xe1\n\xeb O\x83\x17\xff\xfd\xff\xff\x01\xff\xff\xbe\xff\xf9K]n\xbbPG]\xa3\x82\xaf\x81\xda{\xb5\xb7i\xc6\x15\x87\xd0\x87\xf2\xd7\xe8\x81\xfb\xef\xff\xd6\xe0\xea\xcb\xff\xfe\xfb\xff\xa2\x07\xf9KP2\x03\xf4a\x10O\xff\xf7\xff\xc8\x12\xa0\x8e\xd1\xc0\xf7\xbe\xed\x82\xed\xda\xdc\ts\xadgX\x02\x0f\xff\xc7\xe0?\xcaZ\xdd\xa8;\xae\xd7[\xb5\xd7\xff\xbe\x8f\xc0e\xad\xd7\xe0\x15\xf7\x7f\x1a\xdau\x84\x7f\x90/\xfe\x03\xfc\xbf\xffG\x05\xd8\x1e\x03ko\x81n\xd6\x9dk\x1f\xa3\xf0\'\xc1\x0bPB\x96\xa0\xe5\xf8\x19\x01\xd6\xed:q\xe0h\xc5\xd1\xb0\x1e\xed\xd6\x10\x8f\xf2\xfc\x0f\xc0\xf4pU\xf6\xed\xbe\xdd\xa7m\xef\x81.\xd6\x9c\xe3\xff\xffB\x11\x8f\xdf\x7f :\x82\x10%u\x97\xff\xfd-t\xe0\x0f\x80\xe4\x13\x80\xe2\xe8o|\x06\xd3\xa8 B\xb0\xfaR\xfc\x12\x8e\x08\xbd\xf7Zv\xde\xfb\xb6\x07\xbbv\xb7n\xd3\x87\xd2\xfav\x9d@\xc7\xf9\x01\xd7YK\xf02\xd6R\xd7N1\xe0I\x07\xe08\xba\x1b\x04\xdb\xb0\x19\xcf`\x8b\x19\x01\xff\xfd\x1c\x0f`{v\xac\xf7\xc0\xb6\x08\xc0w\xbbN\xb1\x8dgXV\xb0\x8f\xdfH\x0f\xff\x02\x15\xdao\xc7\x80\xe4;\xb1\xfd\xb7;n\xd3\xb7o|\x07v\xaf\xdf\xc8\x0e\x8e\xed\xf0-\xf7X\x13\x03\xd8\x1b[{\xb4\xeb\x003\xb4\xebXB\xb5\x84A=\xf7\xf2\xba\xfc{\xd9\x13\xed\x7f\x94\xbf\xfa\x16\xe0[\xb4\xe3\x1f\xa5\xfctp%\xef\x80\xec\x17\x04\xd8\x1bov\x9c*\n`a\n\xc2 \x9e\xfeWi\xbc\x0e=\xec\x86%3Jg4\xa6}~\xb1\xb6\xf7;n\xd5\x8f\xd1\x96\x9d7h\xed\x82\xb5\xb8\x1a\xedm\xef\x81,\x19\xad:\xce\x1fF\xa0\xc2\x08W_\x80>\x05\x90\xd4\xce}\x8fd\x0f\xaf\xfe0\xb6\xed\x1f\x80\xc8\x12\xb7]\xa7G\x01\xdd\x80\xef|\t`mm\xef\xbbv\x9c\xec\x08p\x8f\xdf\x7f\xf5k\n\xd6 ~\x96\x9cc\xc0\xd2\x15\xd9\x03\xec\xe7\x17\xdd\x8c\xe7\x1a\xfd\x08\xff]\xd6Zo\xc7\xbd\x8b\xef\xd3\xa6\xed\x1c\x07v\x9c\xf7\xc0\x97m\xee\xd3\xb4\xc0\xd4\x0c\xc0\xdau\xfaR\xfa\x15\x04\x08F?k\x7f\x82d;\xb2\x10\xff\xe1\x1f\xa3\x08G\xfdo\xf0#\xee\xd3w\xfa;\xb6\x10\xd6\xde\xfa\xd3\x03P3\x05Z\xc2?}\x1a\xceu\x03\x08G\xedo\xf0$\x01\xf0$\x87%3\xec\x81\xc6\xbfVp\xfb\xf8\xc7\xe9_\xe09\xf5\xfan\x96\x8e\xed\x81\xe0;\xb4\xeb;Z`\xebX\x03\x0ck9\xd4\x0c+X}\xad\xf8\xf0,\x01\xf0,\x85\xa6}}\xfau\x97\xf1\x85gX\xff :\xe9\xbc\x0e=\xec\xfb\xda;\xb6\x08\xc0g:\x82\x80:\xc0\rk\x08Vv\x9da\x100\xfb[\xf1\xe0x\x05\xe0i\x07\x8b\xa3P6\xb4\xeb\n\xd6\x00~\xff\xf9]\xa7N\xba\xdd\xa4\r\xfa&\x06\xa0`\x0e1\xfa0\x88\x18\x04\xac\xc1\x16\xb0\x8c~\xd7\x18\xf0T\x03pD\xe7\x1a\xd6\xd3\xb5\xa6\x06\xb0\xfb\xef\xfe\x8f\xdf\x7f)}\x1f\xbe\xfeR\xd7Ea\x08\xfd\x10O\x05\x0ca\x18\x01\x8ca\t\xce\xa0g8G\xef\xf4\xe3\x1e\n\x80\x9e\x06\x9cJ\xb6\xdd\x80\xd6\xb3\xaf\xda\xdd\xac\x81\xbf\xfc!\x1f\xbf\x96\x88\xfd\xf8\x1f\x80\xfe\x13\xe0q\x8f\xdfF\x15\x06\x08\xfd\xf6\xb8\xf0\x1cx"\x01\x1e\x07\x00\x9c\x07\x1e\xbf\xeb[{\xb5\xa6\x06\xb1\xfa \xbe\xfb\xf9\x7f\xf4#\xf7\xfa\xe8\xfb\xef\xc1\x08\x0e\xb2\x05\xff\xdf\xff\xf7\xff\xc8\x0f\xffF\xa0\x87X\x01\x8f\xdf\xdd\xefc\xc10\n\xf0h\x07)\xefv\xb4\xed:\xd6`\xca\x08 ~\xd6\xfccG\xe0\xc4\x07Y\x7f ?\x82\x90%e\xf4aP3\xac"\x07\xef\xf4\xf8\x16\x00\xf8\x12\x01\x9e\x18S\xd8\x1b\x01\x9c\xec\x0eu\xac#\x1dt\xdf\xef_'


binary_file_data = b'''\xda\x01\xbdLorem ipsum dolor sit amet, consectetur adipiscing elit, 
                          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
                          enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
                          aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
                          in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
                          sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
                          mollit anim id est laborum.'''

non_ascii_file_data = '''Lorem ⇐ipsum dolor sit amet, consectetur adipiscing elit.'''