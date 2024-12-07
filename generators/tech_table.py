html="""<html>
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
				<a class="bar-a" href="./tech.html"><button class="bar-button">Tech Table</button></a>
				<a class="bar-a" href="./framedata.html"><button class="bar-button">Framedata</button></a>
				<a class="bar-a" href="./matchups.html"><button class="bar-button">MatchUps</button></a>
				<a class="bar-a" href="./stages.html"><button class="bar-button">Stages</button></a>
				<a class="bar-a" href="./options.html"><button class="bar-button">options</button></a>
			</center>
		</div>
		<br>
		<div id="main-content" style="line-height: 1.6; font-size: 20px;">
            <center>
                By: <a href="#type"><button style="font-size: 20px;">Type</button></a>
                <a href="#use"><button style="font-size: 20px;">Usefulness</button></a>
                <a href="#dif"><button style="font-size: 20px;">Difficulty</button></a>
            </center>
            <br>
            %TABLE%
		</div>
	</body>
</html>
"""

table_html = """<table id = "%ID%" class="tech-table tab-content">
                <tr>
                    <th style="border-bottom: 5px solid; width: 64;">Type</th>
                    <th style="border-bottom: 5px solid; width: calc( 100% - ( 64 + 64 + 64 + 128 ) );">Tech name</th>
                    <th style="border-bottom: 5px solid; width: 64;">Difficulty</th>
                    <th style="border-bottom: 5px solid; width: 64;">Usefulness</th>
                    <th style="border-bottom: 5px solid; width: 128;">Link(s)</th>
                </tr>
                
%TABLE%
            </table>"""

row_html = """                <tr>
                    <th style="%LINE%padding: 20px; border-right: 5px solid;">%TYPE%</th>
                    <th style="%LINE%padding: 20px; ">%NAME%</th>
                    <th style="%LINE%padding: 20px; ">%DIFF%</th>
                    <th style="%LINE%padding: 20px; ">%USE%</th>
                    <th style="%LINE%padding: 20px; ">%LINK%</th>
                </tr>
"""

def make_stars(n_stars, revs_colors=False):
    fill_star = "★"
    star = "☆"
    colors = {
        0: "#FF00FF",
        5: "#990000",
        4: "#CD7F32",
        3: "#c0c0c0",
        2: "#ffbf00",
        1: "#00D0FF",
    } if revs_colors else {
        0: "#FF00FF",
        1: "#990000",
        2: "#CD7F32",
        3: "#c0c0c0",
        4: "#ffbf00",
        5: "#00D0FF",
    }
    
    return f"<span style='color: {colors[n_stars]}'>{(fill_star*n_stars) + (star*(5 - n_stars))}</span>"

def make_links(links):
    return " ".join([f'<a target="_blank" href="{url}">-Link {i+1}-</a><br>' for i, url in enumerate(links)])

def make_table(techs, id_, index):
    return table_html.replace("%ID%", id_).replace("%TABLE%", "\n".join(
        [
            row_html
            .replace("%NAME%", tech[0])
            .replace("%TYPE%", tech[1])
            .replace("%DIFF%", make_stars(tech[2], revs_colors=True))
            .replace("%USE%", make_stars(tech[3]))
            .replace("%LINK%", make_links(tech[4]))
            .replace("%LINK%", make_links(tech[4]))
            .replace("%LINE%",
                "border-top: 5px solid; "
                if (i > 0) and techs[i - 1][index] != tech[index]
                else ""
            ) 
            for i, tech in enumerate(techs)
        ]
    ))

marth_tech = [
    ("Short hops", "Basics", 1, 5, []),
    ("Spaceing / micro spaceing", "Basics", 1, 5, []),
    ("Short Hop / Full Hop Aerials (fastfall + auto cancel / l cancel)", "Basics", 1, 5, []),
    ("Retreating Aerials (remember nair)", "Basics", 1, 5, []),
    
    ("Dash dance / Foxtrot", "Movement", 2, 5, [
        "https://melee.guru/characters/tech/dash-dance.html",
        "https://melee.guru/characters/tech/fox-trot.html"
    ]),
    ("Shield dashing / Shield stopping / Shield pivoting", "Movement", 2, 4, [
        "https://melee.guru/characters/tech/shield-stop.html"
    ]),
    ("Boost Grab (dash attack cancel grab)", "Movement", 3, 3, [
        "https://melee.guru/characters/tech/boost-grab.html"
    ]),
    ("Wave dash / Wave landing", "Movement", 2, 5, [
        "https://melee.guru/characters/tech/wavedash.html",
        "https://melee.guru/characters/tech/waveland.html"
    ]),
    ("Wave dash / Wave landing + Act out of Wave dash / Wave land", "Movement", 2, 5, [
        "https://melee.guru/characters/tech/wavedash.html",
        "https://melee.guru/characters/tech/waveland.html"
    ]),
    ("Wave dash out of Shield", "Movement", 2, 5, [
        "https://melee.guru/characters/tech/wavedash.html"
    ]),
    ("Dash out of crouch", "Movement", 3, 4, [
        "https://www.youtube.com/watch?v=KsejlibhFvU"
    ]),
    ("Act out of SHFFL", "Movement", 3, 5, []),
    
    ("Act out of D-Tilt IASA", "Movement", 1, 5, [
        "https://melee.guru/characters/tech/dtilt-iasa.html"
    ]),
    ("Run cancel", "Movement", 1, 4, [
        "https://melee.guru/characters/tech/run-cancel.html"
    ]),
    ("Pivots", "Movement", 4, 4, [
        "https://melee.guru/characters/tech/empty-pivot.html",
        "https://melee.guru/characters/tech/perfect-pivot.html"
    ]),
    ("Stationary Dash", "Movement", 3, 3, [
        "https://melee.guru/characters/tech/stationary-dash.html"
    ]),
    ("Fair -> Waveland", "Movement", 3, 2, [
        "https://melee.guru/characters/tech/fair-waveland.html"
    ]),
    
    ("Crouch Cancel + Act out of CC", "Defence", 2, 5, [
        "https://melee.guru/characters/tech/crouch-cancel.html"
    ]),
    ("Teaching / mix up tech", "Defence", 2, 5, [
        "https://melee.guru/characters/tech/teching.html"
    ]),
    ("Powersheilding -> WaveDash / Aerial", "Defence", 4, 3, [
        "https://melee.guru/characters/tech/powershield.html"
    ]),
    ("ASDI / ASDI down", "Defence", 3, 5, [
        "https://melee.guru/characters/tech/automatic-smash-directional-influence.html"
    ]),
    ("Amsah Tech", "Defence", 3, 4, [
        "https://melee.guru/characters/tech/amsah-tech.html"
    ]),
    ("Ledge tech", "Defence", 3, 4, [
        "https://melee.guru/characters/tech/ledge-tech.html"
    ]),
    ("SDI (fox uair/shine in UP)", "Defence", 4, 4, [
        "https://melee.guru/characters/tech/smash-directional-influence.html"
    ]),
    
    ("Ledge dash", "Ledge", 3, 4, [
        "https://melee.guru/characters/tech/ledge-dash.html"
    ]),
    ("INV Ledge Fair", "Ledge", 2, 5, [
        "https://www.youtube.com/watch?v=veeJBKLGATE"
    ]),
    ("Sweet spot Up B", "Ledge", 2, 5, [
        "https://www.youtube.com/watch?v=wB85NELi_tg"
    ]),
    ("Hax dash", "Ledge", 4, 3, [
        "https://melee.guru/characters/tech/haxdash.html"
    ]),
    ("Ledge hogging (WD + fastfall / turn around bair)", "Ledge", 3, 5, [
        "https://melee.guru/characters/tech/wavedash.html",
        "https://melee.guru/characters/tech/waveland.html"
    ]),
    
    ("Shield drop / Shai Drop", "Platform", 4, 4, [
        "https://melee.guru/characters/tech/shai-drop.html",
        "https://melee.guru/characters/tech/shield-drop.html"
    ]),
    ("NILs", "Platform", 3, 2, [
        "https://melee.guru/characters/tech/no-impact-land.html"
    ]),
    ("Edge cancel Aerials", "Platform", 3, 4, [
        "https://melee.guru/characters/tech/edge-cancels.html"
    ]),
    ("Drop cancels", "Platform", 5, 3, [
        "https://melee.guru/characters/tech/drop-cancel.html"
    ]),
    ("Platform Push off", "Platform", 2, 2, [
        "https://melee.guru/characters/tech/platform-pushoff.html"
    ]),
    ("Double Fair / Fair -> Uair", "Attacks", 3, 4, [
        "https://melee.guru/characters/tech/short-hop-double-aerial.html"
    ]),
    ("Jump Cancel grabs", "Attacks", 2, 5, [
        "https://melee.guru/characters/tech/jump-cancel-grab.html"
    ]),
    ("Reverse jab", "Attacks", 1, 1, []),
    ("Instant dash attack", "Attacks", 1, 1, []),
    ("Reverse B", "Attacks", 1, 3, [
        "https://melee.guru/characters/tech/b-reversal.html"
    ]),
    ("Attacks on Sheild", "Attacks", 3, 4, []),
    
    ("Edge guarding fox in UP", "Attacks", 3, 5, []),
    
]

types = [
    "Basics",
    "Movement",
    "Defence",
    "Ledge",
    "Platform",
    "Attacks"
]

with open("./../tech.html", "w", encoding="utf-8") as fp:
    fp.write(html.replace("%TABLE%", "\n\n".join([
        make_table(sorted(marth_tech, key=lambda v: (types.index(v[1]), 5-v[3], 5-v[2])), "type", 1),
        make_table(sorted(marth_tech, key=lambda v: (5-v[3], types.index(v[1]), 5-v[2])), "use", 3),
        make_table(sorted(marth_tech, key=lambda v: (v[2], types.index(v[1]), 5-v[3])), "dif", 2),
    ])))    
