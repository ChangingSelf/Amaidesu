"""
模拟弹幕数据，用于测试和开发
"""

# 模拟用户数据
MOCK_USERS = [
    {"id": 1001, "nickname": "小北故事多", "cardname": "小北故事多"},
    {"id": 1002, "nickname": "夏天的风i", "cardname": "夏天的风i"},
    {"id": 1003, "nickname": "陈旧记忆", "cardname": "陈旧记忆"},
    {"id": 1004, "nickname": "落尘染流年", "cardname": "落尘染流年"},
    {"id": 1005, "nickname": "星辰大海", "cardname": "星辰大海"},
    {"id": 1006, "nickname": "柠檬味少女", "cardname": "柠檬味少女"},
    {"id": 1007, "nickname": "时光漫步者", "cardname": "时光漫步者"},
    {"id": 1008, "nickname": "云上的猫", "cardname": "云上的猫"},
    {"id": 1009, "nickname": "午后蓝调", "cardname": "午后蓝调"},
    {"id": 1010, "nickname": "南巷清风", "cardname": "南巷清风"},
    {"id": 1011, "nickname": "木子李23", "cardname": "木子李23"},
    {"id": 1012, "nickname": "沉默是金_", "cardname": "沉默是金_"},
    {"id": 1013, "nickname": "奶茶加冰", "cardname": "奶茶加冰"},
    {"id": 1014, "nickname": "流星雨心愿", "cardname": "流星雨心愿"},
    {"id": 1015, "nickname": "一个小白兔", "cardname": "一个小白兔"},
    {"id": 1016, "nickname": "喵了个咪w", "cardname": "喵了个咪w"},
    {"id": 1017, "nickname": "淡忘悲伤", "cardname": "淡忘悲伤"},
    {"id": 1018, "nickname": "春风十里不如你", "cardname": "春风十里不如你"},
    {"id": 1019, "nickname": "江湖故人", "cardname": "江湖故人"},
    {"id": 1020, "nickname": "橘子味汽水", "cardname": "橘子味汽水"},
    {"id": 1021, "nickname": "幽蓝梦境", "cardname": "幽蓝梦境"},
    {"id": 1022, "nickname": "冷月葬花魂", "cardname": "冷月葬花魂"},
    {"id": 1023, "nickname": "繁华落尽", "cardname": "繁华落尽"},
    {"id": 1024, "nickname": "小鱼干干", "cardname": "小鱼干干"},
    {"id": 1025, "nickname": "无糖可乐", "cardname": "无糖可乐"},
    {"id": 1026, "nickname": "一只小猪猪", "cardname": "一只小猪猪"},
    {"id": 1027, "nickname": "白云苍狗", "cardname": "白云苍狗"},
    {"id": 1028, "nickname": "浅笑安然", "cardname": "浅笑安然"},
    {"id": 1029, "nickname": "夜空中最亮的星", "cardname": "夜空中最亮的星"},
    {"id": 1030, "nickname": "清风徐来", "cardname": "清风徐来"},
    {"id": 1031, "nickname": "梦里花落知多少", "cardname": "梦里花落知多少"},
    {"id": 1032, "nickname": "半世浮生", "cardname": "半世浮生"},
    {"id": 1033, "nickname": "樱花旳落", "cardname": "樱花旳落"},
    {"id": 1034, "nickname": "空城旧梦", "cardname": "空城旧梦"},
    {"id": 1035, "nickname": "忆往昔", "cardname": "忆往昔"},
    {"id": 1036, "nickname": "夏日微光", "cardname": "夏日微光"},
    {"id": 1037, "nickname": "寒风冷雨", "cardname": "寒风冷雨"},
    {"id": 1038, "nickname": "墨染青衣", "cardname": "墨染青衣"},
    {"id": 1039, "nickname": "琴韵悠扬", "cardname": "琴韵悠扬"},
    {"id": 1040, "nickname": "红尘过客", "cardname": "红尘过客"},
    {"id": 1041, "nickname": "半夏微凉", "cardname": "半夏微凉"},
    {"id": 1042, "nickname": "情书与酒", "cardname": "情书与酒"},
    {"id": 1043, "nickname": "温柔的猫", "cardname": "温柔的猫"},
    {"id": 1044, "nickname": "星月神话", "cardname": "星月神话"},
    {"id": 1045, "nickname": "阳光温暖", "cardname": "阳光温暖"},
    {"id": 1046, "nickname": "故事里的小黄花", "cardname": "故事里的小黄花"},
    {"id": 1047, "nickname": "风中的承诺", "cardname": "风中的承诺"},
    {"id": 1048, "nickname": "山水不相逢", "cardname": "山水不相逢"},
    {"id": 1049, "nickname": "余生请指教", "cardname": "余生请指教"},
    {"id": 1050, "nickname": "你的眼睛", "cardname": "你的眼睛"},
    {"id": 1051, "nickname": "葬心于红尘", "cardname": "葬心于红尘"},
    {"id": 1052, "nickname": "花落满地", "cardname": "花落满地"},
    {"id": 1053, "nickname": "落花无意", "cardname": "落花无意"},
    {"id": 1054, "nickname": "风吹过的夏天", "cardname": "风吹过的夏天"},
    {"id": 1055, "nickname": "时光不老", "cardname": "时光不老"},
    {"id": 1056, "nickname": "旧梦失词", "cardname": "旧梦失词"},
    {"id": 1057, "nickname": "别来无恙", "cardname": "别来无恙"},
    {"id": 1058, "nickname": "流年如歌", "cardname": "流年如歌"},
    {"id": 1059, "nickname": "倾城一笑", "cardname": "倾城一笑"},
    {"id": 1060, "nickname": "青丝蓦然回首", "cardname": "青丝蓦然回首"},
    {"id": 1061, "nickname": "北巷清风", "cardname": "北巷清风"},
    {"id": 1062, "nickname": "暮色沉沉", "cardname": "暮色沉沉"},
    {"id": 1063, "nickname": "森林里的熊", "cardname": "森林里的熊"},
    {"id": 1064, "nickname": "钢铁直男", "cardname": "钢铁直男"},
    {"id": 1065, "nickname": "黑白键的交响", "cardname": "黑白键的交响"},
    {"id": 1066, "nickname": "北极的企鹅", "cardname": "北极的企鹅"},
    {"id": 1067, "nickname": "孤狼666", "cardname": "孤狼666"},
    {"id": 1068, "nickname": "游戏王者", "cardname": "游戏王者"},
    {"id": 1069, "nickname": "沙漠玫瑰", "cardname": "沙漠玫瑰"},
    {"id": 1070, "nickname": "深海里的鱼", "cardname": "深海里的鱼"},
    {"id": 1071, "nickname": "萌萌哒小仙女", "cardname": "萌萌哒小仙女"},
    {"id": 1072, "nickname": "千杯不醉", "cardname": "千杯不醉"},
    {"id": 1073, "nickname": "小小的猫咪", "cardname": "小小的猫咪"},
    {"id": 1074, "nickname": "凌云之志", "cardname": "凌云之志"},
    {"id": 1075, "nickname": "我是真的帅", "cardname": "我是真的帅"},
    {"id": 1076, "nickname": "月亮不发光", "cardname": "月亮不发光"},
    {"id": 1077, "nickname": "苏打绿汽水", "cardname": "苏打绿汽水"},
    {"id": 1078, "nickname": "火星上的人", "cardname": "火星上的人"},
    {"id": 1079, "nickname": "地球不爆炸", "cardname": "地球不爆炸"},
    {"id": 1080, "nickname": "飞翔的企鹅", "cardname": "飞翔的企鹅"},
    {"id": 1081, "nickname": "小可爱超甜", "cardname": "小可爱超甜"},
    {"id": 1082, "nickname": "快乐柠檬", "cardname": "快乐柠檬"},
    {"id": 1083, "nickname": "撒娇的猫咪", "cardname": "撒娇的猫咪"},
    {"id": 1084, "nickname": "微笑向暖", "cardname": "微笑向暖"},
    {"id": 1085, "nickname": "阿狸的尾巴", "cardname": "阿狸的尾巴"},
    {"id": 1086, "nickname": "仙女本仙", "cardname": "仙女本仙"},
    {"id": 1087, "nickname": "我是个大橙子", "cardname": "我是个大橙子"},
    {"id": 1088, "nickname": "旧巷老猫", "cardname": "旧巷老猫"},
    {"id": 1089, "nickname": "心理学大师", "cardname": "心理学大师"},
    {"id": 1090, "nickname": "鱼塘霸主", "cardname": "鱼塘霸主"},
    {"id": 1091, "nickname": "奶瓶突击队", "cardname": "奶瓶突击队"},
    {"id": 1092, "nickname": "猫头鹰先生", "cardname": "猫头鹰先生"},
    {"id": 1093, "nickname": "代码搬运工", "cardname": "代码搬运工"},
    {"id": 1094, "nickname": "咖啡因上瘾", "cardname": "咖啡因上瘾"},
    {"id": 1095, "nickname": "脆皮黄瓜", "cardname": "脆皮黄瓜"},
    {"id": 1096, "nickname": "小猪佩奇", "cardname": "小猪佩奇"},
    {"id": 1097, "nickname": "可爱多冰淇淋", "cardname": "可爱多冰淇淋"},
    {"id": 1098, "nickname": "电竞少女", "cardname": "电竞少女"},
    {"id": 1099, "nickname": "键盘侠", "cardname": "键盘侠"},
    {"id": 1100, "nickname": "摸鱼达人", "cardname": "摸鱼达人"},
]

# 模拟消息内容
MOCK_MESSAGES = [
    "主播技术太强了！",
    "这游戏的难度曲线也太陡了吧",
    "主播声音也太好听了，像天籁",
    "6666666，无敌了",
    "主播这手速我服气了",
    "这个连招我看傻了",
    "主播今天气场全开",
    "请问这是什么游戏啊？看着好好玩",
    "主播笑起来真可爱",
    "好可爱的主播，想偷回家",
    "这游戏在哪买的？我也想玩",
    "手速也太快了吧，跟不上",
    "主播反应能力真好",
    "这么精准的操作，厉害了",
    "这伤害爆炸啊，对面要哭了",
    "打得太凶残了，心疼对面",
    "主播的水平直接起飞",
    "这波操作简直完美",
    "这游戏主播已经玩通关了",
    "绝了，这操作我看一万遍都不会",
    "awsl，这也太可爱了吧",
    "主播今天化妆了吗？好好看",
    "前方高能预警！",
    "这个游戏我昨天才通关，好玩",
    "为主播打call！",
    "主播能唱首歌吗？",
    "这个地方我卡了好久",
    "主播长得真好看",
    "啊啊啊我酸了",
    "这是什么歌，好听",
    "主播的装备好华丽",
    "刚来，错过了什么",
    "主播今天气色不错啊",
    "这个boss我打了十次才过",
    "主播用的什么键盘，声音好好听",
    "我永远喜欢主播！",
    "这操作，我看湿了",
    "主播发际线保持得真好",
    "好家伙，这都能过",
    "主播今天直播多久呀？",
    "这个游戏画面真精致",
    "主播笑起来真好看",
    "这么晚了还在播，辛苦了",
    "主播带我飞",
    "主播的反应真快",
    "有没有一起组队的",
    "这个剧情我哭了",
    "主播的衣服好好看，在哪买的",
    "这个特效太酷了",
    "我来了我来了",
    "我又回来了，刚才网断了",
    "主播素颜都这么好看吗",
    "今天天气真好，适合看主播",
    "主播玩这个游戏多久了",
    "这个剧情我也很喜欢",
    "主播加油，我相信你",
    "主播这个角色玩得真厉害",
    "主播什么时候直播的",
    "这个任务我做了好久",
    "主播好像瘦了",
    "这个音乐是什么，好好听",
    "啊啊啊主播太可爱了",
    "今天的主播特别帅",
    "难道只有我听到了奇怪的声音吗",
    "主播声音好苏",
    "这个游戏好像挺难的",
    "主播会玩其他游戏吗",
    "我来蹲一首歌",
    "这个游戏的剧情真感人",
    "主播的反应好真实",
    "可以求一首歌吗",
    "这个场景太美了",
    "主播好久不见",
    "哇，这个操作我服了",
    "我要给主播打榜",
    "主播这个皮肤好好看",
    "刚下班就来看主播了",
    "好想和主播一起玩游戏",
    "主播今天打扮得真漂亮",
    "我已经追了主播三个月了",
    "这个装备很难得吧",
    "主播怎么这么可爱",
    "这个回合好险啊",
    "主播的技术越来越好了",
    "这是我第一次看主播直播",
    "主播这个头像是在哪里换的",
    "新来的朋友可以点个关注吗",
    "主播今天火力全开啊",
    "这个关卡看着就难",
    "主播能介绍一下这个游戏吗",
    "真希望主播天天直播",
    "主播的头发真好看",
    "这个房间好漂亮",
    "主播的表情太可爱了",
    "好想抱抱主播",
    "玩这个游戏会上瘾吗",
    "主播今天好像很开心",
    "这个背景故事好让人感动",
    "主播的眼睛真好看",
    "好喜欢主播的风格",
    "这个游戏的配乐真棒",
    "今天是特别场吗，怎么这么多人",
    "每天都要来看主播",
    "主播的直播时间好准时",
    "这个游戏的战斗系统真不错",
    "主播今天声音有点不一样",
    "这个游戏节奏好快",
    "我觉得主播玩这个游戏超厉害",
]

# 模拟直播间信息
MOCK_GROUP_INFO = {"group_id": 114514, "group_name": "测试直播间"}
