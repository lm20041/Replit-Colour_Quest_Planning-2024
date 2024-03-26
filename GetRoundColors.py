import random

color_list_hex = [
  ['aliceblue', '#f0f8ff', '19', 'black'],
  ['antiquewhite', '#faebd7', '25', 'black'],
  ['aqua', '#00ffff', '15', 'black'],
  ['aquamarine', '#7fffd4', '27', 'black'],
  ['azure', '#f0ffff', '14', 'black'],
  ['beige', '#f5f5dc', '10', 'black'],
  ['bisque', '#ffe4c4', '13', 'black'],
  ['black', '#000000', '1', 'white'],
  ['blanchedalmond', '#ffebcd', '26', 'black'],
  ['blue', '#0000ff', '2', 'white'],
  ['blueviolet', '#8a2be2', '28', 'white'],
  ['brown', '#a52a2a', '5', 'white'],
  ['burlywood', '#deb887', '20', 'black'],
  ['cadetblue', '#5f9ea0', '24', 'white'],
  ['chartreuse', '#7fff00', '16', 'black'],
  ['chocolate', '#d2691e', '6', 'white'],
  ['coral', '#ff7f50', '7', 'black'],
  ['cornflowerblue', '#6495ed', '18', 'white'],
  ['cornsilk', '#fff8dc', '12', 'black'],
  ['crimson', '#dc143c', '8', 'white'],
  ['cyan', '#00ffff', '15', 'black'],
  ['darkblue', '#00008b', '3', 'white'],
  ['darkcyan', '#008b8b', '17', 'white'],
  ['darkgoldenrod', '#b8860b', '21', 'white'],
  ['darkgray', '#a9a9a9', '9', 'white'],
  ['darkgreen', '#006400', '29', 'white'],
  ['darkgrey', '#a9a9a9', '9', 'white'],
  ['darkkhaki', '#bdb76b', '22', 'black'],
  ['darkmagenta', '#8b008b', '30', 'white'],
  ['darkolivegreen', '#556b2f', '31', 'white'],
  ['darkorange', '#ff8c00', '23', 'black'],
  ['darkorchid', '#9932cc', '32', 'white'],
  ['darkred', '#8b0000', '4', 'white'],
  ['darksalmon', '#e9967a', '33', 'black'],
  ['darkseagreen', '#8fbc8f', '34', 'black'],
  ['darkslateblue', '#483d8b', '35', 'white'],
  ['darkslategray', '#2f4f4f', '36', 'white'],
  ['darkslategrey', '#2f4f4f', '36', 'white'],
  ['darkturquoise', '#00ced1', '37', 'black'],
  ['darkviolet', '#9400d3', '38', 'black'],
  ['deeppink', '#ff1493', '39', 'black'],
  ['deepskyblue', '#00bfff', '40', 'black'],
  ['dimgray', '#696969', '41', 'white'],
  ['dimgrey', '#696969', '41', 'white'],
  ['dodgerblue', '#1e90ff', '42', 'black'],
  ['firebrick', '#b22222', '43', 'white'],
  ['floralwhite', '#fffaf0', '44', 'black'],
  ['forestgreen', '#228b22', '45', 'white'],
  ['fuchsia', '#ff00ff', '46', 'black'],
  ['gainsboro', '#dcdcdc', '47', 'black'],
  ['ghostwhite', '#f8f8ff', '48', 'black'],
  ['gold', '#ffd700', '49', 'black'],
  ['goldenrod', '#daa520', '50', 'black'],
  ['gray', '#808080', '51', 'white'],
  ['green', '#008000', '52', 'white'],
  ['greenyellow', '#adff2f', '53', 'black'],
  ['grey', '#808080', '51', 'white'],
  ['honeydew', '#f0fff0', '54', 'black'],
  ['hotpink', '#ff69b4', '55', 'black'],
  ['indianred', '#cd5c5c', '56', 'black'],
  ['indigo', '#4b0082', '57', 'white'],
  ['ivory', '#fffff0', '58', 'black'],
  ['khaki', '#f0e68c', '59', 'black'],
  ['lavender', '#e6e6fa', '60', 'black'],
  ['lavenderblush', '#fff0f5', '61', 'black'],
  ['lawngreen', '#7cfc00', '62', 'black'],
  ['lemonchiffon', '#fffacd', '63', 'black'],
  ['lightblue', '#add8e6', '64', 'black'],
  ['lightcoral', '#f08080', '65', 'black'],
  ['lightcyan', '#e0ffff', '66', 'black'],
  ['lightgoldenrodyellow', '#fafad2', '67', 'black'],
  ['lightgray', '#d3d3d3', '68', 'black'],
  ['lightgreen', '#90ee90', '69', 'black'],
  ['lightgrey', '#d3d3d3', '68', 'black'],
  ['lightpink', '#ffb6c1', '70', 'black'],
  ['lightsalmon', '#ffa07a', '71', 'black'],
  ['lightseagreen', '#20b2aa', '72', 'black'],
  ['lightskyblue', '#87cefa', '73', 'black'],
  ['lightslategray', '#778899', '74', 'black'],
  ['lightslategrey', '#778899', '74', 'black'],
  ['lightsteelblue', '#b0c4de', '75', 'black'],
  ['lightyellow', '#ffffe0', '76', 'black'],
  ['lime', '#00ff00', '77', 'black'],
  ['limegreen', '#32cd32', '78', 'black'],
  ['linen', '#faf0e6', '79', 'black'],
  ['magenta', '#ff00ff', '80', 'black'],
  ['maroon', '#800000', '81', 'white'],
  ['mediumaquamarine', '#66cdaa', '82', 'black']]

print("we have started with {} colours!".format(len(color_list_hex)))

# loop 3 times (ie: 3 rounds)
color_total = 0
for item in range(0, 3):
  round_colour_list = []
  color_scores = []

  # loop 6 times (6 unique colours)
  while len(round_colour_list) < 6:
    # choose item
    chosen_colour = random.choice(color_list_hex)
    chosen_index = color_list_hex.index(chosen_colour)
    # check score not in list
    if chosen_colour[2] not in color_scores:
      # add to list
      round_colour_list.append(chosen_colour)
      # add to score list
      color_scores.append(chosen_index)
      color_total += int(chosen_colour[2])
  print("Round Colours:", round_colour_list)
  print("Round Scores:", color_total)