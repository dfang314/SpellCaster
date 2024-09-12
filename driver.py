import game
import timeout_player

players = [timeout_player.TimeoutPlayer(i) for i in range(4)]

active_game = game.Game(players)

active_game.play_game()
