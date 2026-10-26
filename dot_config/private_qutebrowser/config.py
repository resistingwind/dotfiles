c.tabs.position = 'left'
c.tabs.show = 'switching'
c.tabs.favicons.show = 'never'
c.tabs.width = '7%'
c.tabs.padding = { 'top': 5, 'bottom': 5, 'left': 9, 'right': 9 }
c.tabs.indicator.width = 0
c.tabs.title.format = '{audio}{current_title}'

c.fonts.web.size.default = 20
c.fonts.default_size = '13pt'
c.fonts.default_family = ['Comic True Mono']
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'

c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'nixpkgs': 'https://search.nixos.org/packages?channel=unstable&query={}',
    'yt': 'https://youtube.com/results?search_query={}',
    'gh': 'https://github.com/search?o=desc&q={}&s=starts'
}

c.statusbar.show = "in-mode"

c.auto_save.session = True

c.content.blocking.enabled = True

config.load_autoconfig(False)
