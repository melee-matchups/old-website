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
