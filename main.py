from curses.ascii import NUL


def define_env(env):

    @env.macro
    def newIn(pluginVersion):
        return '!!! tip "Available as of ' + pluginVersion + '"\n\n\tThis feature is only available in ' + pluginVersion + '!  If you are running into problems [check your plugin version](/faqs/general/#check-installed-plugin-version) first.'.format(pluginVersion)

    @env.macro
    def removedIn(pluginVersion, canBeAdded = True):
        result = '!!! warning "Feature removed in ' + pluginVersion + '"\n\n\tThis feature was removed as of ' + pluginVersion + ' and is no longer supported by BarRaider or his community.<br /><br />'
        if(canBeAdded):
            result += 'If you would like to see this feature, or something like it, return,  why not [leave a suggestion in Discord](https://discord.com/channels/538862772285603880/607626003992281100/654236453655543808)?  Of course, you need to join the server first.'
        else:
            result += '**Please Note:** Unfortunately, we are unable to provide a suitable alternative implementation at this time.  This usually only occurs when a 3rd party (such as Spotify or Twitch) removes or alters a feature of their service that the plugin previously relied on'  
        return result

    @env.macro
    def centeredImage(image, caption = None):
        alt = ''
        hasCaption = caption is not None

        if(hasCaption):
            alt = 'alt="' + caption + '" '

        result =  '<p align="center">\n'
        result += '<img src="' + image + '" ' + alt + '/>\n'

        if(hasCaption):
            result += '<div style="text-align:center">\n<figcaption>' + caption + '</figcaption>\n</div>\n'
            
        result += '</p>'
        return result