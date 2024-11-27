import json

options_json = json.load(open("./options.json"))

options_html = """<html>
	<head>
		<title>Smash - Melee - Marth</title>
		<link rel="stylesheet" href="./css/dark-mode.css">
		<link rel="stylesheet" href="./css/main.css">
	</head>
	<body class="fd_bg">
		<div id="bar">
			<center style="width: 100%;">
				<a class="bar-a" href="./index.html" style="float: left;">
					<svg id="marth_sword_img" height="125" width="125" viewBox="0 0 256 256">
						<path id="marth_sword_img_path" style="fill:#FFFFFF; stroke:#FFFFFF" d="m 210.35584,45.644161 c -5.02604,-5e-6 -11.99452,-1.263729 -17.63347,4.375223 -5.63895,5.638953 -5.19282,12.308078 -5.19282,12.308078 l -9.8111,9.811106 c -3.37848,-1.295991 -7.59342,-1.105514 -11.86614,0.419845 l -11.07064,-16.99266 -22.56113,-0.817592 -10.98225,15.62264 5.01604,21.854019 9.34707,-18.009126 6.65122,0.375651 6.38606,12.484854 -4.44152,12.750019 -82.996654,68.633552 -15.556349,41.89607 41.896077,-15.55635 68.633556,-82.99665 12.75001,-4.44152 12.48486,6.38606 0.37565,6.65122 -18.00913,9.34707 21.85402,5.01604 15.62264,-10.98225 -0.81759,-22.56113 -16.99266,-11.070636 c 1.52536,-4.272724 1.71584,-8.487656 0.41985,-11.866136 l 9.8111,-9.811106 c 0,0 6.66913,0.446137 12.30808,-5.192816 5.63895,-5.638952 4.37522,-12.607443 4.37522,-17.633475 z M 172.7908,83.209209 c 2.30924,2.309248 0.90763,7.445063 -3.11569,11.468388 -4.02333,4.023325 -9.15914,5.424933 -11.46839,3.115689 -2.30925,-2.309248 -0.90764,-7.445063 3.11569,-11.468388 4.02332,-4.023324 9.15914,-5.424937 11.46839,-3.115689 z"></path>
					</svg>
				</a>
				<a class="bar-a" href="./guides.html"><button class="bar-button">Guides & Tech</button></a>
				<a class="bar-a" href="./framedata.html"><button class="bar-button">Framedata</button></a>
				<a class="bar-a" href="./matchups.html"><button class="bar-button">MatchUps</button></a>
				<a class="bar-a" href="./stages.html"><button class="bar-button">Stages</button></a>
				<a class="bar-a" href="./options.html"><button class="bar-button">options</button></a>
			</center>
		</div>
		<br>
		<div id="main-content">
			<pre style="tab-size: 4;">
							+-----------+-----------+-----------+-----------+-----------+
				Grounded	|	<a href="#jab">Jab</a>		|	<a href="#ftilt">F-Tilt</a>	|	<a href="#dtilt">D-Tilt</a>	|	<a href="#utilt">U-Tilt</a>	|	<a href="#grab">Grab</a>	|
				Aerials		| 	<a href="#nair">N-Air</a>	|	<a href="#fair">F-Air</a>	|	<a href="#dair">D-Air</a>	|	<a href="#uair">U-Air</a>	|	<a href="#bair">B-Air</a>	|
				Specials	|	<a href="#nb">N-B</a>		|	<a href="#sideb">Side-B</a>	|	<a href="#upb">Up-B</a>	|	<a href="#downb">Down-B</a>	|			|
				Smashes		| 			|	<a href="#fsmash">F-Smash</a>	|	<a href="#dsmash">D-Smash</a>	|	<a href="#usmash">U-Smash</a>	|<a href="#da">Dash Attack</a>|
				Movement	| <a href="#dd">DashDance</a>	|	<a href="#wd">WD</a>		|	<a href="#walk">Walk</a>	| 			|			|
				Defensive	| <a href="#ad">Air-Dodge</a>	|	<a href="#cc">CC</a>		|	<a href="#asdi">ASDI</a>	| <a href="#tech">AMSH tech</a> |	<a href="#sheild">Shield</a>	|
							+-----------+-----------+-----------+-----------+-----------+<center><a href="#uses">By Uses</a></pre></center>
                
                <div id="uses" class="tab-content">
                    <center><h1>Uses</h1></center>
                    %USES%
                </div>
			
			%CONTENT%
		</div>
	</body>
</html>"""

option_html = """			<div id="%ID%" class="tab-content">
				<center><h1>%NAME%</h1></center>
                <center><span>Combo: %COMBO%</span>\t<span>Kill: %KILL%</span>\t<span>Space: %SPACE%</span>\t<span>Risk: %RISK%</span></center>
				%CAT%
			</div>"""

cat_html = """				<details open>
					<summary style="display: inline;"><h2>%NAME%</h2></summary>
					<div class="indent-tab">
						%CONTENT%
					</div>
				</details>"""

def make_stars(n_stars, revs_colors=False):
    fill_star = "★"
    star = "☆"
    colors = {
        0: "#000099",
        1: "#990000",
        2: "red",
        3: "grey",
        4: "green",
        5: "gold",
    }
    
    return f"<span style='color: {colors[5 - n_stars if revs_colors else n_stars]}'>{(fill_star*n_stars) + (star*(5 - n_stars))}</span>"

option_content = ""
use_mapping = {}

for option_id, options in options_json.items():
    reward = options.pop("Reward")
    name = options.pop("Name")
    
    categories = ""
    for option in options:
        uses = []
        for use in options[option]:
            uses.append(f"<span>{use}</span>")
            if use not in use_mapping:
                use_mapping[use] = []
            use_mapping[use].append(f"<a href=\"#{option_id}\">{option}</a>")
        
        categories += "\n\n" + ("\n".join([
            cat_html
            .replace("%NAME%", option)
            .replace("%CONTENT%", ",\t".join(uses))
        ]))
    
    option_content += "\n\n\n\n" + (
        option_html
        .replace("%ID%", option_id)
        .replace("%NAME%", name)
        .replace("%COMBO%", make_stars(reward["Combo"]))
        .replace("%KILL%", make_stars(reward["Kill"]))
        .replace("%SPACE%", make_stars(reward["Space"]))
        .replace("%RISK%", make_stars(reward["Risk"], True))
        .replace("%CAT%", categories)
    )

uses_content = ""

for use in use_mapping:
    uses_content += "\n\n" + (
        cat_html
        .replace("%NAME%", use)
        .replace("%CONTENT%", ",\t".join(use_mapping[use]))
    )

file_content = (
    options_html
    .replace("%CONTENT%", option_content)
    .replace("%USES%", uses_content)
)


with open("options.html", "w", encoding="UTF-8") as fp:
    fp.write(file_content)


"""
Dtilt:
This attack is absolutely fantastic. It comes out on frame 7, it’s interruptable from frame 20 (out of 49 frames total), and it is one of Marth’s moves that does not have the problem of being a swinging, arcing hitbox, allowing it to be used like more of a persistent hitbox in one place, and that place happens to be in front of him, on the ground, which is an AMAZING place to have a fast, long-range, disjointed hitbox.

I believe this is Marth’s most important asset in neutral. It’s because of this move that Marth has such great ground control, and his ground control is largely what makes him a great character in the first place.

Dtilt is OP. However, one thing I must emphasize is that it’s only good if you use it intelligently!  It’s fairly punishable if you let the opponent jump over you or if you let them trade with your dtilt. Dtilt is very unlike other OP moves for this reason. It’s not a good move because it works pretty safely in a billion situations (e.g. Fox nair) and it’s not a good move because it converts into big damage (e.g. Peach dsmash) on-shield and/or on-hit. Dtilt is a good move because it opens so many doors for Marth, but it’s the responsibility of the player to follow up on them.  For example, if your opponent has resorted to jumping at you or trying to force a trade against you, then that gives you a lot of leverage to do… anything else. The rest of Marth’s kit is perfectly suited for evasion and anti-air, giving him plenty of tools to follow up on the threat of dtilt. I’d even go so far as to say that this move is what completes Marth as a character–what enables all of Marth’s other options to actually work.

In addition to its strength in zoning, dtilt is also a very good edgeguarding tool. It’s much faster than his fsmash, making it easier to land and easier to follow-up afterwards, and its on-hit trajectory is pretty good for edgeguarding.

A small little gimmick I have with dtilt is to immediately go in for a grab after hitting one. A lot of people will go defensive for a split second (shield, CC, or sometimes they’ll just get thrown off-guard) after you use your dtilt to put them in time-out or they’ll try to close in on you immediately to try getting an advantage from your dtilt’s end-lag, allowing you to just go for a grab. Don’t rely on this 100% obviously, but it’s very nifty.

Fair:
This is a great move. It’s his best and most versatile aerial, and it’s one of his best moves period.

As with most of Marth’s attacks, this is a fantastic zoning move. It’s amazing for aerial zoning AND it’s decent for ground zoning because it is a great anti-air that also hits well in front of him (counterexample: uair is also an amazing anti-air, but it does not cover his front very well).

Fair is a good move for edgeguarding, especially off-stage edgeguards simply because it’s his fastest aerial overall, hits in front of him, has good range allowing it to beat a lot of recoveries, and you can follow up after it fairly well due to its speed and trajectory.

This attack is also extremely useful for comboing (surprise, surprise). It’s vital to be able to manage your tippers vs non-tippers because both of these hitboxes will combo very differently. I feel like tipper fair is better most of the time (not all the time, obviously) because it hits the opponent upwards and stuns for a longer time, granting you the positional advantage, even if it doesn’t directly combo, whereas non-tipper fair is closer to horizontal, making it so that your opponent can DI into the ground or just DI in ways that make it a lot more difficult for you to follow up. Because your opponent can DI into the ground to make comboing off non-tipper fair more difficult, I believe non-tipper fair is much stronger high up than it is near the ground. All-in-all, non-tipper fairs are still essential for your combo game because of a different trajectory and because they are weaker than tipper fairs.

Fair is something to keep in mind when you are playing an extended anti-air game (i.e. whenever you launch someone in the air and try to repeatedly abuse and re-establish positional advantage). A lot of people rely exclusively on Marth’s up moves for these anti-air situations (uair, utilt), but don’t sleep on fair. Its tipper is very useful for popping them back up in the air; it hits in front of him better than uair/utilt, making it a better choice at some angles; and its non-tipper can swat them offstage and set up edgeguard situations.

When using your aerials (especially fair), it is important to distinguish between when you want to do a falling aerial or a rising aerial. Both have their applications.

A problem that a lot of Marths have with fair (and his aerials in general) IMO is being too aggressive or pushy with it, or being too spammy with it just because they think they can.

For example, a lot of Marth players will throw out fairs for no reason, thinking that it’s okay as long as they don’t get hit for it, ignoring the fact that they’re being wasteful in a situation where they should be establishing ground control or should be keeping a lot of options available to them.

A lot of Marth players will also improperly use their fair vs shield, just because it can be safe, given frames/range. Honestly, whenever you’re in the air vs someone’s shield, I personally think it’s better to not throw out an attack and just remain patient and uncommitted more than half the time. However, swinging your sword is situationally useful for some tricks or to deter some of their out of shield options. A classic Marth trick is Ken’s patented close fair -> dash behind the opponent. It IS safe against frame-perfect shieldgrabs if done correctly, and it’s probably safe vs most people’s shields, but just because it’s safe doesn’t mean it is a good choice. Swinging your sword is a commitment, and it’s up to you to decide if that commitment is worth it.

Something to keep in mind about the fair is that it swings in a top -> down arc. In other words, even though it comes out on frame 4, his lower front side is EXTREMELY vulnerable until it reaches down that low.

Nair:
This is an interesting move. It’s pretty good, but it’s very overrated by a lot of players because it loosely accomplishes some of the same things that other characters’ aerials do. For example, it doesn’t have a sweetspot (Strong Bad told me this. Apparently, there are different hitboxes with different sound effects, but all of the nair (second)-hitboxes have the same knockback and trajectory), meaning you don’t need to worry as much about your tipper. Secondly, it has stronger knockback than his fair, which makes it convert better than his fair, along with making it better in some cases where fair is too weak. Third, it is not an swinging arc, so it fits with how people like to use other aerials, like Fox’s nair. However, this third point is very iffy, because the first hit is so weak and so short.  Fourth, it has a very easy auto-cancel, which fits with Melee players’ obsession with low landing lag.

Even though these strengths are nice, there’s a problem: whenever you overuse Marth’s nair because of these strengths, you are playing him in a way that does not emphasize his strengths and weaknesses. A lot of people overrate nair because they only look at the positives.

For a lot of players, overuse of nair will distract from Marth’s primary goals, like ground control, playing for positional advantage, and staying at a safe distance. Having an auto-cancel on nair does not make up for the fact that Marth is a bad character at very close range and has no fast and reliable followups on the autocancel, like shine, dsmash (do you really need to ask whose dsmash I’m talking about?), and a lot of character’s jabs. Another weakness of nair is the fact that it has a very narrow zone of control BECAUSE it’s not a swinging arc, which can let people go over hit and bump your head or even go under it and hit your feet (because the first hit is so mediocre).

In neutral, nair is primarily another zoning tool. Whenever you set up nair on your own terms, you can maximize its strength and minimize its weaknesses, just like fair. Try it out, find out when it works, and find out why!

Nair has some other situational uses outside of the punish game. For example, it’s pretty good at shield poking and catching people out of shield. Whenever your opponent is sitting on the edge of a platform and waiting for you to push them off so they can do a bair, nair is good because the first hit can push them off the platform and set them up for the second hit.

In the punish game, nair is a pretty good combo move and a decent finisher. Against Fox and Falco at high percentages, uthrow -> nair can work fairly well in terms of hitting them offstage and setting up for a kill.

Fsmash:
The fsmash… yet another awesome move. It’s a great combo finisher. It’s a great edgeguard move. It’s a viable move in neutral if you can get the right read, and if you land it, BIG opportunities arise. Everyone is scared of Marth’s fsmash, and because of this alone, you get to threaten and bank off their fear, whether you actually use the attack or not. It’s a fairly straightforward move aside from that. An understated fact about fsmash is that its range is fairly deceptive because the upper-middle part of it actually reaches further than the bottom part of it.

Fsmash is great to land (duh) because it knocks the opponent over starting from a very low percent, and it has a good chance of knocking the opponent offstage for an edgeguard.

Although this is a great move, a lot of beginner Marths overuse it and rely on it as a crutch. If you find this is the case, try looking for other options. Don’t limit your search to just attacks, but also think about all the different movements and positions you can use, as well.

Uthrow:
This is one of your most important throws. This throw puts the opponent in the air above you (or on a platform above you, which is great for you, as well), immediately giving you a good chance to try and do some damage to them.

Something very important to consider when thinking about throw follow-ups is the weight of the opponent (THERE IS A VERY BIG DIFFERENCE BETWEEN WEIGHT AND FALL SPEED. PEACH AND SAMUS ARE HEAVY CHARACTERS, FOX AND FALCO ARE LIGHT CHARACTERS). Throws are slower whenever your opponent is heavier (and therefore, faster when they are lighter). The additional time you spend in the throw animation wastes frames of hitstun from the throw. In other words, you have less frame advantage on throws the heavier your opponent is.

From this, it makes sense that you’re more likely to land true combos off uthrow against light characters because you have more frame advantage off throws. For example, Young Link and Link are two characters that have the same fall speed, but different weight. The uthrow will send both of them up the same distance, but you may be able to true combo an aerial from it against Young Link because he is lighter. On the other hand, you certainly will not true combo an aerial from a uthrow against Link at any percent or DI because he is too heavy. Knowing this, you need to accept that you won’t true combo these characters, and you’ll need to just throw for positional advantage and abuse that instead. Character weight differences are why Marth can chaingrab Fox and Falco on FD, but he cannot chaingrab Falcon on FD (for the most part).

Another thing to consider is fall-speed. Fall speed is essentially the only determining factor for vertical throw height between different characters because throws assume everyone has the same weight, but fall speed affects how quickly they accelerate downward, fighting your uthrow. You can chaingrab and get really big juggles on Fox and Falco because they are fastfallers, but slower-falling characters can, like heavy characters, force you to throw for positional advantage instead because they get sent up higher so it’s harder to combo.

Dthrow:
This is also one of Marth’s very important throws. It can knock the opponent over at lower percentages, it can send the opponent offstage when you are near the ledge, allowing for low percent edgeguard situations (and high percent edgeguard situations), it’s good for setting up corner position and techchases, and it can combo sometimes.

Like every throw, dthrow followups are dictated by fall-speed and weight. Most true combos from dthrow only work whenever the opponent DIs poorly. There are tricks you can use to mess up your opponent’s DI, but you need to not rely on the possibility of comboing off dthrow, but it’s fine to react to it when it happens. You need to be prepared to get damage off dthrow in other ways.

Fthrow:
This throw is useful, but it can also be pretty unreliable. I believe overusing fthrow is a common bad habit for Marth players.

Against bad DI, it’s arguably Marth’s best throw. You can get fthrow chaingrabs, fthrow into fsmash, fthrow dash attack, and sometimes other stuff.

Against good DI, it’s very fickle. It doesn’t set up positional advantage as cleanly as dthrow and uthrow do, and once they DI correctly, that’s almost all you’re going to get. I believe there are some situational combos with fthrow/dthrow into pivot tipper, but I do also know that pivot tipper STILL does not guarantee that you will get follow-ups from fthrow and dthrow if they DI correctly.

Uair:
Great attack. Allows him to chase people in the air and allows him to juggle. Something to note about it is that it has more range directly above his head and less range on the sides.

Utilt:
Another great move, but only when you use it right. Some Marths will overuse this move in neutral, but it has little to no influence on the ground and its end-lag can be pretty punishable, so it’s not very safe to use unless you’re fairly sure you can get away with it.

Dair:
I love this move. It’s one of the most satisfying finishers in the game, and it’s fairly good on-stage/in close quarters too. It doesn’t give you a lot of control and influence, but it allows you to win some situations where fair and nair won’t work.

Ftilt:
I like this move. It feels like a cross between his jab and his fsmash. It’s got a pretty nice tipper and a pretty decent non-tipper. I don’t have much to say about this move except that it seems fairly straightforward and that you should just try it out and see when it works.

Jab:
This move can be very useful. It’s pretty fast and hits higher than dtilt, so it’s an easy move to land when you want to just stop someone’s momentum. Also, you can IASA this move and dtilt into each other, which is pretty sweet. However, this move is very weak, so it’s more useful when your opponent is in the air (and can’t hold down), when they’re at really high percent (so the weakness isn’t a big deal), or if they’re stuck in the corner (so they don’t have space to really maneuver around your jabs)

Up B (Dolphin Slash):
This is your recovery move and it can be used as a strong kill/edgeguard move.

Everyone should know about using this move for recovery, more or less. You can slightly change the angle at which Marth up B’s by inputting a direction on your control stick when you throw it out. Also, a good tip for recovering with this move is to aim it slightly up and out from the ledge, allowing you to weave around some edgeguards and then grabbing the ledge afterwards with your magnet hands.

The lower-front part of this move is the strong part. IT DOES NOT HAVE TO BE REVERSED TO GET THE STRONG HIT, NOR DOES THIS EXTEND HIS STRONG RANGE. THIS IS A LONG-STANDING MISCONCEPTION. Use it as a combo finisher, use it as an edgeguard, and you can also use it situationally as an on-stage kill move. It can be used out-of-shield, which is amazing when it works out.

The top of Marth’s up B isn’t that strong, but it’s a weird hitbox that lets you pop your opponents offstage when they’re high above you and at high percent. This is a pretty situational use for the move.

Bair:
This is an aerial that lets you hit things behind you. It’s fairly slow, so it’s not a big part of Marth’s game, but you can get some mileage from learning how to use it.

This move can be pretty good for hitting people who are above/behind you because it doesn’t have top-down swing, it has a Drake swing (started from the bottom). This makes it a fairly good move for edgeguarding people recovering higher (for example, I think it’s very good against Samus).

I find that people get hit by this move more than they should. I think people like to go offensive when Marth’s back is turned because a lot of Marths will spam DD grab and not cover their backs very well (because Marth as a character doesn’t), so learning when to use this move to cover your back can be helpful.

Bthrow:
This is a very situational throw. The other three throws are usually better, but bthrow has its moments.

One of the most common uses for bthrow is at high percentages when you’re near the ledge. The opponent will usually expect you to dthrow and DI in (because if they DI away at that percent, they’ll get sent too far away), which can allow you to land an fsmash or a bair.

Forward B:
This is an interesting move. It’s not an INCREDIBLE move, but it’s got its niches.

The first hit of forward B can be a pretty useful poke because you can use it seamlessly out of your dashdance. However, it is extremely weak and it’s pretty short, so it’s not that ridiculous.

At high percentages against floaty characters in the air (can’t hold down), forward B is nice because it has a very weak pop-up that can link into utilt for vertical kills.

I don’t like the later iterations of the side B too much, but it’s nice when it works out. Your opponent can escape if they hold in (because Marth steps forward) or hold down and shield, so I would only really use it when your opponent is not on the ground *and* if I have a read on their DI. Alternately, you can use them where you have the space to set up the later hits, but this is situational.

First hit of side B can be useful for edgeguarding space animals. Taj likes to call it “blowing out the candle” because of how it looks whenever you kill Fox or Falco’s up B with it.

Down B (Counter):
Not an AMAZING move, but it’s nice to know when it works when push comes to shove.

My favorite use for this move is ledgehop -> counter. This isn’t a spammable option at all, but because Marth’s ledge options are fairly slow, limited, and swingy (i.e. they’re mediocre), so lot of people will be very aggressive with you when you’re trying to recover from the ledge, so this is nice for keeping them off you if you think they’ll overextend. Although it’s not the best option, I think it’s decent at filling in some of the gaps in his ledge recovery.

This move has some situational use vs projectiles, out of shield, and if you’ve got a bait, but I think in most situations, there’s something more reliable that you can go for. I think this is just one of those moves that works out if you’ve got a read, but it shouldn’t be integral to your gameplan.

Dsmash:
Very situational move. It has an insanely strong tipper (about as strong as Fox’s usmash) and actually has very fast startup (frame 5), but it requires really weird and/or difficult setups.

Problem is, the tipper is difficult to land, and his non-tipper hitboxes for dsmash are pretty bad. Furthermore, the second swing makes the move really laggy.

I found a way to pretty consistently land tipper dsmash on a sleeping Puff. I think dsmash is marginally longer than jab, so if you use your jab as a meter stick to gauge your spacing, a tipper dsmash will connect whenever the jab BAAAAAARRREELY whiffs.

Sometimes dsmash is useful at high % because it has really fast startup, and at higher percentages, it doesn’t matter that his non-tippered hitboxes are mediocre because they are still strong enough to KO.

Usmash:
Very situational move. Sometimes you can land weak uair -> tipper usmash, but most tipper usmash setups are situational or gimmicky. Personally, I don’t use this attack at all, but I wouldn’t stop anyone from experimenting with it."""