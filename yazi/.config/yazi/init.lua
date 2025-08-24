-- ~/.config/yazi/init.lua
th.git = th.git or {}
th.git.modified_sign = "M"
th.git.deleted_sign = "D"

require("git"):setup()
require("no-status"):setup()
