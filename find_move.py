import points_player
import game_parser

players = [points_player.PointsPlayer(i) for i in range(4)]

grid, turn, round = game_parser.get_game_state(players)

move, details = players[turn].take_turn(grid, players, round)

print("The move that was found was", move)
print("With details", details) # TODO prettier print
