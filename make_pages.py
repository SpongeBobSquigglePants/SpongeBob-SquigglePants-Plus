# make_pages.py: writes the site's HTML pages (shared header, menu and footer) into ../site
import os

OUT = os.path.dirname(os.path.abspath(__file__))
VERSION, DATE, DATE_ISO = '1.0', '22 October 2026', '2026-10-22'
SITE = 'https://sbsp-plus.wubbzp.com/'  # the site's address, for link previews and search engines
ZIP = 'SpongeBob-SquigglePants-plus-v%s.zip' % VERSION
TITLE = '<cite>SpongeBob SquigglePants+</cite>'
GAME = '<cite>SpongeBob SquigglePants</cite>'

PAGES = [('index', 'Home', ''), ('features', 'Features', 'features/'), ('download', 'Download', 'download/'), ('tools', 'Tools', 'tools/'),
         ('credits', 'Credits', 'credits/')]


def head(root, title, desc, path=None):
    """path: the page's address under SITE ('' for the home page), or None for a page with no address of its own."""
    url = SITE + path if path is not None else None
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<title>%(title)s</title>
<meta name="description" content="%(desc)s"/>
<meta name="author" content="Mitch &quot;WubbzP&quot; Bentz"/>
<meta name="theme-color" content="#1d74bd"/>
%(canon)s<link rel="icon" type="image/png" sizes="32x32" href="%(r)sassets/icons/plus-32.png"/>
<link rel="icon" type="image/png" sizes="192x192" href="%(r)sassets/icons/plus-192.png"/>
<link rel="apple-touch-icon" href="%(r)sassets/icons/plus-192.png"/>
<meta property="og:site_name" content="SpongeBob SquigglePants+"/>
<meta property="og:title" content="%(title)s"/>
<meta property="og:description" content="%(desc)s"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="en_US"/>
%(ogurl)s<meta property="og:image" content="%(site)sassets/images/og-image.jpg"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="The SpongeBob SquigglePants+ logo"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:site" content="@wubbzp"/>
<meta name="twitter:title" content="%(title)s"/>
<meta name="twitter:description" content="%(desc)s"/>
<meta name="twitter:image" content="%(site)sassets/images/og-image.jpg"/>
<meta name="twitter:image:alt" content="The SpongeBob SquigglePants+ logo"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&amp;display=swap"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer"/>
<link rel="stylesheet" href="%(r)sassets/css/style.css"/>
<script>document.documentElement.className += " js";</script>
</head>
<body>
<a class="skip-link" href="#content">Skip to content</a>
<div class="site">
''' % {'title': title, 'desc': desc, 'r': root, 'site': SITE,
       'canon': '<link rel="canonical" href="%s"/>\n' % url if url else '',
       'ogurl': '<meta property="og:url" content="%s"/>\n' % url if url else ''}


def header(root, current):
    items = ''.join('<li><a href="%s%s"%s>%s</a></li>' % (root, href or './', ' aria-current="page"' if key == current else '', name)
                    for key, name, href in PAGES)
    return '''
  <header class="header">
    <a href="%(r)s" class="logo" aria-label="SpongeBob SquigglePants+ home">
      <img src="%(r)sassets/images/logo-720.png" srcset="%(r)sassets/images/logo-720.png 720w, %(r)sassets/images/logo-1440.png 1440w" sizes="300px" width="720" height="352" alt="SpongeBob SquigglePants+"/>
    </a>
    <nav class="ribbon" aria-label="Main"><ul>%(items)s</ul></nav>
  </header>
''' % {'r': root, 'items': items}


def sidebar(root, current):
    items = ''.join('<li><a href="%s%s"%s>%s</a></li>' % (root, href or './', ' aria-current="page"' if key == current else '', name)
                    for key, name, href in PAGES)
    return '''
    <aside class="sidebar">
      <nav class="menu" aria-label="Site menu">
        <ul>
          %s
          <li class="menu-divider" role="separator"></li>
          <li><a href="https://wubbzp.com" target="_blank" rel="noopener">WubbzP.com <i class="fa-solid fa-globe" aria-hidden="true"></i></a></li>
          <li><a href="https://github.com/wubbzp" target="_blank" rel="noopener">GitHub <i class="fa-brands fa-github" aria-hidden="true"></i></a></li>
          <li><a href="https://discord.gg/hKXwdhUQzr" target="_blank" rel="noopener">Discord <i class="fa-brands fa-discord" aria-hidden="true"></i></a></li>
          <li><a href="https://twitter.com/wubbzp" target="_blank" rel="noopener">Twitter <i class="fa-brands fa-twitter" aria-hidden="true"></i></a></li>
        </ul>
      </nav>
    </aside>
''' % items


def footer(root, current):
    links = ' |\n      '.join('<a href="%s%s"%s>%s</a>' % (root, href or './', ' aria-current="page"' if key == current else '', name)
                               for key, name, href in PAGES)
    return '''
  <footer class="footer">
    <nav class="footer-links" aria-label="Footer">
      %(links)s
    </nav>
    <p>%(t)s &copy; <span id="year">2026</span> Mitch "WubbzP" Bentz. A free fan-made patch.</p>
    <p>Not affiliated with or endorsed by Nickelodeon, THQ, WayForward or uDraw. <cite>SpongeBob SquarePants</cite>, <cite>SpongeBob SquigglePants</cite> and all related titles, logos and characters are trademarks of Viacom International Inc. Game art and screenshots are from %(g)s.</p>
    <div class="socials">
      <a href="https://wubbzp.com" class="social" target="_blank" rel="noopener">Visit <b class="wp"><i class="fa-solid fa-globe" aria-hidden="true"></i> WubbzP.com</b></a>
      <a href="https://github.com/wubbzp" class="social" target="_blank" rel="noopener">Find me on <b class="gh"><i class="fa-brands fa-github" aria-hidden="true"></i> GitHub</b></a>
      <a href="https://discord.gg/hKXwdhUQzr" class="social" target="_blank" rel="noopener">Join me on <b class="dc"><i class="fa-brands fa-discord" aria-hidden="true"></i> Discord</b></a>
      <a href="https://twitter.com/wubbzp" class="social" target="_blank" rel="noopener">Follow me on <b class="tw"><i class="fa-brands fa-twitter" aria-hidden="true"></i> twitter</b></a>
    </div>
  </footer>

</div>
<script src="%(r)sassets/js/site.js"></script>
</body>
</html>
''' % {'links': links, 't': TITLE, 'g': GAME, 'r': root}


def page_title(root, key, alt):
    return '<h1><img class="title-img" src="%sassets/images/titles/%s.png" alt="%s"/></h1>' % (root, key, alt)


def inner(root, current, title_key, title_alt, body):
    return '''
  <div class="stage stage-page">
%s
    <main class="page" id="content">
      <div class="page-head">
        %s
        <a href="%s" class="back-btn" aria-label="Back to home"><span aria-hidden="true">Back</span></a>
      </div>
%s
    </main>
  </div>
''' % (sidebar(root, current), page_title(root, title_key, title_alt), root or './', body)


# ---------------------------------------------------------------- home

SLIDES = [('title', 'The title screen, now with a "+"'), ('replay-iconbob', 'IconBob: a new world in Nanogame Replay'),
          ('candid-krabs', '"Candid Krabs", playable on the Wii'), ('dpad', 'Steer the IconBob games with the D-Pad'),
          ('chum-is-fum', '"Chum Is Fum"'), ('gary-is-going-places', '"Gary Is Going Places"'),
          ('puzzle-intro', '"Puzzle de Pants": the cut nanogame, restored'),
          ('options', 'A Credits button, and a new frame on the wall'), ('credits', 'The full credits, now in Options')]


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s)


def home():
    r = ''
    imgs = '\n'.join('          <img src="assets/images/shots/%s.jpg" width="854" height="480" alt="%s" data-caption="%s"%s/>'
                     % (f, strip_tags(c).replace('"', '&quot;'), strip_tags(c).replace('"', '&quot;'),
                        ' class="on"' if i == 0 else '' ) for i, (f, c) in enumerate(SLIDES))
    body = '''
  <div class="stage">
%(side)s
    <main class="showcase" id="content">
      <h1 class="visually-hidden">SpongeBob SquigglePants+</h1>
      <div class="gold-frame">
        <div class="slides">
%(imgs)s
        </div>
      </div>
      <p class="slide-caption" id="slide-caption" aria-live="polite">The title screen, now with a "+"</p>
      <ul class="dots" id="dots" aria-label="Pictures"></ul>
      <h2 class="tiles-head" id="new-title"><img class="title-img" src="assets/images/titles/whats-new.png" alt="What's New"/></h2>
      <ul class="tiles">
        <li><a class="tile" href="features/#iconbob"><img src="assets/images/frames/world-8.png" width="195" height="159" alt=""/><b>IconBob</b><span>7 nanogames from the 3DS version, in Replay</span></a></li>
        <li><a class="tile" href="features/#puzzle"><img src="assets/images/frames/puzzle-de-pants.png" width="195" height="159" alt=""/><b>"Puzzle de Pants"</b><span>The cut nanogame, playable at last</span></a></li>
        <li><a class="tile" href="features/#complete"><img src="assets/images/frames/world-1.png" width="195" height="159" alt=""/><b>100%% for Real</b><span>The 99%% bug is fixed: your save can reach 100%%</span></a></li>
        <li><a class="tile" href="features/#fixes"><img src="assets/images/frames/world-5.png" width="195" height="159" alt=""/><b>Fixes</b><span>Corrected titles, the full credits, no more slowdown</span></a></li>
      </ul>
    </main>

    <section class="feature" aria-label="The patch">
      <img class="medal" src="assets/images/ui/ribbon-medal.png" width="128" height="268" alt=""/>
      <div class="burst" aria-hidden="true">Out<br>Now!</div>
      <div class="feature-card">
        <b>%(t)s</b>
        <span class="version">Version %(v)s &middot; %(d)s</span><br>
        Seven lost 3DS games, a cut nanogame, the 99%% bug fixed and lots more, for the Wii version of %(g)s.
      </div>
      <a class="stack-btn" href="download/"><small>click here to</small>Download!</a>
      <span class="small-note">Free. You need your own copy of the game (US).<br><a href="features/">See everything that's new</a></span>
    </section>

    <div class="patchy-spot">
      <span class="bubble" aria-live="polite"></span>
      <button type="button" class="patchy" aria-label="Poke Patchy the Pirate" title="Poke Patchy!">
        <img src="assets/images/patchy-podium.png" width="401" height="463" alt=""/>
      </button>
    </div>
  </div>

  <section class="box" aria-labelledby="news-title">
    <div class="box-inner">
      <h2 id="news-title"><img class="title-img" src="assets/images/titles/news.png" alt="News"/></h2>
      <ul class="news">
        <li>
          <time datetime="%(diso)s">Oct<br>2026</time>
          <div><b>Version %(v)s is out!</b><span>The first release of %(t)s. <a href="download/">Download it</a></span></div>
        </li>
        <li>
          <span class="news-date soon">Coming<br>Soon</span>
          <div><b>The trailer</b><span>A "now available" trailer, in the style of the original game's launch trailer.</span></div>
        </li>
      </ul>
    </div>
  </section>

  <section class="box" aria-labelledby="fun-title">
    <div class="box-inner">
      <h2 id="fun-title"><img class="title-img" src="assets/images/titles/fun-fact.png" alt="Fun Fact!"/></h2>
      <p>Tucked away in the game's save files is a stowaway: the save banner and icon of <cite>Batman: The Brave and the Bold - The Videogame</cite>, WayForward's 2010 Wii game. They sit right next to %(g)s' own, but the game never uses them: it only asks for its own banner and icons, which the Wii shows in its Data Management screen.</p>
      <p>From what we can tell, %(g)s' save system was built on Batman's, and these were left behind when it moved in.</p>
      <div class="fun-pair">
        <figure>
          <div class="fun-row">
            <img src="assets/images/fun/batman-banner.png" width="664" height="304" alt="The Batman: The Brave and the Bold save banner"/>
            <img src="assets/images/fun/batman-icon.png" width="280" height="304" alt="The Batman save icon: Batman running"/>
          </div>
          <figcaption>Left behind: <cite>Batman</cite>'s banner and icon</figcaption>
        </figure>
        <figure>
          <div class="fun-row">
            <img src="assets/images/fun/sbsp-banner.png" width="664" height="304" alt="The SpongeBob SquigglePants save banner"/>
            <img src="assets/images/fun/sbsp-icon.gif" width="280" height="304" alt="The SpongeBob SquigglePants save icon, animated"/>
          </div>
          <figcaption>The ones the game uses: %(g)s' banner and icon</figcaption>
        </figure>
      </div>
    </div>
  </section>
''' % {'side': sidebar(r, 'index'), 'imgs': imgs, 't': TITLE, 'g': GAME, 'v': VERSION, 'd': DATE, 'diso': DATE_ISO}
    return (head(r, 'SpongeBob SquigglePants+', 'SpongeBob SquigglePants+: a free fan-made patch for SpongeBob '
                 'SquigglePants on the Wii, with the lost 3DS IconBob games, the cut nanogame &quot;Puzzle de Pants&quot; and the 99% bug fixed.', '')
            + header(r, 'index') + body + footer(r, 'index'))


# ---------------------------------------------------------------- features

ICONBOB = ['Gary Is Going Places', 'SpongeBob Says', 'Chum Is Fum', 'Jellyfish Joy Ride', 'Candid Krabs', 'To Dive For',
           'Bikini Bottom on Ice']
FIXES = [('Sea is for Coloring', 'Sea Is for Coloring'), ("Rollin' With My Homies", "Rollin' with My Homies"),
         ('The Show Off Show', 'The Show-Off Show'), ('Mr. Krabs Cash Grab', "Mr. Krabs' Cash Grab"),
         ('Ping Pong Pals', 'Ping-Pong Pals'), ('Water You Waving For', 'Water You Waving For?'),
         ('That Takes The Spongecake', 'That Takes the Spongecake'), ('Select A World', 'Select a World')]
LOGOS = [('us', 'United States'), ('uk', 'United Kingdom'), ('fr', 'French'), ('de', 'German'), ('it', 'Italian'),
         ('nl', 'Dutch'), ('es', 'Spanish')]


def features():
    r = '../'
    games = '\n'.join('          <li><img src="../assets/images/ui/medal-%s.png" width="62" height="62" alt=""/>"%s"</li>'
                      % (['gold', 'silver', 'bronze'][i % 3], g) for i, g in enumerate(ICONBOB))
    fixes = '\n'.join('          <tr><td>%s</td><td>%s</td></tr>' % (a, b) for a, b in FIXES)
    logos = '\n'.join('          <figure><img src="../assets/images/logos/%s.png" alt="The %s title logo with a plus"/><figcaption>%s</figcaption></figure>'
                      % (k, n, n) for k, n in LOGOS)
    body = '''      <div class="guide">
        <img src="../assets/images/patchy-wham.png" width="323" height="432" alt=""/>
        <p>Ahoy! Here's everything %(t)s adds to the game. Each part can be turned on or off in Riivolution.</p>
      </div>

      <section class="panel" id="iconbob">
        <h2>IconBob, in Nanogame Replay</h2>
        <figure class="shot"><img src="../assets/images/shots/replay-iconbob.jpg" width="854" height="480" alt="Nanogame Replay with the IconBob frame picked"/></figure>
        <p>The Nintendo 3DS version had an eighth world, IconBob. Its seven nanogames were left on the Wii disc but never used. Now they're the eighth Nanogame Replay section, the one the game was made ready for, just before Remix, as on the 3DS.</p>
        <ul class="game-list">
%(games)s
        </ul>
        <p>They were made for the 3DS circle pad, so you steer them with the <strong>D-Pad</strong> (a Nunchuk works too). Their best scores, medals and "%% Unlocked" are kept in your normal save, which still works without the patch.</p>
        <div class="shot-row">
          <figure class="shot"><img src="../assets/images/shots/candid-krabs.jpg" width="854" height="480" alt="Candid Krabs"/></figure>
          <figure class="shot silver"><img src="../assets/images/shots/chum-is-fum.jpg" width="854" height="480" alt="Chum Is Fum"/></figure>
          <figure class="shot bronze"><img src="../assets/images/shots/dpad.jpg" width="854" height="480" alt="The controls screen, saying D-PAD!"/></figure>
        </div>
      </section>

      <section class="panel" id="puzzle">
        <h2>Credits, and "Puzzle de Pants"</h2>
        <figure class="shot silver"><img src="../assets/images/shots/puzzle-intro.jpg" width="854" height="480" alt="Puzzle de Pants: ROTATE! TAP!"/></figure>
        <p>The Options screen gets a <strong>Credits</strong> button for the game's scrolling credits, which were only reachable from the developers' menu. Scroll them with the D-Pad or the pen, and leave with B.</p>
        <p>Watch them all the way to the end, and a new picture frame appears on the Options wall. Pick it to play "Puzzle de Pants", the nanogame that was cut from the game: tap to rotate the pieces until SpongeBob is whole.</p>
      </section>

      <section class="panel" id="complete">
        <h2>100%% for Real</h2>
        <img class="panel-icon" src="../assets/images/patchy-potty.png" width="368" height="480" alt="Patchy and Potty"/>
        <p>In the original game, a save with everything done could still show 99%%. The game's own 100%% rewards, the last stamps and the last Patchy movie, unlock at 100 rounds in a Nanogame Replay game, but the save screen's last point needed <em>101</em>. Now 100 rounds count there too.</p>
        <h3>What 100%% needs</h3>
        <ul class="checklist">
          <li>A gold medal in every Collection and every Nanogame Replay game</li>
          <li>The minigames "RetroBob", "Seasons of Sandy" and "Rattle and Roll" at 100, and "Showboating Shower" at 50</li>
          <li>75 rounds in Remix</li>
          <li>100 rounds in any one Nanogame Replay game (101 without the fix)</li>
        </ul>
      </section>

      <section class="panel" id="fixes">
        <h2>Fixes and Touch-Ups</h2>
        <figure class="shot"><img src="../assets/images/shots/credits.jpg" width="854" height="480" alt="The credits, with the new lines"/></figure>
        <h3>Corrected titles</h3>
        <p>Twenty nanogame titles are set in proper title case, and menu text is tidied up:</p>
        <table class="fixes">
          <thead><tr><th>Before</th><th>After</th></tr></thead>
          <tbody>
%(fixes)s
          </tbody>
        </table>
        <h3>The credits</h3>
        <p>Luke Brookshier's writer credit from the 3DS version is restored, Jake Kaufman is credited as Composer, and the game's title is in italics wherever the game writes it, in every language.</p>
        <h3>No more slowdown</h3>
        <p>The ending credits after the PixelBob world (Movies entry 7) used to drop to a few frames a second. They run smoothly now.</p>
        <h3>Candid Krabs</h3>
        <p>Its 3DS-sized pictures were too big for the Wii and crashed the game. They're resized, so it plays properly.</p>
      </section>

      <section class="panel" id="logo">
        <h2>The "+" Logo, in Every Language</h2>
        <p>The title screen's logo gets a "+", whichever language your Wii is set to:</p>
        <div class="logos">
%(logos)s
        </div>
      </section>

      <section class="panel" id="devmenu">
        <h2>The Dev Menu (Optional)</h2>
        <p>The developers' own menu is still in the game, with its controls taken out. Turn this option on and the game starts in it, with D-Pad and button controls put back. It's off by default.</p>
      </section>
''' % {'games': games, 'fixes': fixes, 'logos': logos, 't': TITLE}
    return (head(r, 'Features | SpongeBob SquigglePants+', 'Everything SpongeBob SquigglePants+ adds: the IconBob games, '
                 '&quot;Puzzle de Pants&quot;, the 100% fix, corrected titles and more.', 'features/')
            + header(r, 'features') + inner(r, 'features', 'features', 'Features', body) + footer(r, 'features'))


# ---------------------------------------------------------------- download

OPTIONS = [('100% Completion Fix', True, '100 rounds in a Nanogame Replay game count for the save screen\'s last point (it needed 101), so the save can show 100%.'),
           ('Ending Credits Slowdown Fix', True, 'The credits after PixelBob run at full speed.'),
           ('Title and Credit Fixes', True, 'Corrected titles and text, the restored credits, the italic title, and "D-PAD!" on the IconBob controls screen.'),
           ('SpongeBob SquigglePants+ Logo', True, 'The high-quality <cite>SpongeBob SquigglePants+</cite> logo on the US title screen, and a "+" on every other language\'s logo.'),
           ('IconBob in Replay', True, 'The seven IconBob games as the eighth Replay section, before Remix.'),
           ('Credits and Puzzle de Pants in Options', True, 'The Credits button, and the Puzzle de Pants frame once you have watched them.'),
           ('Dev Menu', False, "Starts the game in the developers' menu.")]


def download():
    r = '../'
    opts = '\n'.join('          <tr><th>%s</th><td><span class="pill%s">%s</span></td><td>%s</td></tr>'
                     % (n, '' if on else ' off', 'On' if on else 'Off', d) for n, on, d in OPTIONS)
    body = '''      <div class="guide">
        <img src="../assets/images/patchy-podium.png" width="401" height="463" alt=""/>
        <p>It's free! Ye'll need yer own copy of the game, a few minutes, and a sprinkle of pirate patience.</p>
      </div>

      <section class="panel">
        <h2>Version %(v)s</h2>
        <p>Released %(d)s. For the US Wii version of %(g)s (game ID <code>SS8E78</code>).</p>
        <a class="stack-btn" href="../downloads/%(zip)s" download><small>click here to</small>Download %(t)s</a>
        <div class="callout"><b>Why do I have to make some of the files myself?</b> The download only contains the patch: my own changes, and the tools that apply them. The game's own files belong to Nickelodeon and THQ, so the tools build the patched ones from your copy of the game.</div>
      </section>

      <section class="panel">
        <h2>What You Need</h2>
        <ul>
          <li>Your own copy of %(g)s for the Wii (US, <code>SS8E78</code>) and the uDraw GameTablet.</li>
          <li>A Wii with <a href="https://riivolution.github.io/" target="_blank" rel="noopener">Riivolution</a> installed, or the <a href="https://dolphin-emu.org/" target="_blank" rel="noopener">Dolphin</a> emulator.</li>
          <li><a href="https://www.python.org/downloads/" target="_blank" rel="noopener">Python 3</a> on your computer, to make the patched files (once).</li>
        </ul>
      </section>

      <section class="panel">
        <h2><img class="title-img" src="../assets/images/titles/install.png" alt="How to Install"/></h2>
        <ol class="steps">
          <li><b>Unzip the download.</b>Inside are the <code>riivolution</code> folder, the tools, and an empty <code>your-game-files</code> folder.</li>
          <li><b>Copy four files from your game.</b>In Dolphin, right-click the game, choose <em>Properties</em>, then <em>Filesystem</em>. Right-click each of <code>Boot.vol</code>, <code>menus.vol</code>, <code>Microgames.vol</code> and <code>Game305.vol</code>, choose <em>Extract File</em>, and save it into <code>your-game-files</code>. (On a Wii, first back up your disc with <a href="https://wiibrew.org/wiki/CleanRip" target="_blank" rel="noopener">CleanRip</a>, then open the backup in Dolphin.)</li>
          <li><b>Make the patched files.</b>Double-click <code>Make SquigglePants+ Files.bat</code> (Windows), or run <code>make-files.sh</code> (Mac or Linux). It checks your files and writes the <code>SquigglePants</code> folder.</li>
          <li><b>Copy two folders to your SD card.</b>Put <code>riivolution</code> and <code>SquigglePants</code> at the root of the SD card. For Dolphin, put them in Dolphin's <code>Load/Riivolution</code> folder instead.</li>
          <li><b>Play!</b>Start Riivolution, pick the game and turn the options on. In Dolphin, right-click the game and choose <em>Start with Riivolution Patches</em>.</li>
        </ol>
      </section>

      <section class="panel">
        <h2>The Options</h2>
        <table class="options">
          <thead><tr><th>Option</th><th>Default</th><th>What it does</th></tr></thead>
          <tbody>
%(opts)s
          </tbody>
        </table>
      </section>

      <section class="panel faq">
        <h2><img class="title-img" src="../assets/images/titles/faq.png" alt="Questions"/></h2>
        <details><summary>Will it mess up my save?</summary><p>No. Everything the patch saves (IconBob's records and the Puzzle de Pants unlock) goes in spare space in your normal save, and the save still works without the patch.</p></details>
        <details><summary>Does it work with the European or Australian version?</summary><p>Not yet: it's made for the US version (<code>SS8E78</code>). The title logo has its "+" in every language, though.</p></details>
        <details><summary>Do I need the uDraw GameTablet?</summary><p>Yes, as for the original game. The IconBob games are steered with the D-Pad on the Wii Remote.</p></details>
        <details><summary>Does "Puzzle de Pants" save my score?</summary><p>No, it's just for fun: nothing it does is saved.</p></details>
        <details><summary>What do I need for 100%%?</summary><p>Gold in every Collection and every Nanogame Replay game, "RetroBob", "Seasons of Sandy" and "Rattle and Roll" at 100, "Showboating Shower" at 50, 75 rounds in Remix, and 100 rounds in any one Nanogame Replay game. See <a href="../features/#complete">100%% for Real</a>.</p></details>
        <details><summary>The tool says a file isn't the right one.</summary><p>It checks each file against the US version's. Make sure you copied the files from <code>SS8E78</code>, and that they aren't already patched.</p></details>
      </section>
''' % {'v': VERSION, 'd': DATE, 'g': GAME, 't': TITLE, 'zip': ZIP, 'opts': opts}
    return (head(r, 'Download | SpongeBob SquigglePants+', 'Download SpongeBob SquigglePants+ and how to install it with '
                 'Riivolution or Dolphin.', 'download/')
            + header(r, 'download') + inner(r, 'download', 'download', 'Download', body) + footer(r, 'download'))


# ---------------------------------------------------------------- credits

VOLX = 'https://github.com/spongebobsquigglepants/volextractor'
VOLX_FORMATS = [('<code>.image</code>, <code>.texture</code>, <code>.tpl</code>', 'PNG, with transparency'),
                ('<code>.anim</code>', 'A PNG for each frame, and an animated GIF'),
                ('<code>.text</code>', 'A spreadsheet (CSV) with a column for each language'),
                ('<code>.font</code>', 'A PNG sheet of every letter, and a CSV of their sizes'),
                ('<code>.wave</code>', 'WAV'),
                ('<code>.arc</code>', 'Unpacked, with what\'s inside converted too')]


def tools():
    r = '../'
    formats = '\n'.join('          <tr><th>%s</th><td>%s</td></tr>' % f for f in VOLX_FORMATS)
    body = '''      <div class="guide">
        <img src="../assets/images/patchy-wham.png" width="323" height="432" alt=""/>
        <p>Want to see how the game's made? Here be the tools for diggin' through its treasure chest of files!</p>
      </div>

      <section class="panel" id="volextractor">
        <h2>VolExtractor</h2>
        <p>Almost everything in %(g)s is packed into <code>.vol</code> archives: the pictures, animations, text, fonts and sounds. VolExtractor unpacks them and turns what's inside into files you can open.</p>
        <div class="shot-row">
          <figure class="shot"><img src="../assets/images/tools/sample-image.jpg" width="854" height="480" alt="The game's own title logo, converted to a PNG"/></figure>
          <figure class="shot silver"><img src="../assets/images/tools/sample-font.jpg" width="854" height="480" alt="Part of a font's letter sheet"/></figure>
          <figure class="shot bronze"><img src="../assets/images/tools/sample-anim.gif" width="427" height="240" alt="SpongeBob's loading animation, as a GIF"/></figure>
        </div>
        <table class="fixes">
          <thead><tr><th>In the game</th><th>What you get</th></tr></thead>
          <tbody>
%(formats)s
          </tbody>
        </table>
        <p>Every file is also saved exactly as it was stored, so nothing is left out.</p>
        <div class="callout"><b>Made for %(g)s on the Wii.</b> Other games built with WayForward's engine, EngineBlack, may use some of the same formats, but they haven't been tested. Not all of them use <code>.vol</code> archives: <cite>Batman: The Brave and the Bold - The Videogame</cite> on the Wii doesn't, for one.</div>
        <a class="stack-btn" href="%(x)s/archive/refs/heads/main.zip"><small>click here to</small>Download VolExtractor</a>
        <p class="center"><a href="%(x)s" target="_blank" rel="noopener"><i class="fa-brands fa-github" aria-hidden="true"></i> See it on GitHub</a></p>
      </section>

      <section class="panel">
        <h2>How to Use It</h2>
        <ol class="steps">
          <li><b>Get Python.</b>Install <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">Python 3</a> (on Windows, tick <em>Add python.exe to PATH</em>). VolExtractor installs the one extra package it needs the first time.</li>
          <li><b>Copy the game's archives.</b>In Dolphin, right-click the game, choose <em>Properties</em>, then <em>Filesystem</em>, and extract the <code>.vol</code> files into the VolExtractor folder.</li>
          <li><b>Run it.</b>Double-click <code>extract_all.bat</code> (Windows) or run <code>extract_all.sh</code> (Mac or Linux). You can also drag files or folders onto <code>extract_all.bat</code>.</li>
          <li><b>Look inside.</b>Each archive gets a <code>_extracted</code> folder next to it, with <code>raw</code> (the files as stored) and <code>converted</code> (the files you can open).</li>
        </ol>
        <div class="callout"><b>No game files are included.</b> VolExtractor only reads the copy of the game you already own.</div>
      </section>
''' % {'g': GAME, 'formats': formats, 'x': VOLX}
    return (head(r, 'Tools | SpongeBob SquigglePants+', 'VolExtractor: unpack the .vol archives of SpongeBob SquigglePants '
                 'into pictures, animations, text, fonts and sounds.', 'tools/')
            + header(r, 'tools') + inner(r, 'tools', 'tools', 'Tools', body) + footer(r, 'tools'))


def credits():
    r = '../'
    body = '''      <div class="guide">
        <img src="../assets/images/patchy-potty.png" width="368" height="480" alt=""/>
        <p>A hearty thanks to everyone who made the game! Potty, take a bow!</p>
      </div>

      <section class="panel">
        <h2>%(t)s</h2>
        <dl class="credit-list">
          <dt>Patch</dt><dd>Mitch "WubbzP" Bentz</dd>
          <dt>Website</dt><dd>Mitch "WubbzP" Bentz</dd>
        </dl>
      </section>

      <section class="panel">
        <h2>The Original Game</h2>
        <p>%(g)s (Wii and Nintendo 3DS, 2011) was developed by WayForward Technologies and published by THQ, with Nickelodeon. Its full credits are in the game: press <strong>Credits</strong> on the Options screen.</p>
        <dl class="credit-list">
          <dt>Creative Director</dt><dd>Matt Bozon</dd>
          <dt>Designer / Director</dt><dd>James Montagna</dd>
          <dt>Writer</dt><dd>Luke Brookshier</dd>
          <dt>Composer</dt><dd>Jake Kaufman</dd>
        </dl>
        <p><cite>SpongeBob SquarePants</cite> was created by Stephen Hillenburg.</p>
      </section>

      <section class="panel">
        <h2>Thanks</h2>
        <p>To the makers of <a href="https://riivolution.github.io/" target="_blank" rel="noopener">Riivolution</a> and <a href="https://dolphin-emu.org/" target="_blank" rel="noopener">Dolphin</a>, which made the patch possible to build and to test.</p>
        <p>And to Sandmanfan, Berdstep, Rnjwalkthroughs, Andykishore and KyoakuNaKira.</p>
      </section>
''' % {'t': TITLE, 'g': GAME}
    return (head(r, 'Credits | SpongeBob SquigglePants+', 'Who made SpongeBob SquigglePants+, and the original game.', 'credits/')
            + header(r, 'credits') + inner(r, 'credits', 'credits', 'Credits', body) + footer(r, 'credits'))


def not_found():
    r = '/'
    body = '''      <div class="guide">
        <img src="/assets/images/patchy-wham.png" width="323" height="432" alt=""/>
        <p>Arrr! That page has sunk to the bottom of Bikini Bottom.</p>
      </div>
      <a class="stack-btn" href="/"><small>click here</small>Back to Home</a>
'''
    return (head(r, 'Page Not Found | SpongeBob SquigglePants+', 'This page could not be found.')
            + header(r, '') + inner(r, '', 'not-found', 'Uh-Oh!', body) + footer(r, ''))


def main():
    out = {'index.html': home(), 'features/index.html': features(), 'download/index.html': download(), 'tools/index.html': tools(),
           'credits/index.html': credits(), '404.html': not_found()}
    for path, html in out.items():
        p = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', newline='\n').write(html)
    os.makedirs(os.path.join(OUT, 'downloads'), exist_ok=True)
    print('wrote', ', '.join(out))


if __name__ == '__main__':
    main()
