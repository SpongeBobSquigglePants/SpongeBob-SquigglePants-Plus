SpongeBob SquigglePants+ website

A static site: upload everything in this folder to the root of your web host (GitHub Pages works).

- index.html is the home page; features/, download/ and credits/ are the other pages; 404.html is the
  "page not found" page (it uses paths from the site's root, so it works once the site is at a domain's root).
- Put the release zip, SpongeBob-SquigglePants-plus-v1.0.zip, in the downloads/ folder: the Download page
  links to downloads/SpongeBob-SquigglePants-plus-v1.0.zip.
- The pages are built by make_pages.py (not needed on the server); the images come from the game's files,
  the patch's builds and screenshots from the patched game.
- Fonts: Nunito (Google Fonts) and Font Awesome icons (cdnjs), loaded from the web.
