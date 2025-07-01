import game
import timeout_player
import points_player

players = [points_player.PointsPlayer(i) for i in range(3)]

active_game = game.Game(players)

active_game.play_game()
