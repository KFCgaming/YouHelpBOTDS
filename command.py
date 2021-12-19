from typing import ContextManager
import discord
import random
from discord import voice_client
from discord import message
from discord.ext import commands
from discord.player import AudioPlayer, AudioSource
from discord.voice_client import VoiceClient
import asyncio
import time
import youtube_dl

bot = commands.Bot(command_prefix = ",")

POppit = ["https://www.ootb.de/wp-content/uploads/2021/02/Fidget-Pop-Toy_Header-Artikel-06.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841579695210506/amrambow.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841581095583774/amgirl.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841583335997470/716jYcW5ShL._AC_SL1500_-min-640x640.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841582962311178/1500-2021-R-1100x1100.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841585566842910/6064196561.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867841585013194762/U740d7e4353064187b3dacf383ba561293.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843523164504064/811Xr46IUS._AC_SL1500_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843525625905223/51g3Yqn4AiS._AC_SL1200_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843526968868864/71qTuzvZFoS._AC_SL1500_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843528785002536/61NeBingq5S._AC_SL1200_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843529414148106/41aJN7b8uL._AC_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843530995007528/61WFbzF7QYS._AC_SL1500_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843532220137513/617TtPNRN1S._AC_SL1200_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843533334773791/81E3OzqxuFS._AC_SL1500_.png",
"https://cdn.discordapp.com/attachments/862982107054473236/867843549948805160/41sh2d7YXSL._AC_.png"]

cat = ["https://www.comportementaliste-gironde.fr/wp-content/uploads/2019/12/chat-chartreux.jpg",
"https://images.unsplash.com/photo-1506160484494-d2b1d999debd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
"https://pixnio.com/free-images/2017/09/16/2017-09-16-08-04-17.jpg",
"https://upload.wikimedia.org/wikipedia/commons/4/4a/Yawning_cat_portrait_(8423278464).jpg",
"https://i.pinimg.com/736x/8c/ab/4e/8cab4e46f19b1c4ae0ed8ff6c5115e7d.jpg",
"https://yt3.ggpht.com/a/AATXAJz-iBcY8fpw9HE3ngNwiWATqoCSOcvq_6NGTx_U-w=s900-c-k-c0xffffffff-no-rj-mo",
"https://i.pinimg.com/736x/52/bc/39/52bc3928fd63daa22ebfb555f9ae07dd.jpg",
"https://th.bing.com/th/id/OIP.Khkah7dcUh0m09tqD219uwHaKg?pid=ImgDet&rs=1",
"https://www.islandecho.co.uk/wp-content/uploads/2016/11/Cats-Protection-November-2016-74.jpg",
"https://i.pinimg.com/originals/59/a8/a2/59a8a2d022912450f3d8c5998f2928c6.jpg"]

dogs = ["https://th.bing.com/th/id/OIP.Lo-zaAM0m1IbtQ162XYDTwHaLH?pid=ImgDet&rs=1",
"https://www.auris-en-oisans.fr/wp-content/uploads/wpetourisme/6828718-diaporama.jpg",
"https://th.bing.com/th/id/R.b92583e3a998df973454c7c8981eaae7?rik=N8At7kWIYBPSlQ&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.60ccd268ae71497d651de7498b6fdccd?rik=hsB0tY%2bmqpdZ1w&pid=ImgRaw&r=0",
"https://www.woopets.fr/assets/img/002/046/og-image/13-races-de-chiens-qui-en-grandissant-passent-de-chiots-a-colosses-sur-pattes.jpg",
"https://th.bing.com/th/id/OIP.3ylSnAOaA5B8rhGMz_ljjQHaFE?pid=ImgDet&rs=1",
"https://www.jardiner-malin.fr/wp-content/uploads/2020/11/Chien-categorie-2.jpg",
"https://caniprof.com/wp-content/uploads/2019/04/chien-boxer-2.jpg",
"https://www.la-spa.fr/sites/default/files/pages/principales/black_st_omer_chien_1_0_0_0_0_0.jpg",
"https://th.bing.com/th/id/OIP.maBh99j1ZVwAHIXXXvX0XAHaHa?pid=ImgDet&rs=1"]

fish = ["https://th.bing.com/th/id/R.5bb8411e488eaa4efe51bc04afe45f5d?rik=ZyzSC4daPqRZow&riu=http%3a%2f%2fimg.fotocommunity.com%2fpoisson-chirurgien-8038307f-39bc-4f84-964a-787c7185e0f4.jpg%3fheight%3d1080&ehk=DfC0JLbVjWe0h9UDu3DcLqv4oQwhsNzhlcMyVxF5Ct0%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.5d1c3db1b6d3b791e92d2c1fdb60d951?rik=amEtet2xqzBJ9g&pid=ImgRaw&r=0",
"https://i1.wp.com/escapadesphoto.fr/wp-content/uploads/2019/04/DSC_7538.jpg?w=1200&ssl=1",
"https://th.bing.com/th/id/OIP.GjGL1WOFAl-1US4KKZJC6gHaF7?pid=ImgDet&rs=10",
"https://media.cooperation.ch/images/2015/09/21/AUF_1046x570_1533588441620.jpg",
"https://www.visoflora.com/images/original/poisson-tropical-visoflora-24403.jpg",
"https://www.baobabsalon.fr/public/img/big/ornamentalfish29882421920jpg_5d10f9ba1fc48.jpg",
"https://th.bing.com/th/id/OIP.l5st2BVF4y2Q7E5QDpNiIwHaE7?pid=ImgDet&rs=1",
"https://th.bing.com/th/id/OIP.rm--2W_w-C6JnqeAMUZ1kAHaE8?pid=ImgDet&rs=1",
"https://th.bing.com/th/id/R.da20b47e602513b0bb4cb0d5d729a045?rik=eC2t4p%2bYPydDZg&pid=ImgRaw&r=0"]

Blague = ["Monsieur et Madame Golo ont un fils👨‍👩‍👦. Comment s'appelle-t-il ? Thierry car t'y es rigolo !! 🤣😂",
"Pourquoi les lapins🐰 ne jouent-ils qu'avec 39 cartes et non avec 52 📇? Parce qu'ils mangent les trèfles ! ☘",
"Que demande un douanier à un cochon🐷 qui passe la frontière ? Son passe-porc !!🤣🛃",
"Qu'y a t'il après un oeuf de Pâques 🍫 ? Un dix de Pâques !! 🐰",
"Quel est le comble pour une citrouille le jour d'Halloween ? C'est de trop se creuser la tête 🎃",
"Comment appelle-t-on l'ex d'un mouchoir 🤧? Un Kleen-ex 💔!!",
"Comment appelle-t-on un chat qui éteint les feux 🔥? Un chat peur pompier 😹!!",
"Pourquoi dit-on que les poissons travaillent illégalement ? Car ils n'ont pas de FISH de paie !! 🐟🐟",
"Comment appelle-t-on la femme du hamster ? C'est l'Amsterdam bien sûr !!💃",
"Toto à l'école <<Qu'est-ce qu'une voyelle ?>>, demande la professeure. Toto répond <<Je sas ! C'est la femme d'un voyou !>> 😝😝",
"Quel est le comble pour un poisson 🐠? C'est d'avoir l'eau à la bouche !! 🌊",
"Quel est le comble pour un coq🐓 ? C'est d'avoir la chair de poule!! 🐔",
"Quel est le gatêau préféré des arbres 🌳 ? Le mille-feuille 🍃 !! 🤣😂",
"Quel est le fruit que les poissons 🐟 détestent le plus ? La pêche 🍑 !!",
"Quelle est la ville la plus veille du monde 🏙? C'est Milan !! 😂",
"Où vont les biscottes pour danser 🍞 ? En biscothèque 🕺💃!!",
"Quel est le point commun entre un footballeur et un champion de natation ⚽🏊‍♂️ ? Ils aiment 'Mouiller le maillot' 🎽🎽!! ",
"Comment s'appelle un chat 🐈tombé dans un pot de peinture🖌 le jour de Noël🎅 ?¨Un chat pein de Noël 🎄🎄!! 🤣 ",
"Comment s'appelle une poule qui a peur de l'eau🌊 ? Une poulle mouillée !!🐔",
"Quel est le comble pour une pieuvre 🐙? C'est de se faire un sang d'encre 😰!!",
"Que dit une pierre à une autre pierre ⛰ ? <<La vie est dure>> !! 😂",
"Qu'est-ce qui est vert et qui se déplace sous l'eau ? Un chou-marin 🌊🥦 !!",
"Quel est le fruit préféré du canard 🦆 ? C'est le coing !!😂",
"Que fait l'Assistant Google pendant un match de foot 🏟 ? Il raconte des blagues à deux balles ⚽⚽ !! 😁",
"Pourquoi les marchands de savon font-ils fortune 🧼? Car leurs client les savent honnêtes !! 🛁",
"Comment s'appelle le cousin végétarien de Bruce Lee ? Broco Lee 🥦🥦 !! 😂",
"Quel est l'animal qui a le plus de dents ? La petite souris ! 🐭🐭",
"Quelle coupe de cheveux est à la mode le jour d'Halloween 🎃? La chayve Souris 🦇!!",
"Qu'est-ce qui va de ville en ville sans jamais bouger ? Une route🚗🛣 !",
"Pourquoi les livres n'ont-ils pas froid en hiver 📚? Car ils portent une couverture ❄!!"]

SavizVous = ["Le saviez-vous ? Le DogeCoin à été crée par Elon Musk en référence au meme du Shiba Inu 🐕.",
"Le saviez-vous ? Un BitCoin, en avril 2021 valaient maximum 52 000 Euros !!",
"Le saviez-vous ? Le FastFood le plus connue, Mcdonald's a fait 6 Milliard de dollard de bénéfice 🍔🍟!!",
"Le saviez-vous ? La ville avec le plus d'habitant au monde est Hong Kong avec 65 700 000 habitant en 2021 🏙🏙!!",
"Le saviez-vous ? Le jeu vidéo le plus vendu au monde est Minecraft avec 200 millions de copies ⚒ !!",
"Le saviez-vous ? Le jeu vidéo avec le plus de joueur et Fortnite avec 250 millions de joueurs 🔫!!",
"Le saviez-vous ? La vidéo la plus vue sur YouTube est Baby Shark avec 9 Milliard de vue en 2021 👶🦈 !!",
"Le saviez-vous ? Les consoles les plus vendu de l'histoire sont la PS2 avec 157 Millions d'exemplaires, La Nintendo DS avec 154 Millions d'exemplaires et la Nintendo Game Boy avec 118 d'exemplaires 🎮🕹!!",
"Le saviez-vous ? Le bot discord le plus utilisé au monde est MEE6 inclut 12 Millions de serveurs en 2021 🤖!!",
"Le saviez-vous ? Le plus petit pays du monde et le Vatican avec en superficie 0,44 kilomètre carré🌍🌎!!",
"Le saviez-vous ? "]



MEMES = ["https://memeguy.com/photos/images/cursed-image-358629.jpg",
"https://i.redd.it/khnb2v1f52871.jpg",
"https://i.redd.it/jev4peyw29871.jpg",
"https://i.imgflip.com/4ggvb0.jpg",
"https://th.bing.com/th/id/R.bf5159d0f199220bfc652bf746ffae09?rik=UXoT4splV66tSg&pid=ImgRaw",
"https://th.bing.com/th/id/R.65d3099e7f81d93136cc79bc11e2c2ab?rik=ctewo7m%2bTYJ%2bTg&pid=ImgRaw",
"https://th.bing.com/th/id/OIP.MCAIv_5ePc4RMTWcdiNU4gAAAA?pid=ImgDet&rs=1",
"https://img.memecdn.com/modern-problems-require-modern-solutions_o_3377699731001602.webp",
"https://media.tenor.com/images/7645a8d8641078195b89b1b7f096c7b2/tenor.gif",
"https://images3.memedroid.com/images/UPLOADED87/6098eba222302.jpeg",
"https://images7.memedroid.com/images/UPLOADED623/5ebcdb53797cc.jpeg",
"https://images7.memedroid.com/images/UPLOADED901/5e79af8ef2cb8.jpeg",
"https://images3.memedroid.com/images/UPLOADED328/5d15ae9c295f5.jpeg",
"https://images3.memedroid.com/images/UPLOADED398/5a829727e5793.jpeg",
"https://images3.memedroid.com/images/UPLOADED736/60e18ad3777f6.jpeg",
"https://images3.memedroid.com/images/UPLOADED896/60e0c19551d4a.jpeg",
"https://images3.memedroid.com/images/UPLOADED136/60e04ae24bb2d.jpeg",
"https://rvideos2.memedroid.com/videos/UPLOADED666/60e0574be48e0.mp4",
"https://images7.memedroid.com/images/UPLOADED845/60e03df30d7f1.jpeg",
"https://images3.memedroid.com/images/UPLOADED812/60e0135128d2f.jpeg",
"https://images3.memedroid.com/images/UPLOADED912/60df29cec10ef.jpeg",
"https://images3.memedroid.com/images/UPLOADED514/60df0746cb0f0.jpeg",
"https://images3.memedroid.com/images/UPLOADED162/60def77792e90.jpeg",
"https://images7.memedroid.com/images/UPLOADED975/60f93b95be3d8.jpeg",
"https://images7.memedroid.com/images/UPLOADED714/60f91b12bd105.jpeg",
"https://images3.memedroid.com/images/UPLOADED598/60f910687be88.jpeg",
"https://images3.memedroid.com/images/UPLOADED537/60f7e522cbb44.jpeg"]

daup = ["https://th.bing.com/th/id/R.c470578862b9c7aa6e70270fa917516e?rik=mhZBZ4M58%2bdhcw&riu=http%3a%2f%2fwww.bianoti.com%2fwp-content%2fuploads%2f2015%2f12%2fWallpapers-Dauphin6.jpg&ehk=Y1Zd1trL%2fo9C3FmTr7bsOhbNcP%2f9nSxWKKayDixbQiM%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.e36863483db6a4991152a486477ace11?rik=xdzcgklWrbPIxQ&riu=http%3a%2f%2fwww.animaw.com%2fwp-content%2fuploads%2f2017%2f08%2fdeux-grands-dauphins.jpg&ehk=hGwTfDnVC3FyiZx6BUTNKncR62dXPIDDb6O1PMlgIf0%3d&risl=&pid=ImgRaw&r=0",
"https://www.mer-ocean.com/wp-content/uploads/2018/12/dauphin-pixabay-1024x768.jpg",
"https://th.bing.com/th/id/R.cb04004a6a1f18462b346379d3a0ce57?rik=w0JHNwQ0qd4y7Q&riu=http%3a%2f%2fwww.bianoti.com%2fwp-content%2fuploads%2f2015%2f12%2fWallpapers-Dauphin7.jpg&ehk=sJbOCQ9iqYM0EioYJ3PJw8nukUj2VupLbd48J7bvXBI%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.8d7e891132681bdfe0899a3eacb45ebb?rik=fAWo9W5CtzthXw&riu=http%3a%2f%2fimages.4ever.eu%2fdata%2fdownload%2fanimaux%2fvie-aquatique%2fdauphin-sautant-190791.jpg&ehk=rGQ5KcmNeJ7BiYCpWbtTUSehuAPUTZ7X7pYnR2KayrE%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.9b2acfbc0d6869d67addb06178e4c348?rik=aZbmr9PwDW6pGQ&riu=http%3a%2f%2fwww.snut.fr%2fwp-content%2fuploads%2f2015%2f08%2fimage-de-dauphin-5.jpg&ehk=ff4vh5ZWTB1Bzk0hlSxFjj%2b%2fSjkobeB69AsQf%2fTVVW8%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.956caad8b0f6b1da04a904562a16a093?rik=%2bqMHzjf02NhtpA&riu=http%3a%2f%2fwww.gdegem.org%2fsites%2fgdegem.org%2ffiles%2fthumbnails%2fimage%2fsga_saint_cyprien_20140524_grand_dauphin_saut_20.jpg&ehk=Mk9sRx8qOa4oZ8vKLpRSkCYoYC5DuBisFpEqBEH3XOs%3d&risl=&pid=ImgRaw&r=0",
"https://animalaxy.fr/wp-content/uploads/2020/01/iStock-525733140.jpg",
"https://i.skyrock.net/4306/47574306/pics/2387783201_small_1.jpg",
"https://th.bing.com/th/id/R.b2979f8fdea40c854351b65ddf7d58fe?rik=cpRHILC%2f5DW8uA&riu=http%3a%2f%2fwww.ac-grenoble.fr%2fecoles%2fvienne2%2flocal%2fcache-vignettes%2fL468xH263%2frepasdauphins-16ffe.jpg&ehk=EJprgvpYdDwJTn38a%2fmD%2f9B0%2b1BPXeokis5%2fwra2ou8%3d&risl=&pid=ImgRaw&r=0"]

cerff = ["https://th.bing.com/th/id/R.e3295a5ddc704aaf255dfe2919ec6f93?rik=Y2bomSADN34Cgg&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/OIP.O-QP0S7zYF99QwSd8V2C2QHaE8?pid=ImgDet&rs=1",
"https://media.cooperation.ch/images/2017/04/17/1714Co_R2_Orizzonti_alamy_1046x570_1533607544998.jpg",
"https://www.zoologiste.com/images/xl/cerf-foret.jpg",
"https://th.bing.com/th/id/OIP.fFu14N8MQW2H0FmFs_bSygHaFP?pid=ImgDet&rs=1",
"https://th.bing.com/th/id/R.72f026ea786f08ed8e779139f9b013fa?rik=GK3A5GwLBdIguA&riu=http%3a%2f%2fwww.cantalpassion.com%2fimages%2fterritoire%2fla-nature%2ffaune%2fCerf%2fcerf.jpg&ehk=KEvpNgZfmYCx5XSck01EY9OxF3vial3lky%2bTrE3UopI%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/OIP.ZEiTuWPXXeJTULGvxbm7fwHaLI?pid=ImgDet&rs=1",
"https://th.bing.com/th/id/R.7d71ac8d6d7b0a37ff82aa43c3d6de91?rik=kNUE0x8LCkotGQ&pid=ImgRaw&r=0",
"https://www.ecobalade.fr/sites/default/files/PHOTO_taxon/cervus_elaphus_-_peter_trimming.jpg",
"https://aventure-france.fr/wp-content/uploads/2020/04/brame-du-cerf-aventure-france-scaled.jpeg"]

CAsiNO = ["🍒🍓🍓",
"🍒🍓🍒",
"🍓🍒🍓",
"🍓🍓🍒",
"🍒🍒🍒",
"🍒🍓**7**",
"🍓🍒**7**",
"**7**🍓🍒",
"**7**🍒🍓",
"🍓**7**🍒",
"🍒**7**🍓",
"🍓🍓🍓",
"**77**🍓",
"**77**🍒",
"🍒**77**",
"🍓**77**",
"**777**"]
WtF = ["https://pointerpointer.com/",
"http://scroll-o-meter.club/",
"https://pixelsfighting.com/",
"http://chihuahuaspin.com/",
"http://papertoilet.com/",
"https://zoomquilt.org/",
"https://longdogechallenge.com/",
"⚠Epileptic Alert⚠||http://www.staggeringbeauty.com/||",
"http://www.staggeringbeauty.com/",
"http://endless.horse/",
"http://www.koalastothemax.com/",
"https://neave.tv",
"https://neal.fun/life-stats/",
"http://buzzybuzz.biz/",
"https://www.bouncingdvdlogo.com/",
"https://remoji.com/",
"https://thatsthefinger.com/",
"http://eelslap.com/",
"http://www.republiquedesmangues.fr/",
"http://sadforjapan.com/",
"https://cat-bounce.com/",
"http://www.ouaismaisbon.ch/"]

Fortnitecy = ["https://www.youtube.com/channel/UCKgXoalnzLs1VDbkT8opX6Q",
"https://www.youtube.com/channel/UC3FLNDzxVDGDGM85sMveJqg",
"https://www.youtube.com/c/ZRKGlitcher",
"https://www.youtube.com/user/MineJeanfils",
"https://www.youtube.com/c/SWIIZEN/videos",
"https://www.youtube.com/channel/UC7ijkNcwtGN9qohTn70OsMw",
"https://www.youtube.com/c/NexTazTK/videos",
"https://www.youtube.com/c/SPIDERGAMESYT",
"https://www.youtube.com/channel/UCDf1I775_G_JkqpjRQ6e-eg",
"https://www.youtube.com/user/StudioKoco"]

TIcy = ["https://www.youtube.com/channel/UC7fOs0P_rIkOOwcpAGToTjw",
"https://www.youtube.com/channel/UClC9Ci31vpWYakB2X9x5hSg",
"https://www.youtube.com/channel/UCZTFgxH04J2j-rmtb1aZ2rQ",
"https://www.youtube.com/channel/UCHNdRr2zPankleA17mLiDKw/featured",
"https://www.youtube.com/channel/UC20yy4loz_kfli5d7yd9VTQ",
"https://www.youtube.com/channel/UCYoOVCb4C2Up_J6dxKF-Pkw",
"https://www.youtube.com/channel/UCClSxAbpsTDrsO6lt4WGKrA",
"https://www.youtube.com/channel/UCxuz1ASgsVgusnvXQoWiLyw",
"https://www.youtube.com/user/cenahiphop50",
"https://www.youtube.com/channel/UC9gX37NkBNR2Ygg6ZMfuJEg"]

MCcy = ["https://www.youtube.com/user/MrAntoine56000",
"https://www.youtube.com/c/FuzeIII",
"https://www.youtube.com/c/MulticortT",
"https://www.youtube.com/user/Siphano13",
"https://www.youtube.com/user/Frigiel",
"https://www.youtube.com/c/Ninjaxx",
"https://www.youtube.com/channel/UCGogCYmJUnrGw65rgYbxsgg",
"https://www.youtube.com/channel/UCxnV0b1efAuVgzvLdjzrTsg",
"https://www.youtube.com/channel/UCXoHgg84q9ysd83EYnVyxYw",
"https://www.youtube.com/user/magicknup",]

Gcy = ["https://www.youtube.com/c/TheFuriousJumper",
"https://www.youtube.com/channel/UCY-_QmcW09PHAImgVnKxU2g",
"https://www.youtube.com/user/CouilleBleuGaming",
"https://www.youtube.com/channel/UCGjE4SbUyAKj5d_baD6Pxlg/videos",
"https://www.youtube.com/user/RedKill24",
"https://www.youtube.com/channel/UCIPPMRA040LQr5QPyJEbmXA"]

scy = ["https://www.youtube.com/user/NormanFaitDesVideos",
"https://www.youtube.com/c/cyprien",
"https://www.youtube.com/user/lemondealenversvideo",
"https://www.youtube.com/c/ParodieBro",
"https://www.youtube.com/user/FestivalDuRireTV",
"https://www.youtube.com/c/filleludique",]

@bot.command()
async def salut(ctx):
    await ctx.send("Salut cher utilisateur :) ! Comment vas-tu ? Moi plutôt cool !!!!☺☺")

@bot.command()
async def aide(ctx):
    embed=discord.Embed(title="🌍๖̶ζ͜͡YouHelp🌎", description="Vous avez effectué la commande ``,aide``", color=0x00fbff)
    embed.add_field(name="Montre toutes les commandes du bot | celle-ci 😉", value="``,aide``", inline=False)
    embed.add_field(name="Vous salut 🤗", value="``,salut``", inline=True)
    embed.add_field(name="Vous donne une commande dans lequel il y a une recette 🍪", value="``,recette``", inline=True)
    embed.add_field(name="Mets le tag du créateur du bot et la date du commencement du bot🤖", value="``,creation``", inline=True)
    embed.add_field(name="Vous raconte une blague 🤣", value="``,blague``", inline=True)
    embed.add_field(name="Saviez-vous | Donne quelques information pertinente 😲", value="``,sv``", inline=True)
    embed.add_field(name="Vous met une petit meme qui fait plaisir 😉", value="``,meme``", inline=True)
    embed.add_field(name="Vous met un popit :)   🔴🟠🟡🟢🔵", value="``,popit``", inline=True)
    embed.add_field(name="Référence à un pote 🐔🐔🍣", value="``,cotcot``", inline=True)
    embed.add_field(name="Offre un cadeau à ton amis le bot🎁🎁🎁🎁 ", value="``,cadeau``", inline=True)
    embed.add_field(name="Logs des versions ", value="``,logs``", inline=True)
    embed.add_field(name="Catégories des commandes lier aux animaux 🐠🐱🐶 ", value="``,ctanimaux``", inline=True)
    embed.add_field(name="Jeux du Casino 🍒🍓**7**", value="``,casino``", inline=True)
    embed.add_field(name="Cherche des site WTF pour vous amusez😂😁", value="``,wtf``", inline=True)
    embed.add_field(name="Cherche des chaine YouTube celon votre demande", value="``,cy``", inline=True)
    embed.add_field(name="Vous donnes accès au lien d'invitation", value="``,invite``", inline=True)
    embed.set_footer(text="1.1.0")
    await ctx.send(embed=embed)

@bot.command()
async def creation(ctx):
    await ctx.send("Mon créateur est fou 🤯 !! Il a commencer à me crée le 4 Juillet à Minuit et si tu ne sais pas comment il s'appelle, sont nom est KFCgamingFR#4001.")

@bot.command()
async def recette(ctx):
    await ctx.send("Je ne suis pas un cuisiner mais j'en ai une qui devrais te plaire ! Si tu es gourmand fais /cookiesrecette")

@bot.command()
async def cookiesrecette(ctx):
    await ctx.send("Pour 6 Cookies 🍪, Il te faut 1 oeuf🥚, 85 grammes de beurre doux🧈, 100 grammes de pépite de chocolat, 1 cuillière à café de levure chimique, 85 grammes de sucre🍭, 150 grammes de farine, 1 sachet de sucre vanillé 🍭, 1 demi cuillère à café de sel 🧂. 1️⃣ Laissez ramollir le beurre à température ambiante. Dans un saladier, malaxez-le avec le sucre. 2️⃣ Ajoutez l'oeuf et éventuellement le sucre vanillé. 3️⃣Versez progressivement la farine, la levure chimique, le sel et les pépites de chocolat. Mélangez bien. 4️⃣ Beurrez une plaque allant au four ou recouvrez-la d'une plaque de silicone. À l'aide de deux cuillères à soupe ou simplement avec les mains, formez des noix de pâte en les espaçant car elles s'étaleront à la cuisson. 5️⃣Faites cuire 8 à 10 minutes à 180°c soit thermostat 6. Il faut les sortir dès que les contours commencent à brunir. Et enfin dégustez-les | Source cuisine.journaldesfemmes.fr")

@bot.command()
async def blague(ctx):
    await ctx.send(random.choice(Blague))

@bot.command()
async def sv(ctx):
    await ctx.send(random.choice(SavizVous))

@bot.command()
async def meme(ctx):
    await ctx.send(random.choice(MEMES))
    
@bot.command()
async def popit(ctx):
    await ctx.send(random.choice(POppit))

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="Lien d'invitation", description="Inviter le bot discord sur votre serveur !!", color=0xff7b00)
    embed.set_author(name="Invitation", icon_url="https://webstockreview.net/images/discord-icon-png.png")
    embed.add_field(name="Lien d'invitation", value="https://bit.ly/2XKipsK", inline=True)
    embed.set_footer(text="⚠ A savoir ⚠ : Le bot discord n'est pas en marche 24h/24 et non 7j/7. Pour l'instant, à quelques moment, le bot sera en marche. Si important, demander à KFCgamingFR#4001 d'allumer le bot pour un moment mais pas disponible tous le temps.")
    await ctx.send(embed=embed)

@bot.command()
async def logs(ctx):
    embed=discord.Embed(title="🌍๖̶ζ͜͡YouHelp🌎", description="Vous avez effectué la commande ``,logs``", color=0x00fbff)
    embed.add_field(name="Ajout de ,salut", value="``1.0.0``", inline=False)
    embed.add_field(name="Ajout de ,creation ,recette", value="``1.0.1``", inline=True)
    embed.add_field(name="Ajout de ,cookiesrecette", value="``1.0.2``", inline=True)
    embed.add_field(name="Ajout de ,blague avec 30 blagues", value="``1.0.3``", inline=True)
    embed.add_field(name="Ajout de ,sv avec 10 blagues ,meme avec 20 memes ", value="``1.0.4``", inline=True)
    embed.add_field(name="Ajout de ,popit", value="``1.0.5``", inline=True)
    embed.add_field(name="Ajout de ,cotcot ,cadeau ,logs et 5 memes", value="``1.0.6``", inline=True)
    embed.add_field(name="Ajout de ,ctanimaux ,chat ,chien ,poisson et de 30 photos de chien, de chat et de poisson", value="``1.0.7``", inline=True)
    embed.add_field(name="Ajout de ,casino ,cerf ,dauphin", value="``1.0.8``", inline=True)
    embed.add_field(name="Ajout de ,wtf", value="``1.0.9``", inline=True)
    embed.add_field(name="Ajout de ,invite ,cy ,cyf ,cyti ,cym ,cyg ,cyc , cys et de 43 Chaine YouTube", value="**current**``1.1.0``", inline=True)
    embed.set_footer(text="Logs")
    await ctx.send(embed=embed)

@bot.command()
async def cotcot(ctx):
    await ctx.send("https://pngimage.net/wp-content/uploads/2018/06/nems-png-2.png")

@bot.command()
async def ctanimaux(ctx):
    embed=discord.Embed(title="😺Catégorie Animaux🦌", description="La commande ``,ctanimaux`` vous permet de voir les commandes lier au animaux.", color=0xffd500)
    embed.set_author(name="🌍๖̶ζ͜͡YouHelp🌎", icon_url="https://cdn.discordapp.com/avatars/860985238096052235/1a671a3877b34f7ac7fdf7083758dd25.png?size=128")
    embed.set_thumbnail(url="https://th.bing.com/th/id/R.c3f30eae941659a5db3e38e2e2e8b607?rik=IUVtr%2fAMoE%2f6Ow&pid=ImgRaw&r=0")
    embed.add_field(name="🐈Chat🐈", value=",chat", inline=True)
    embed.add_field(name="🐕Chien🐕", value=",chien", inline=True)
    embed.add_field(name="🐠Poisson🐠", value=",poisson", inline=True)
    embed.add_field(name="🐬Dauphin🐬", value=",dauphin", inline=True)
    embed.add_field(name="🦌Cerf🦌", value=",cerf", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def chat(ctx):
    embed=discord.Embed(title="🐱Chat🐱", description="Le chat domestique (Felis silvetris catus) est un mammifère carnivore qui appartient à la famille des félidés. Il a été domestiqué par l'homme il y plusieurs milliers d'années pour protéger les cultures des souris et autres rongeurs. Par la suite, le chat domestique est aussi devenu un simple animal de compagnie.", color=0x00ffcc)
    embed.set_image(url=random.choice(cat))
    await ctx.send(embed=embed)

@bot.command()
async def chien(ctx):
    embed=discord.Embed(title="🐶Chien🐶", description="Le Chien est la sous-espèce domestique de Canis lupus, un mammifère de la famille des Canidés, laquelle comprend également le dingo, chien domestique retourné à l'état sauvage.", color=0x00ffcc)
    embed.set_image(url=random.choice(dogs))
    await ctx.send(embed=embed)

@bot.command()
async def dauphin(ctx):
    embed=discord.Embed(title="🐬Dauphin🐬", description="Dauphin est un nom vernaculaire ambigu désignant en français certains mammifères marins et fluviaux appartenant à l'ordre des Cétacés.", color=0x00ffcc)
    embed.set_image(url=random.choice(daup))
    await ctx.send(embed=embed)

@bot.command()
async def cerf(ctx):
    embed=discord.Embed(title="🦌Cerf🦌", description="Le cerf élaphe est un grand cervidé des forêts tempérées d'Europe, d'Afrique du Nord et d'Asie occidentale et centrale. Son nom est un pléonasme, car « élaphe » signifie déjà « cerf » en grec.", color=0x00ffcc)
    embed.set_image(url=random.choice(cerff))
    await ctx.send(embed=embed)

@bot.command()
async def poisson(ctx):
    embed=discord.Embed(title="🐠Poisson🐟", description="Les poissons sont des animaux vertébrés aquatiques à branchies, pourvus de nageoires et dont le corps est le plus souvent couvert d'écailles. On les trouve abondamment aussi bien dans les eaux douces que dans les mers : on trouve des espèces depuis les sources de montagnes (omble de fontaine, goujon) jusqu'au plus profond des océans (grandgousier, poisson-ogre). Leur répartition est toutefois très inégale : 50 % des poissons vivraient dans 17 % de la surface des océans (qui sont souvent aussi les plus surexploités).", color=0x00ffcc)
    embed.set_image(url=random.choice(fish))
    await ctx.send(embed=embed)

@bot.command()
async def cadeau(ctx):
    await ctx.send(" Un cadeau ! Pour moi !!! Je te remercie infiniment !! Je peux ouvrir le cadeau ? Aller je l'ouvre. Oh !!! Trop sympa, un disque dur SSD de 500Go et une ram de 8 gigabytes !!! Trop génial je vais me l'implenter !! Je me sens plus puissant merci beaucoup.")
    
@bot.command()
async def casino(ctx):
    await ctx.send("🎰Le rouleau tourne ...🎰")
    await ctx.send(random.choice(CAsiNO))

@bot.command()
async def wtf(ctx):
    await ctx.send("Recherche de site WTF... 🌐")
    await ctx.send(random.choice(WtF))

@bot.command()
async def cy(ctx):
    embed=discord.Embed(title=" 🎥Chaine Youtube🎥", description="Voici les catégories de chaine youtube", color=0xff0000)
    embed.set_thumbnail(url="https://1.bp.blogspot.com/-zPnHKpUdViY/X0OzA6pRnXI/AAAAAAAAAQM/LZQbELfm9BQK6nIkju-1t4KqMVxcPkRdQCLcBGAsYHQ/s1912/logo%2Byt%2Byogiancreative1.png")
    embed.add_field(name="Chaine Fortnite", value=",cyf", inline=True)
    embed.add_field(name="Chaine Repost Tiktok et Instagram", value=",cyti", inline=True)
    embed.add_field(name="Chaine Minecraft", value=",cym", inline=True)
    embed.add_field(name="Chaine Gaming (Tous jeux)", value=",cyg", inline=True)
    embed.add_field(name="Chaine de KFCgamingFR", value=",cyc", inline=True)
    embed.add_field(name="Chaine de Sketch", value=",cys", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def cyf(ctx):
    await ctx.send("Recherche de Chaine YouTube Fortnite... 🌐")
    await ctx.send(random.choice(Fortnitecy))

@bot.command()
async def cyti(ctx):
    await ctx.send("Recherche de Chaine YouTube de Repost de Tiktok et d'instagram... 🌐")
    await ctx.send(random.choice(TIcy))

@bot.command()
async def cym(ctx):
    await ctx.send("Recherche de Chaine YouTube Minecraft... 🌐")
    await ctx.send(random.choice(MCcy))

@bot.command()
async def cyg(ctx):
    await ctx.send("Recherche de Chaine YouTube Gaming... 🌐")
    await ctx.send(random.choice(Gcy))

@bot.command()
async def cyc(ctx):
    await ctx.send("https://www.youtube.com/channel/UC2BS8WfI9nFKZciHwomz7eg")

@bot.command()
async def cys(ctx):
    await ctx.send("Recherche de Chaine YouTube de Sketch... 🌐")
    await ctx.send(random.choice(scy))

bot.run("ODYwOTg1MjM4MDk2MDUyMjM1.YODM_Q.fcEY5MnT9XhHUfSM2KUFxzQEbdo")