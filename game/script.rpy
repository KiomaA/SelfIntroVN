# 遊戲腳本位於此檔案。

# 聲明該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define k = Character("祈奧馬")
define v = Character("凡泰爾", color="#12b3b3")
define m = Character("巫摩西",color="#140849")
define mq = Character("???",color="#140849")
define p = Character("珀西瓦爾七世", color="#886c25")
define t = Character("敵軍首領",color="#581616")

# 遊戲從這裡開始。

label start:

    scene bg black

    voice "voice_1_1.wav"
    "假如一切歷史都重寫……"
    
    voice "voice_1_2.wav"
    "去到一個會理解魔法、以魔法為本的世界……"

    voice "voice_1_3.wav"
    "一般人跟魔法師都可以融洽相處……"

    voice "voice_1_4.wav"
    "這樣的世界會不會更美好呢？"

    voice "voice_1_5.wav"
    "帶你去一個充滿魔法的異世界……"

    scene bg palace
    play music "bgm_palace.mp3" loop

    voice "voice_1_6.wav"
    "這裡是卡美洛，一個在異世界的王國"

    voice "voice_1_7.wav"
    "自亞瑟王統治以來，已過了數千年"

    voice "voice_1_8.wav"
    "人們理解、包容魔法師，享受魔法帶來的生活便利，並建立共融的社會"

    voice "voice_1_9.wav"
    "而魔法師創造魔導裝置，改善人們的生活"

    voice "voice_1_10.wav"
    "並透過魔法擊退魔物和黑魔法師，保護國土裡的人們。"

    # 介紹

    show kioma with fade
    voice "voice_1_11.wav"
    "這是祈奧馬・阿凡隆，一個宮廷魔法師"

    voice "voice_1_12.wav"
    "從小對魔法就很有興趣，並擁有著強大的空間扭曲魔法技能"

    voice "voice_1_13.wav"
    "除了魔法之外也熱衷於設計和改良魔導裝置，對空間傳送裝置很有研究"

    voice "voice_1_14.wav"
    "在卡美洛宮廷工作，負責維護王宮裡的魔導裝置。"

    voice "voice_1_15k.wav"
    k "（呼～工作了一整天快累死了）"

    voice "voice_1_16k.wav"
    k "（總算把防禦系統的程序重新編寫完畢……）"

    voice "voice_1_17k.wav"
    k "（但是這樣看來王宮的防禦設備還是需要加強呢……）"

    voice "voice_1_18k.wav"
    k "（什麼時候才能有足夠的材料製作新的防禦裝置啊……）"

    hide kioma

    show vatar with moveinright

    voice "voice_1_19.wav"
    "這是凡泰爾・阿凡隆，祈奧馬的雙胞胎弟弟"

    voice "voice_1_20.wav"
    "從小修練戰鬥系魔法，也隨在騎士團的父親練習劍法和戰術"

    voice "voice_1_21.wav"
    "成年後便進入騎士團征戰，現時為宮廷衛隊隊長"

    voice "voice_1_22.wav"
    "除戰鬥魔法外，也擅長抵擋黑魔法。"

    show vatar at left with moveinright
    show kioma at right with moveinright

    voice "voice_1_23v.wav"
    v "哥哥～！"

    show kioma surprised

    voice "voice_1_24k.wav"
    k "凡泰爾？你怎麼會在這裡？"

    voice "voice_1_25v.wav"
    v "辛苦了哥哥！看到你終於把防禦系統修好了就來找你了！"

    voice "voice_1_26v.wav"
    v "我們等下一起吃飯然後休息一下吧！"

    voice "voice_1_27k.wav"
    k "話說你今天不是在練附魔劍法嗎？練了一整天你不累嗎？"

    voice "voice_1_28v.wav"
    v "還好啦，只是新的那把劍是雷屬性，我要慢慢掌握才能熟練"

    show kioma
    voice "voice_1_29k.wav"
    k "話說我們等下去哪裡吃好呢？魔法區最近有新開的餐廳要不要試試？"

    voice "voice_1_30k.wav"
    k "也順便去市集看一下魔法裝置的零件……"

    voice "voice_1_31v.wav"
    v "好欸！我們一起出發吧！"

    voice "voice_1_32v.wav"
    v "等下在市集也想看看魔劍和附魔材料！"


    # 戰爭中的皇城

    scene bg black
    stop music

    voice "voice_1_33.wav"
    "本以為這樣的日子會一直下去……"

    voice "voice_1_34.wav"
    "怎知，黑魔法的勢力再次冒起威脅著王國的安全……"

    scene bg war
    show king at left with moveinright
    show vatar surprised at right with moveinright
    play music "bgm_epic.mp3" loop

    voice "voice_2_1v.wav"
    v "陛下，黑魔法軍正在包圍皇城，還要求陛下交出王位，否則把皇宮夷為平地"

    voice "voice_2_2p.wav"
    p "可惡！這些黑魔法師整天只會搞破壞，現在還想逼我讓出王位？豈有此理！"

    voice "voice_2_3v.wav"
    v "陛下可放心，我們衛隊以及騎士團將會堅守到底，不讓黑魔法師們得逞。"

    voice "voice_2_4v.wav"
    v "在下先行告辭前往前線，請陛下多加保重。"

    hide vatar with moveinright
    "..."
    show kioma at right
    show kioma serious
    show king surprised

    voice "voice_2_5p.wav"
    p "祈奧馬，看看出面的情況，你弟應該沒事吧？"


    "轟！！！"

    play sound "sound_explosion.mp3"
    show kioma surprised
    "轟隆隆！！！"

    voice "voice_2_6k.wav"
    k "什麼？竟然是結界爆破術？這下子我們完了……"

    voice "voice_2_7k.wav"
    k "（啊對了，實驗室裡有傳送門）"



    # 傳送門

    scene bg portal
    show king surprised at left
    show kioma serious at right
    play music "bgm_demon.mp3" loop

    voice "voice_2_8k.wav"
    k "陛下，請趕快到這裡，這是傳送門可以將陛下傳送到安全的地方"

    voice "voice_2_9k.wav"
    k "可以將陛下傳送到深山的行宮暫避，附近已經設定了多重結界，黑魔法師會更難以入侵"
    
    voice "voice_2_10p.wav"
    p "什麼？如果身為國王的我也棄守皇城，人民會怎樣想我？"

    voice "voice_2_11p.wav"
    p "想當年我在北方跟你爸一起征戰，一起抵抗敵軍的入侵……"

    voice "voice_2_12p.wav"
    p "原以為捉拿了他們的首領，他們就會乖乖就範不再騷擾我們"

    voice "voice_2_13p.wav"
    p "怎知現在敵軍竟然煽動黑魔法師叛亂，企圖用黑魔法破壞王國？！"

    voice "voice_2_14k.wav"
    k "陛下，我明白這個處境……"

    voice "voice_2_15k.wav"
    k "但是，現在……"

    show king sad

    voice "voice_2_16p.wav"
    p "亞瑟王啊，我罪該萬死，現在我要暫時離開皇城了"

    voice "voice_2_17p.wav"
    p "請繼續看守皇城不要讓黑魔法師得逞……"

    p "..."

    hide king
    with fade
    voice "voice_2_18k.wav"
    k "現在送了國王去安全的地方了，其他人還安好嗎？"


    show kioma at left
    with moveinright
    show kioma surprised
    
    voice "voice_2_19k.wav"
    k "凡泰爾！！！"

    show vatar dizzy at right
    with moveinright
    voice "voice_2_20v.wav"
    v "哥哥！"

    voice "voice_2_21k.wav"
    k "你也快點進入傳送門護送國王吧！"

    show vatar surprised
    voice "voice_2_22v.wav"
    v "你呢？"

    show kioma serious
    voice "voice_2_23k.wav"
    k "我要死守到底不讓這些黑魔法師攻入這裡"

    show vatar serious
    voice "voice_2_24v.wav"
    v "別說傻話了，還是快逃吧！！！"

    voice "voice_2_25k.wav"
    k "不，我可以的！如果使用那個祖傳奧義的話，說不定可以……"

    voice "voice_2_26v.wav"
    v "好吧，萬事小心，我會在那邊等你的"

    show vatar surprised
    voice "voice_2_27v.wav"
    v "其他人也快點進來！！！"
    
    "..."

    hide vatar
    hide kioma
    with dissolve

    # 與敵軍首領對峙

    scene bg palace broken
    show evil laugh

    voice "voice_3_1t.wav"
    t "哈哈哈！你們的防禦系統真的弱得可憐呢！"

    voice "voice_3_2t.wav"
    t "我們只要稍為施法就能輕易打破了！"

    voice "voice_3_3t.wav"
    t "你的國王現在也離你們而去了，看看你這個菜鳥魔法師還可以怎樣？"

    voice "voice_3_4t.wav"
    t "以後卡美洛就是魔法師的天下，由魔法師建立新的秩序，讓麻瓜們成為我們的奴隸吧！！！"

    voice "voice_3_5t.wav"
    t "哈哈哈哈哈哈！"

    show evil laugh at left  with moveinright
    show kioma angry at right  with moveinright
    voice "voice_3_6k.wav"
    k "你們這些自私鬼"

    voice "voice_3_7k.wav"
    k "明明王國已經給予魔法師不少資源以及機會，你們卻不知足，還要搶走其他人的機會？"

    show evil
    voice "voice_3_8t.wav"
    t "屁話，你以為那些麻瓜們會理解你們的魔法嗎？"

    voice "voice_3_9t.wav"
    t "你看看其他國家，魔法師要麼就是統治國家要麼就是被麻瓜清算！"
    
    voice "voice_3_10t.wav"
    t "他們只是想利用你們的魔法，然後不需要的時候把你們全部殺掉！"
    
    voice "voice_3_11k.wav"
    k "什麼歪理，我們國王才不會說這樣的話！"

    show kioma serious

    voice "voice_3_12k.wav"
    k "自古在卡美洛，一般人跟魔法師是平等的不是嗎？"

    voice "voice_3_13k.wav"
    k "還記得梅林對亞瑟王作過的保證嗎？"

    voice "voice_3_14k.wav"
    k "魔法師們會盡一齊努力保護國王保障人民的生活，相對地國王也會保護魔法師們免受外界的侵擾。"

    voice "voice_3_15k.wav"
    k "當其他國家在排斥魔法師的時候，是哪個國家願意收留被迫害的魔法師的？"

    voice "voice_3_16k.wav"
    k "你們這些只顧自己利益的黑魔法師們，才沒有資格統治卡美洛！"

    voice "voice_3_17k.wav"
    k "我以梅林弟子阿凡隆的後人為名"

    voice "voice_3_18k.wav"
    k "要求將這些忘恩負義的叛徒驅逐出去！"

    hide evil
    hide kioma

    # show kioma serious at center with moveinright
    scene bg black
    scene cg kiomamagic
    play music "bgm_chaos.mp3" loop
    with Dissolve(2.0)
    $ renpy.pause(1.5, hard=True)
    
    voice "voice_3_19k.wav"
    k "Kærcelo Sæpaćika Kævø（混沌空間牢籠）"

    voice "voice_3_20k.wav"
    k "Mæmapa Ævalonja, jær pøtaći kivona pjæn!（先祖阿凡隆大師啊，請賜予我力量！）"

    voice "voice_3_21k.wav"
    k "（這樣的牢籠應該足夠包圍這些敵軍了吧？）"
    
    voice "voice_3_22k.wav"
    k "Sæpaćika, Kævønja!（空間，混亂起來吧！）"


    scene bg palace broken
    show kioma
    play sound "sound_speed.mp3"
    voice "voice_3_23k.wav"
    k "（成功了！成功了！敵軍開始困在牢籠裡面了）"
    
    hide kioma
    show evil shout
    ""
    hide evil 
    with dissolve
    play sound "sound_speed2.mp3"
    voice "voice_3_24t.wav"
    t "啊啊啊啊啊啊！！！！！"

    
    voice "voice_3_25k.wav"
    k "（敵軍逐漸被牢籠裡扭曲的空間撕碎……）"

    voice "voice_3_26k.wav"
    k "（這樣王國就有救了吧……）"

    show kioma surprised
    voice "voice_3_27k.wav"
    k "咦？怎麼地板歪歪的？難道空間出現破洞？"

    stop music
    voice "voice_3_28k.wav"
    k "等等……不要掉下去……"

    hide kioma
    with moveoutbottom

    voice "voice_3_29k.wav"
    k "啊！！！！！！"


    
    

    scene bg black
    

    "……"

    # 回想小時候 （故鄉）

    play music "bgm_memory.mp3" loop
    scene bg house

    voice "voice_4_1z.wav"
    "媽媽" "祈奧馬、凡泰爾，爸爸媽媽要去前線作戰，抵抗黑魔法師的入侵"

    voice "voice_4_2z.wav"
    "媽媽" "等下送你們去香爐山的阿姨那邊住，你們要乖，要對阿姨有禮貌喔！"

    scene bg black
    
    "……"

    # 回想小時候 （香爐山）

    scene bg hls
    voice "voice_4_3k.wav"
    k "這裡就是香爐山嗎？看來跟卡美洛很不一樣欸……"

    voice "voice_4_4k.wav"
    k "沿著這條街走，應該去到阿姨家吧？"

    voice "voice_4_5k.wav"
    k "希望爸媽都沒事吧……"

    scene bg black
    
    "……"


    # 回想 （魔法學院）

    scene bg school

    show kioma

    voice "voice_4_6k.wav"
    k "終於回到卡美洛了，我要在魔法學院好好修讀魔法！"

    voice "voice_4_7k.wav"
    k "話說凡泰爾已經回到老家跟爸爸學習戰術了，那邊還好嗎？"

    voice "voice_4_8k.wav"
    k "等下寫封信給他吧？"

    hide kioma

    scene bg black
    
    "……"

    # 回想 （畢業後）

    scene bg house2

    show vatar at left

    voice "voice_4_9v.wav"
    v "哥哥你看，皇宮正在招聘魔法師喔！"

    voice "voice_4_10v.wav"
    v "你要不要試試看？"

    show kioma surprised at right

    voice "voice_4_11k.wav"
    k "我沒有什麼自信可以進皇宮工作欸……"

    voice "voice_4_12v.wav"
    v "你可以的！看看我都已經找到宮廷衛隊的工作了"

    voice "voice_4_13k.wav"
    k "好吧？那幫我看看這份工作有什麼要求？"

    show vatar surprised

    voice "voice_4_14v.wav"
    v "需要維護和升級魔導裝置、幫宮廷用品附魔、抵抗魔物入侵，等等……需要通過劍術考試？"

    voice "voice_4_15k.wav"
    k "魔法師要近戰來幹什麼？皇宮是不是對魔法師有什麼誤解？糟了，我不會劍術……"

    voice "voice_4_16v.wav"
    v "我也不知道為什麼……不過劍術的部分我可以跟你一起練習？"

    voice "voice_4_17k.wav"
    k "好吧……就這樣吧……"

    hide vatar
    hide kioma


    scene bg black
    
    "……"


    # 降落本世界
    stop music
    scene bg hk1
    play sound "sound_street.mp3" loop
    show kioma surprised

    voice "voice_4_18k.wav"
    k "這裡是？"

    voice "voice_4_19k.wav"
    k "看地形好像是香爐山，但是感覺怪怪的？"

    voice "voice_4_20k.wav"
    k "怎麼會有這麼多高樓大廈，而且造型都很奇怪？"

    hide kioma
    with moveoutbottom

    scene bg black
    stop sound

    play sound "sound_fall.mp3"
    "轟！！！"

    k "……"

    k "……"

    voice "voice_5_1m.wav"
    mq "果然，就如預言一樣！"

    voice "voice_5_2m.wav"
    mq "一個從異世界來的魔法師會在這個時候被傳送過來這裡！"

    scene bg hk2

    show kioma dizzy at left
    show moses at right
    play music "bgm_confused.mp3" loop

    k "……"

    voice "voice_5_3m.wav" #滑鼠聲
    m "你終於醒了！你還好嗎？"

    show kioma surprised
    voice "voice_5_4k.wav"
    k "……這裡是哪裡？"

    voice "voice_5_5k.wav"
    k "剛才好像有什麼東西但是我記不起來……"

    voice "voice_5_6k.wav"
    k "只記得啊一聲就從上面摔下來了"

    voice "voice_5_7k.wav"
    k "……請問你是？"

    voice "voice_5_8m.wav"
    m "啊對忘了介紹自己，我叫做巫摩西，是香港魔法協會的會長，叫我摩西就可以了"

    voice "voice_5_9k.wav"
    k "香港？？？魔法？？？"

    voice "voice_5_10m.wav"
    m "你就是異世界來的的魔法師嗎？"

    voice "voice_5_11k.wav"
    k "異世界？？？魔法師？？？"

    voice "voice_5_12k.wav"
    k "你到底在說什麼？"

    show moses surprised

    voice "voice_5_13m.wav"
    m "（奇怪了，明明應該是這裡沒錯吧？）"

    voice "voice_5_14m.wav"
    m "（透過魔力共鳴知道這個人是魔法師，不會有錯吧？）"

    voice "voice_5_15m.wav"
    m "（難道，時空傳送對他的記憶有影響？）"

    show moses

    voice "voice_5_16m.wav"
    m "看來你是真的記不起來了……"

    show kioma serious
    voice "voice_5_17k.wav"
    k "請問是怎麼了嗎？"

    voice "voice_5_18m.wav"
    m "要說起來有點複雜，總之我們找一個地方慢慢說好嗎？"

    hide kioma
    hide moses

    # scene bg library

    ""
    voice "voice_5_19k.wav"
    k " （自此之後，我就在魔法協會學習魔法）"

    voice "voice_5_20k.wav"
    k "（也協助魔法協會進行不同的任務）"

    voice "voice_5_21k.wav"
    k "（至於卡美洛，應該就是對應這個世界的英國吧？）"

    voice "voice_5_22k.wav"
    k "（說不定在英國的任務也可以重拾自己的回憶）"

    voice "voice_5_23k.wav"
    k "（假以時日也可以傳送回原本的世界？）"

    "完"

    # 完

    return
