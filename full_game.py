import game
import timeout_player
import points_player

players = [timeout_player.TimeoutPlayer(i) for i in range(3)]
players.append(points_player.PointsPlayer(3))

active_game = game.Game(players)

active_game.play_game()
